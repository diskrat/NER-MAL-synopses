#!/usr/bin/env python3
"""Basic spaCy runner for pt-br documents.

Reads `data/processed/clean_texts` (JSONL `clean_texts.jsonl` or `.md` files),
runs a Portuguese spaCy model and writes per-document JSON outputs with
sentences and named entities under the output directory.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Iterator, Any, Iterable, List, Set
import time
import re

import networkx as nx
from collections import Counter


def load_spacy_model(name: str):
    try:
        import spacy

        return spacy.load(name)
    except Exception:
        try:
            import spacy
            from spacy.cli.download import download

            print(
                f"Model '{name}' not found, attempting to download...", file=sys.stderr
            )
            download(name)
            return spacy.load(name)
        except Exception as e:
            print(f"Failed to load/download spaCy model '{name}': {e}", file=sys.stderr)
            raise


# Pipeline constants (align with main.py defaults)
PROCESSED_DIR = Path("data/processed")
OUTPUT_DIR = Path("output")
LOG_PATH = OUTPUT_DIR / "pipeline.log"
FILTER_LABELS = {
    "PERSON",
    "PER",
    "ORG",
    "GPE",
    "LOC",
    "NORP",
    "PRODUCT",
    "EVENT",
    "WORK_OF_ART",
    "LAW",
    "MISC",
}
ENTITIES_PER_DOC = 40
CHAR_BLOCK_SIZE = 500
K_CHAR_SIZES = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]


def log_message(msg: str) -> None:
    print(msg)
    try:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except Exception:
        pass


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


def save_graph_gexf(graph: nx.Graph, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mapping = {n: i for i, n in enumerate(graph.nodes())}
    H = nx.relabel_nodes(graph, mapping, copy=True)
    for new_id, data in H.nodes(data=True):
        original = (
            data.get("entity")
            if data.get("entity")
            else next((o for o, v in mapping.items() if v == new_id), str(new_id))
        )
        H.nodes[new_id]["label"] = original
        H.nodes[new_id]["entity"] = original

    raw = nx.generate_gexf(H)
    if isinstance(raw, (list, tuple)):
        content = "\n".join(raw)
    elif isinstance(raw, str):
        content = raw
    else:
        content = "\n".join(list(raw))

    content = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), content)
    content = re.sub(r"&#x([0-9a-fA-F]+);", lambda m: chr(int(m.group(1), 16)), content)
    if not content.lstrip().startswith("<?xml"):
        content = '<?xml version="1.0" encoding="utf-8"?>\n' + content

    with path.open("w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def iter_documents(inp: Path) -> Iterator[Dict]:
    """Yield dicts {'id':..., 'text':...} from input path.

    Read only Markdown files (`.md`). If `inp` is a file it must be an `.md` file.
    If `inp` is a directory, iterate all `*.md` files inside.
    """
    if not inp.exists():
        raise FileNotFoundError(f"No such input: {inp}")

    if inp.is_file():
        if inp.suffix.lower() != ".md":
            raise ValueError("Input file must be a Markdown (.md) file")
        yield {"id": inp.stem, "text": inp.read_text(encoding="utf-8")}
        return

    # directory: iterate .md files only
    for p in sorted(inp.glob("*.md")):
        yield {"id": p.stem, "text": p.read_text(encoding="utf-8")}


def process_doc(nlp, doc_obj: Dict) -> Dict:
    doc = nlp(doc_obj.get("text") or "")
    out = {
        "id": doc_obj.get("id"),
        "ents": [
            {
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_,
                "text": ent.text,
            }
            for ent in doc.ents
        ],
    }
    return out


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description="Run spaCy over cleaned documents (pt-BR)")
    p.add_argument(
        "--input",
        "-i",
        default="data/processed/clean_texts",
        help="Input file or directory",
    )
    p.add_argument(
        "--out", "-o", default="data/processed/spacy", help="Output directory"
    )
    p.add_argument(
        "--model", "-m", default="pt_core_news_lg", help="spaCy model name (pt-BR)"
    )
    args = p.parse_args(argv)

    inp = Path(args.input)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    try:
        nlp = load_spacy_model(args.model)
    except Exception:
        print(
            "Cannot load spaCy model. Install it manually and retry.", file=sys.stderr
        )
        sys.exit(2)

    # enable sentence segmentation if not present
    if not nlp.pipe_names:
        # this is unlikely, but ensure the pipeline can produce sentences
        try:
            nlp.add_pipe("sentencizer")
        except Exception:
            pass

    # Prepare pipeline accumulators similar to main.py
    graphs: Dict[str, nx.Graph] = {"sentence": nx.Graph(), "paragraph": nx.Graph()}
    # add one graph per k-char size
    for k in K_CHAR_SIZES:
        graphs[f"k_chars_{k}"] = nx.Graph()
    entities_path = PROCESSED_DIR / "entities.jsonl"
    if entities_path.exists():
        try:
            entities_path.unlink()
        except Exception:
            pass

    metrics_acc: Dict[str, Any] = {}
    for name in ("sentence", "paragraph"):
        metrics_acc[name] = {
            "documents_processed": 0,
            "segments_total": 0,
            "segments_with_entities": 0,
            "total_entities": 0,
            "unique_entities": set(),
            "processing_time_seconds": 0.0,
        }
    for k in K_CHAR_SIZES:
        metrics_acc[f"k_chars_{k}"] = {
            "documents_processed": 0,
            "segments_total": 0,
            "segments_with_entities": 0,
            "total_entities": 0,
            "unique_entities": set(),
            "processing_time_seconds": 0.0,
        }

    processed_count = 0
    for doc_obj in iter_documents(inp):
        processed_count += 1
        # write per-doc JSON as before
        out_obj = process_doc(nlp, doc_obj)
        path = out / f"{out_obj['id']}.json"
        path.write_text(
            json.dumps(out_obj, ensure_ascii=False, indent=None), encoding="utf-8"
        )
        print(f"Wrote {path}")

        text = doc_obj.get("text", "") or ""
        if not text:
            continue

        # build full spaCy Doc for segmentation + filtering
        doc = nlp(text)
        limited_entities = extract_limited_entities_from_doc(doc)
        append_entities_jsonl(
            doc_obj.get("id") or Path(path).stem, limited_entities, entities_path
        )

        # per-strategy accumulators
        seen_in_doc: Dict[str, Set[str]] = {name: set() for name in graphs.keys()}
        sentence_segments = [
            s.text.strip() for s in getattr(doc, "sents", []) if s.text.strip()
        ]
        paragraph_segments = segment_text_by_paragraph(text)
        segments_map = {"sentence": sentence_segments, "paragraph": paragraph_segments}
        # add one k_chars segmentation per configured block size
        for k in K_CHAR_SIZES:
            segments_map[f"k_chars_{k}"] = segment_text_by_char_blocks(
                text, block_size=k
            )

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
                metrics_acc[name]["segments_with_entities"] += 1
                metrics_acc[name]["total_entities"] += len(entities_in_seg)
                metrics_acc[name]["unique_entities"].update(entities_in_seg)

                for ent in entities_in_seg:
                    if not G.has_node(ent):
                        G.add_node(ent, entity=ent, document_count=0)
                    if ent not in seen_in_doc[name]:
                        G.nodes[ent]["document_count"] += 1
                        seen_in_doc[name].add(ent)

                for a, b in __import__("itertools").combinations(
                    sorted(entities_in_seg), 2
                ):
                    if G.has_edge(a, b):
                        G[a][b]["weight"] += 1
                    else:
                        G.add_edge(a, b, weight=1)

            metrics_acc[name]["processing_time_seconds"] += time.perf_counter() - start

    log_message(f"[INFO] Processed {processed_count} documents from {inp}")

    # Save graphs and compute degree distributions
    degree_distributions: Dict[str, Dict[int, int]] = {}
    for name, G in graphs.items():
        out_path = OUTPUT_DIR / f"graph_{name}.gexf"
        save_graph_gexf(G, out_path)
        # compute degree distribution: degree -> count
        degs = [d for _, d in G.degree()]
        # produce an ordered mapping degree -> count (sorted by degree)
        degree_counts = dict(sorted(Counter(degs).items()))
        degree_distributions[name] = degree_counts

    # compose final metrics including degree distributions
    final_metrics = {}
    for k, v in metrics_acc.items():
        final_metrics[k] = {
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
            "degree_distribution": degree_distributions.get(k, {}),
        }

    save_json(final_metrics, PROCESSED_DIR / "performance_metrics.json")

    log_message("[DONE] Pipeline finished")


if __name__ == "__main__":
    main()
