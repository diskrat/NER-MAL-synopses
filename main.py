import json
import re
import subprocess
import sys
import time
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set, Iterator

import networkx as nx
import spacy
from pypdf import PdfReader

# Paths and defaults
RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_DIR = Path("output")
LOG_PATH = OUTPUT_DIR / "pipeline.log"

DEFAULT_SPACY_MODEL = "pt_core_news_sm"
MODEL_CANDIDATES = ["pt_core_news_lg", "pt_core_news_sm"]
ENTITIES_PER_DOC = 20
FILE_LIMIT = 25
FILTER_LABELS = {"PERSON", "PER", "ORG", "GPE", "LOC"}
CHAR_BLOCK_SIZE = 2000


def ensure_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def log_message(msg: str) -> None:
    print(msg)
    try:
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


def clean_text(text: str) -> str:
    # Preserve paragraph breaks (double newlines) while normalizing
    # whitespace inside paragraphs to single spaces.
    if not text:
        return ""
    # Normalize newlines
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    # Split on blank-line boundaries, clean each paragraph, then join
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", text)]
    paras = [p for p in paras if p]
    return "\n\n".join(paras)


def extract_pdf_text(pdf_path: Path) -> str:
    pages: List[str] = []
    try:
        reader = PdfReader(str(pdf_path))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pages.append(page_text)
    except Exception as e:
        log_message(f"[ERROR] Failed reading {pdf_path.name}: {e}")
        return ""
    # Join pages with blank-line separators so paragraph boundaries
    # can be preserved during cleaning.
    return clean_text("\n\n".join(pages))


def load_raw_pdfs(raw_dir: Path = RAW_DIR) -> Iterator[Dict[str, Any]]:
    if not raw_dir.exists() or not raw_dir.is_dir():
        raise FileNotFoundError(f"No raw folder: {raw_dir}")
    for path in sorted(raw_dir.glob("*.pdf")):
        text = extract_pdf_text(path)
        if not text:
            continue
        yield {"id": path.stem, "title": path.stem, "text": text, "path": str(path)}


