from pathlib import Path
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest

from main import (
    analyze_segmentation,
    build_entity_cooccurrence_graph,
    clean_text,
    save_extracted_texts,
    segment_text_by_char_blocks,
    segment_text_by_paragraph,
)


class DummyEnt:
    def __init__(self, text: str) -> None:
        self.text = text


class DummySentence:
    def __init__(self, text: str) -> None:
        self.text = text


class DummyDoc:
    def __init__(self, text: str) -> None:
        normalized = text.lower()
        self.ents = [DummyEnt(entity) for entity in ["alice", "bob", "carol"] if entity in normalized]
        self.sents = [DummySentence(sentence.strip()) for sentence in text.split(".") if sentence.strip()]


class DummyNLP:
    def __call__(self, text: str) -> DummyDoc:
        return DummyDoc(text)


def test_clean_text():
    assert clean_text("  Hello\nWorld  ") == "Hello World"


def test_segment_text_by_paragraph():
    paragraphs = segment_text_by_paragraph("First paragraph.\n\nSecond paragraph.")
    assert paragraphs == ["First paragraph.", "Second paragraph."]


def test_segment_text_by_char_blocks():
    text = "a" * 520
    blocks = segment_text_by_char_blocks(text, block_size=200)
    assert len(blocks) == 3
    assert blocks[0] == "a" * 200


def test_save_extracted_texts(tmp_path: Path):
    records = [{"id": "sample", "text": "hello world"}]
    save_extracted_texts(records, tmp_path)
    assert (tmp_path / "sample.txt").read_text(encoding="utf-8") == "hello world"


def test_build_entity_cooccurrence_graph():
    records = [
        {"id": "1", "title": "doc1", "text": "Alice and Bob went to the park."},
        {"id": "2", "title": "doc2", "text": "Alice met Carol and Bob."},
    ]
    graph = build_entity_cooccurrence_graph(records, DummyNLP())
    assert set(graph.nodes()) == {"alice", "bob", "carol"}
    assert graph["alice"]["bob"]["weight"] == 2
    assert graph["alice"]["carol"]["weight"] == 1


def test_analyze_segmentation():
    records = [{"id": "1", "text": "Alice. Bob."}]
    metrics = analyze_segmentation(records, DummyNLP(), text_key="text")
    assert metrics["sentence"]["documents_processed"] == 1
    assert metrics["paragraph"]["segments_total"] == 1
    assert metrics["k_chars"]["segments_total"] >= 1
    assert metrics["sentence"]["unique_entities"] >= 1
