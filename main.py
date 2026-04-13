import json
import re
import subprocess
import sys
from itertools import combinations
from pathlib import Path
from typing import Any, Dict, Iterable, List, Set

import networkx as nx
import spacy
from spacy.language import Language

RAW_DIR = Path("data/raw")
OUTPUT_DIR = Path("output")
LOG_PATH = OUTPUT_DIR / "pipeline.log"
DEFAULT_SPACY_MODEL = "en_core_web_sm"


def ensure_output_dir() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    if LOG_PATH.exists():
        LOG_PATH.unlink()


def log_message(message: str) -> None:
    print(message)
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(message + "\n")


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_raw_records(raw_dir: Path = RAW_DIR) -> List[Dict[str, Any]]:
    if not raw_dir.exists() or not raw_dir.is_dir():
        raise FileNotFoundError(f"Pasta de raw não encontrada: {raw_dir}")

    paths = sorted(raw_dir.glob("*.json"))
    if not paths:
        raise FileNotFoundError(f"Nenhum arquivo JSON encontrado em {raw_dir}")

    records: List[Dict[str, Any]] = []
    for path in paths:
        with path.open("r", encoding="utf-8") as f:
            batch = json.load(f)
        for item in batch:
            title = item.get("title", "")
            if not title or not title.strip():
                continue
            records.append(
                {
                    "id": item.get("id"),
                    "title": title.strip(),
                    "synopsis": clean_text(item.get("synopsis", "")),
                    "year": item.get("year"),
                    "genres": item.get("genres", []),
                }
            )
    return records


def load_spacy_model(model_name: str = DEFAULT_SPACY_MODEL) -> Language:
    try:
        log_message(f"[INFO] Carregando spaCy model '{model_name}'...")
        return spacy.load(model_name)
    except OSError:
        log_message(f"[INFO] Modelo '{model_name}' não encontrado. Baixando...")
        subprocess.run([sys.executable, "-m", "spacy", "download", model_name], check=True)
        log_message(f"[INFO] Modelo '{model_name}' instalado. Recarregando...")
        return spacy.load(model_name)


def extract_named_entities(text: str, nlp: Language) -> Set[str]:
    if not text:
        return set()
    doc = nlp(text)
    return {ent.text.strip().lower() for ent in doc.ents if ent.text.strip()}


def build_entity_cooccurrence_graph(
    records: Iterable[Dict[str, Any]], nlp: Language
) -> nx.Graph:
    graph = nx.Graph()
    for record in records:
        entities = sorted(extract_named_entities(record.get("title", ""), nlp))
        if len(entities) < 2:
            continue

        for entity in entities:
            if not graph.has_node(entity):
                graph.add_node(entity, entity=entity, title_count=0)
            graph.nodes[entity]["title_count"] += 1

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


def main() -> None:
    ensure_output_dir()

    try:
        records = load_raw_records()
    except FileNotFoundError as exc:
        log_message(f"[ERROR] {exc}")
        return

    log_message(f"[INFO] {len(records)} registros carregados de data/raw")

    nlp = load_spacy_model()

    log_message("[STEP] Gerando grafo de co-ocorrência de entidades nomeadas a partir dos títulos")
    graph = build_entity_cooccurrence_graph(records, nlp)
    graph_path = OUTPUT_DIR / "graph.gexf"
    if graph.number_of_nodes() == 0:
        log_message("[WARN] O grafo ficou vazio. Verifique se os títulos contêm entidades nomeadas.")

    save_graph_gexf(graph, graph_path)
    log_message("[CONCLUÍDO] Pipeline finalizada com saída direta para GEXF")


if __name__ == "__main__":
    main()
