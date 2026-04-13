import contextlib
import io
import json
import re
import subprocess
import sys
import time
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

import networkx as nx
import spacy
from pypdf import PdfReader
from spacy.language import Language

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
OUTPUT_DIR = Path("output")
LOG_PATH = OUTPUT_DIR / "pipeline.log"
DEFAULT_SPACY_MODEL = "en_core_web_sm"
CHAR_BLOCK_SIZE = 500


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    if LOG_PATH.exists():
        LOG_PATH.unlink()


def log_message(message: str) -> None:
    print(message)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(message + "\n")


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_pdf_text(pdf_path: Path) -> str:
    pages: List[str] = []
    with contextlib.redirect_stderr(io.StringIO()):
        reader = PdfReader(str(pdf_path))
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pages.append(page_text)
    return clean_text("\n\n".join(pages))


def load_raw_pdfs(raw_dir: Path = RAW_DIR) -> List[Dict[str, Any]]:
    if not raw_dir.exists() or not raw_dir.is_dir():
        raise FileNotFoundError(f"Pasta de raw não encontrada: {raw_dir}")

    paths = sorted(raw_dir.glob("*.pdf"))
    if not paths:
        raise FileNotFoundError(f"Nenhum arquivo PDF encontrado em {raw_dir}")

    documents: List[Dict[str, Any]] = []
    for path in paths:
        log_message(f"[INFO] Extraindo texto de {path.name}")
        try:
            text = extract_pdf_text(path)
        except Exception as exc:
            log_message(f"[ERROR] Falha ao ler {path.name}: {exc}")
            continue

        if not text:
            log_message(f"[WARN] Sem texto extraído de {path.name}")
            continue

        documents.append(
            {
                "id": path.stem,
                "title": path.stem,
                "text": text,
                "path": str(path),
            }
        )
    return documents