def save_extracted_texts(records: Iterable[Dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for rec in records:
        p = output_dir / f"{rec['id']}.txt"
        with p.open("w", encoding="utf-8") as f:
            f.write(rec.get("text", ""))


def choose_nlp_model(candidates: List[str] = MODEL_CANDIDATES):
    for m in candidates:
        try:
            nlp = spacy.load(
                m, exclude=["parser", "attribute_ruler", "lemmatizer", "tagger"]
            )
            if "sentencizer" not in nlp.pipe_names:
                nlp.add_pipe("sentencizer")
            return nlp
        except Exception:
            continue
    # attempt download of default
    subprocess.run(
        [sys.executable, "-m", "spacy", "download", DEFAULT_SPACY_MODEL], check=True
    )
    nlp = spacy.load(
        DEFAULT_SPACY_MODEL,
        exclude=["parser", "attribute_ruler", "lemmatizer", "tagger"],
    )
    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")
    return nlp


def extract_limited_entities_from_doc(
    doc: Any,
    max_entities: int = ENTITIES_PER_DOC,
    filter_labels: Set[str] | None = FILTER_LABELS,
) -> Set[str]:
    ents_ordered: List[str] = []
    for ent in getattr(doc, "ents", []) or []:
        text = getattr(ent, "text", "")
        if not text or not text.strip():
            continue
        text = text.strip().lower()
        label = getattr(ent, "label_", None)
        if (
            filter_labels
            and label
            and label.upper() not in {fl.upper() for fl in filter_labels}
        ):
            continue
        ents_ordered.append(text)
    seen: Set[str] = set()
    unique: List[str] = []
    for e in ents_ordered:
        if e not in seen:
            seen.add(e)
            unique.append(e)
        if len(unique) >= max_entities:
            break
    return set(unique)


def segment_text_by_paragraph(text: str) -> List[str]:
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paras or ([text.strip()] if text.strip() else [])


def segment_text_by_char_blocks(
    text: str, block_size: int = CHAR_BLOCK_SIZE
) -> List[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    return [
        normalized[i : i + block_size].strip()
        for i in range(0, len(normalized), block_size)
        if normalized[i : i + block_size].strip()
    ]


def build_entity_cooccurrence_graph(records: Iterable[Dict[str, Any]], nlp) -> nx.Graph:
    G = nx.Graph()
    for rec in records:
        text = rec.get("text", "")
        if not text:
            continue
        doc = nlp(text)
        entities = sorted(
            {
                ent.text.strip().lower()
                for ent in getattr(doc, "ents", [])
                if ent.text and ent.text.strip()
            }
        )
        if len(entities) < 2:
            continue
        for e in entities:
            if not G.has_node(e):
                G.add_node(e, entity=e, document_count=0)
            G.nodes[e]["document_count"] += 1
        for a, b in combinations(entities, 2):
            if G.has_edge(a, b):
                G[a][b]["weight"] += 1
            else:
                G.add_edge(a, b, weight=1)
    return G


def save_graph_gexf(graph: nx.Graph, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Export with short integer node ids to improve Gephi compatibility.
    mapping = {n: i for i, n in enumerate(graph.nodes())}
    H = nx.relabel_nodes(graph, mapping, copy=True)
    # Ensure each node has a human-readable label attribute for Gephi
    for new_id, data in H.nodes(data=True):
        # original entity text may be stored under 'entity' or be the original key
        original = (
            data.get("entity")
            if data.get("entity")
            else next((o for o, v in mapping.items() if v == new_id), str(new_id))
        )
        H.nodes[new_id]["label"] = original
        H.nodes[new_id]["entity"] = original

    # Generate full GEXF. networkx may return an iterable of lines
    # or a single string depending on version; normalize to string.
    raw = nx.generate_gexf(H)
    if isinstance(raw, (list, tuple)):
        content = "\n".join(raw)
    elif isinstance(raw, str):
        content = raw
    else:
        # Iterator/generator
        content = "\n".join(list(raw))

    # Replace decimal numeric refs: &#1234; -> actual char
    content = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), content)
    # Replace hex numeric refs: &#x1aF; -> actual char
    content = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), content)

    # Ensure XML declaration with UTF-8 encoding (if missing)
    if not content.lstrip().startswith("<?xml"):
        content = '<?xml version="1.0" encoding="utf-8"?>\n' + content

    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def save_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def append_entities_jsonl(record_id: str, entities: Iterable[str], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        json.dump(
            {"id": record_id, "entities": sorted(list(entities))}, f, ensure_ascii=False
        )
        f.write("\n")


def analyze_segmentation(
    records: Iterable[Dict[str, Any]], nlp, text_key: str = "text"
) -> Dict[str, Any]:
    strategies = ("sentence", "paragraph", "k_chars")
    accum: Dict[str, Any] = {
        name: {
            "documents_processed": 0,
            "segments_total": 0,
            "segments_with_entities": 0,
            "total_entities": 0,
            "unique_entities": set(),
            "processing_time_seconds": 0.0,
        }
        for name in strategies
    }
    for rec in records:
        text = rec.get(text_key, "")
        if not text:
            continue
        doc = nlp(text)
        sentence_segments = [
            s.text.strip() for s in getattr(doc, "sents", []) if s.text.strip()
        ]
        paragraph_segments = segment_text_by_paragraph(text)
        kchar_segments = segment_text_by_char_blocks(text)
        segments_map = {
            "sentence": sentence_segments,
            "paragraph": paragraph_segments,
            "k_chars": kchar_segments,
        }
        for name, segments in segments_map.items():
            start = time.perf_counter()
            accum[name]["documents_processed"] += 1
            accum[name]["segments_total"] += len(segments)
            for seg in segments:
                seg_lower = seg.lower()
                entities_in_seg = {
                    ent.text.strip().lower()
                    for ent in getattr(doc, "ents", [])
                    if ent.text
                    and ent.text.strip()
                    and ent.text.strip().lower() in seg_lower
                }
                if not entities_in_seg:
                    continue
                accum[name]["segments_with_entities"] += 1
                accum[name]["total_entities"] += len(entities_in_seg)
                accum[name]["unique_entities"].update(entities_in_seg)
            accum[name]["processing_time_seconds"] += time.perf_counter() - start
    results: Dict[str, Any] = {}
    for name in strategies:
        d = accum[name]
        results[name] = {
            "documents_processed": d["documents_processed"],
            "segments_total": d["segments_total"],
            "segments_with_entities": d["segments_with_entities"],
            "total_entities": d["total_entities"],
            "unique_entities": len(d["unique_entities"]),
            "avg_entities_per_segment": (
                round(d["total_entities"] / d["segments_with_entities"], 3)
                if d["segments_with_entities"]
                else 0.0
            ),
            "processing_time_seconds": round(d["processing_time_seconds"], 3),
            "character_block_size": CHAR_BLOCK_SIZE if name == "k_chars" else None,
        }
    return results


def main() -> None:
    ensure_dirs()
    log_message("[INFO] Starting pipeline")
    try:
        pdf_iter = load_raw_pdfs()
    except FileNotFoundError as exc:
        log_message(f"[ERROR] {exc}")
        return
    nlp = choose_nlp_model()
    # Create one graph per segmentation strategy so we can export
    # co-occurrence networks for sentences, paragraphs and k-char blocks.
    graphs: Dict[str, nx.Graph] = {
        "sentence": nx.Graph(),
        "paragraph": nx.Graph(),
        "k_chars": nx.Graph(),
    }
    entities_path = PROCESSED_DIR / "entities.jsonl"
    if entities_path.exists():
        entities_path.unlink()
    metrics_acc: Dict[str, Any] = {
        name: {
            "documents_processed": 0,
            "segments_total": 0,
            "segments_with_entities": 0,
            "total_entities": 0,
            "unique_entities": set(),
            "processing_time_seconds": 0.0,
        }
        for name in ("sentence", "paragraph", "k_chars")
    }
    processed_count = 0
    raw_texts_dir = PROCESSED_DIR / "raw_texts"
    raw_texts_dir.mkdir(parents=True, exist_ok=True)
    for record in pdf_iter:
        if processed_count >= FILE_LIMIT:
            break
        processed_count += 1
        record_id = record.get("id") or f"doc_{processed_count}"
        text = record.get("text", "")
        if not text:
            continue
        with (raw_texts_dir / f"{record_id}.txt").open("w", encoding="utf-8") as f:
            f.write(text)
        doc = nlp(text)
        limited_entities = extract_limited_entities_from_doc(doc)
        append_entities_jsonl(record_id, limited_entities, entities_path)

        # Track which entities were already counted for document_count
        # per graph to avoid double-counting across multiple segments
        # within the same document.
        seen_in_doc: Dict[str, Set[str]] = {
            name: set() for name in ("sentence", "paragraph", "k_chars")
        }

        # Build per-strategy co-occurrence graphs using limited entities
        # found inside each segment.
        sentence_segments = [
            s.text.strip() for s in getattr(doc, "sents", []) if s.text.strip()
        ]
        paragraph_segments = segment_text_by_paragraph(text)
        kchar_segments = segment_text_by_char_blocks(text)
        segments_map = {
            "sentence": sentence_segments,
            "paragraph": paragraph_segments,
            "k_chars": kchar_segments,
        }
        for name, segments in segments_map.items():
            start = time.perf_counter()
            metrics_acc[name]["documents_processed"] += 1
            metrics_acc[name]["segments_total"] += len(segments)
            G = graphs[name]
            for seg in segments:
                seg_lower = seg.lower()
                entities_in_seg = {e for e in limited_entities if e in seg_lower}
                if not entities_in_seg:
                    continue
                # Update metrics
                metrics_acc[name]["segments_with_entities"] += 1
                metrics_acc[name]["total_entities"] += len(entities_in_seg)
                metrics_acc[name]["unique_entities"].update(entities_in_seg)

                # Add nodes and update per-document counts once
                for ent in entities_in_seg:
                    if not G.has_node(ent):
                        G.add_node(ent, entity=ent, document_count=0)
                    if ent not in seen_in_doc[name]:
                        G.nodes[ent]["document_count"] += 1
                        seen_in_doc[name].add(ent)

                # Add co-occurrence edges for this segment
                for a, b in combinations(sorted(entities_in_seg), 2):
                    if G.has_edge(a, b):
                        G[a][b]["weight"] += 1
                    else:
                        G.add_edge(a, b, weight=1)

            metrics_acc[name]["processing_time_seconds"] += time.perf_counter() - start
    log_message(f"[INFO] Processed {processed_count} documents from {RAW_DIR}")
    # Save each per-strategy graph
    for name, G in graphs.items():
        out_path = OUTPUT_DIR / f"graph_{name}.gexf"
        save_graph_gexf(G, out_path)
    save_json(
        {
            k: {
                "documents_processed": v["documents_processed"],
                "segments_total": v["segments_total"],
                "segments_with_entities": v["segments_with_entities"],
                "total_entities": v["total_entities"],
                "unique_entities": len(v["unique_entities"]),
                "avg_entities_per_segment": (
                    round(v["total_entities"] / v["segments_with_entities"], 3)
                    if v["segments_with_entities"]
                    else 0.0
                ),
                "processing_time_seconds": round(v["processing_time_seconds"], 3),
            }
            for k, v in metrics_acc.items()
        },
        PROCESSED_DIR / "performance_metrics.json",
    )
    log_message("[DONE] Pipeline finished")


if __name__ == "__main__":
    main()