def save_extracted_texts(records: Iterable[Dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for record in records:
        file_name = f"{record['id']}.txt"
        path = output_dir / file_name
        with path.open("w", encoding="utf-8") as f:
            f.write(record.get("text", ""))
    log_message(f"[INFO] Textos extraídos salvos em {output_dir}")


def load_spacy_model(model_name: str = DEFAULT_SPACY_MODEL) -> Language:
    try:
        log_message(f"[INFO] Carregando spaCy model '{model_name}' com pipeline otimizada...")
        nlp = spacy.load(
            model_name,
            exclude=["parser", "attribute_ruler", "lemmatizer", "tagger"],
        )
    except OSError:
        log_message(f"[INFO] Modelo '{model_name}' não encontrado. Baixando...")
        subprocess.run([sys.executable, "-m", "spacy", "download", model_name], check=True)
        log_message(f"[INFO] Modelo '{model_name}' instalado. Recarregando...")
        nlp = spacy.load(
            model_name,
            exclude=["parser", "attribute_ruler", "lemmatizer", "tagger"],
        )

    if "sentencizer" not in nlp.pipe_names:
        nlp.add_pipe("sentencizer")

    return nlp


def extract_named_entities(text: str, nlp: Language) -> Set[str]:
    if not text:
        return set()
    doc = nlp(text)
    return {ent.text.strip().lower() for ent in doc.ents if ent.text.strip()}


def segment_text_by_sentence(text: str, nlp: Language) -> List[str]:
    if not text:
        return []
    doc = nlp(text)
    return [sentence.text.strip() for sentence in doc.sents if sentence.text.strip()]


def segment_text_by_paragraph(text: str) -> List[str]:
    paragraphs = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]
    return paragraphs or [text.strip()] if text.strip() else []


def segment_text_by_char_blocks(text: str, block_size: int = CHAR_BLOCK_SIZE) -> List[str]:
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return []
    return [normalized[i : i + block_size].strip() for i in range(0, len(normalized), block_size) if normalized[i : i + block_size].strip()]


def build_entity_cooccurrence_graph(records: Iterable[Dict[str, Any]], nlp: Language) -> nx.Graph:
    graph = nx.Graph()
    for record in records:
        text = record.get("text", "")
        entities = sorted(extract_named_entities(text, nlp))
        if len(entities) < 2:
            continue

        for entity in entities:
            if not graph.has_node(entity):
                graph.add_node(entity, entity=entity, document_count=0)
            graph.nodes[entity]["document_count"] += 1

        for left, right in combinations(entities, 2):
            if graph.has_edge(left, right):
                graph[left][right]["weight"] += 1
            else:
                graph.add_edge(left, right, weight=1)

    return graph


def save_graph_gexf(graph: nx.Graph, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_graph = graph.copy()
    for u, v, data in safe_graph.edges(data=True):
        for key, value in list(data.items()):
            if isinstance(value, (list, tuple, set, dict)):
                data[key] = json.dumps(value, ensure_ascii=False)
    nx.write_gexf(safe_graph, path)
    log_message(f"[INFO] Grafo salvo em GEXF em {path}")


def save_graph_svg(graph: nx.Graph, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if graph.number_of_nodes() == 0:
        log_message(f"[WARN] Grafo SVG não gerado porque o grafo está vazio.")
        return

    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(12, 12))
    ax.axis("off")
    layout = nx.spring_layout(graph, seed=42)
    nx.draw(
        graph,
        pos=layout,
        ax=ax,
        with_labels=True,
        node_size=400,
        font_size=8,
        node_color="#4c72b0",
        edge_color="#888888",
        linewidths=0.5,
    )
    fig.savefig(path, format="svg")
    plt.close(fig)
    log_message(f"[INFO] Grafo salvo em SVG em {path}")


def save_json(data: Any, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    log_message(f"[INFO] JSON salvo em {path}")


def analyze_segmentation(records: Iterable[Dict[str, Any]], nlp: Language, text_key: str = "text") -> Dict[str, Any]:
    strategies = {
        "sentence": lambda text: segment_text_by_sentence(text, nlp),
        "paragraph": segment_text_by_paragraph,
        "k_chars": lambda text: segment_text_by_char_blocks(text, CHAR_BLOCK_SIZE),
    }
    results: Dict[str, Any] = {}

    for name, segmenter in strategies.items():
        start_time = time.perf_counter()
        document_count = 0
        segment_count = 0
        entity_count = 0
        segments_with_entities = 0
        unique_entities: Set[str] = set()

        for record in records:
            text = record.get("text", "")
            if not text:
                continue
            document_count += 1
            segments = segmenter(text)
            segment_count += len(segments)

            for segment in segments:
                entities = extract_named_entities(segment, nlp)
                if not entities:
                    continue
                segments_with_entities += 1
                entity_count += len(entities)
                unique_entities.update(entities)

        elapsed = time.perf_counter() - start_time
        results[name] = {
            "documents_processed": document_count,
            "segments_total": segment_count,
            "segments_with_entities": segments_with_entities,
            "total_entities": entity_count,
            "unique_entities": len(unique_entities),
            "avg_entities_per_segment": round(entity_count / segments_with_entities, 3)
            if segments_with_entities
            else 0.0,
            "processing_time_seconds": round(elapsed, 3),
            "character_block_size": CHAR_BLOCK_SIZE if name == "k_chars" else None,
        }

    return results


def main() -> None:
    ensure_output_dir()
    log_message("[INFO] Iniciando pipeline de extração e análise de NER")

    try:
        records = load_raw_pdfs()
    except FileNotFoundError as exc:
        log_message(f"[ERROR] {exc}")
        return

    log_message(f"[INFO] {len(records)} documentos PDF carregados de {RAW_DIR}")
    save_extracted_texts(records, PROCESSED_DIR / "raw_texts")
    nlp = load_spacy_model()

    log_message("[STEP] Gerando grafo de co-ocorrência de entidades nomeadas")
    graph = build_entity_cooccurrence_graph(records, nlp)
    save_graph_gexf(graph, OUTPUT_DIR / "graph.gexf")
    save_graph_svg(graph, OUTPUT_DIR / "graph.svg")

    log_message("[STEP] Executando análise de desempenho por granulação de texto")
    metrics = analyze_segmentation(records, nlp)
    save_json(metrics, PROCESSED_DIR / "performance_metrics.json")

    save_json(records, PROCESSED_DIR / "pdf_documents.json")

    log_message("[CONCLUÍDO] Pipeline de análise finalizada")


if __name__ == "__main__":
    main()
