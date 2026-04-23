#!/usr/bin/env python3
"""Extract and clean summary and main body from markdown files.

Creates JSONL and per-document `.md` outputs under `data/processed/clean_texts/`.

Usage (CLI):
    python scripts/extract_main_content.py --input <file|dir> --out data/processed/clean_texts
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Optional


def clean_text(s: str) -> str:
    # minimal fallback normalizer: collapse whitespace
    return re.sub(r"\s+", " ", s or "").strip()


def remove_references_section(md: str) -> str:
    """Remove any content starting at a REFERENCES heading or standalone 'REFERÊNCIAS' line.

    This matches lines like 'REFERÊNCIAS', '# REFERÊNCIAS', 'REFERENCIAS' (case-insensitive),
    and cuts the document at that line.
    """
    if not md:
        return md
    m = re.search(
        r"(?im)^[ \t]*#*\s*(refer\w{0,10}|referênc|referenc|references)\b.*$", md
    )
    if m:
        return md[: m.start()].rstrip()
    return md


# Regexes and helpers for code/math/image/html blocks
RE_HTML_BLOCK = re.compile(
    r"(?is)<!--.*?-->|<script.*?>.*?</script>|<style.*?>.*?</style>|<table.*?>.*?</table>"
)
RE_HTML_IMG = re.compile(r"(?i)<img[^>]*>")
RE_FENCED_CODE = re.compile(r"(?ms)(^\s*(```|~~~).*?^\s*\2\s*$)")
RE_INDENTED_CODE = re.compile(r"(?m)(^(?: {4}|\t).*(?:\n(?: {4}|\t).*)*)")
RE_DISPLAY_MATH = re.compile(r"(?s)(\$\$.*?\$\$|\\\[.*?\\\])")
RE_INLINE_MATH_DOLLAR = re.compile(r"(?s)(?<!\$)\$(.+?)\$(?!\$)")
RE_INLINE_MATH_PARENS = re.compile(r"(?s)\\\((.+?)\\\)")
RE_LATEX_ENV = re.compile(r"(?s)\\begin\{.*?\}.*?\\end\{.*?\}")
RE_MARKDOWN_IMAGE = re.compile(r"!\[[^\]]*\]\([^\)]*\)")


def remove_html_blocks(text: str) -> str:
    # remove comments, script/style blocks and html img tags
    text = RE_HTML_BLOCK.sub("", text)
    text = RE_HTML_IMG.sub("", text)
    return text


def remove_markdown_tables(text: str) -> str:
    """Remove Markdown-style pipe tables and simple table captions."""
    if not text:
        return text
    # remove contiguous pipe-table blocks
    text = re.sub(r"(?m)^(?:\s*\|.*\n)+", "", text)
    # remove separator-only lines like '|---|---|' or '--- | ---'
    text = re.sub(r"(?m)^[\s\|\-:]+$\n?", "", text)
    # remove caption lines starting with Tabela / Table
    text = re.sub(r"(?im)^\s*(tabela|table)\s*\d+\b.*$\n?", "", text)
    return text


def remove_fenced_code_blocks(text: str) -> str:
    # Remove fenced code blocks and indented code entirely (omit)
    text = RE_FENCED_CODE.sub("", text)
    text = RE_INDENTED_CODE.sub("", text)
    return text


def remove_display_math_blocks(text: str) -> str:
    # remove display math blocks entirely
    return RE_DISPLAY_MATH.sub("", text)


def remove_inline_math(text: str, keep: bool = False) -> str:
    if keep:
        return text
    # remove inline math occurrences
    text = RE_INLINE_MATH_DOLLAR.sub("", text)
    text = RE_INLINE_MATH_PARENS.sub("", text)
    return text


def remove_latex_environments(text: str) -> str:
    # remove LaTeX environments entirely
    return RE_LATEX_ENV.sub("", text)


def remove_markdown_images(text: str) -> str:
    # remove markdown image links entirely
    return RE_MARKDOWN_IMAGE.sub("", text)


def normalize_whitespace(text: str) -> str:
    return clean_text(text or "")


HEADING_RE = re.compile(r"(?m)^(#{1,6}\s*.*)$")


def clean_preserve_structure(
    text: str, keep_inline_math: bool = False, convert_html_tables: bool = False
) -> str:
    """Clean the document while preserving markdown headings.

    Splits the document by heading lines and cleans each section independently,
    reattaching the heading even if the section becomes empty.
    """
    parts = []
    last_idx = 0
    headings = []
    for m in HEADING_RE.finditer(text):
        headings.append((m.start(), m.end(), m.group(0)))
    if not headings:
        # no headings: clean full text
        return clean_piece(
            text,
            keep_inline_math=keep_inline_math,
            convert_html_tables=convert_html_tables,
        )

    # handle pre-heading content
    first_start = headings[0][0]
    pre = text[0:first_start]
    pre_clean = clean_piece(
        pre, keep_inline_math=keep_inline_math, convert_html_tables=convert_html_tables
    )
    if pre_clean.strip():
        parts.append(pre_clean)

    for i, (s, e, hline) in enumerate(headings):
        # find end of this section (start of next heading or end of text)
        sec_start = e
        sec_end = headings[i + 1][0] if i + 1 < len(headings) else len(text)
        section = text[sec_start:sec_end]
        cleaned = clean_piece(
            section,
            keep_inline_math=keep_inline_math,
            convert_html_tables=convert_html_tables,
        )
        # Always include heading
        parts.append(hline.strip())
        # include cleaned content (may be empty)
        if cleaned.strip():
            parts.append(cleaned)

    return "\n\n".join(parts)


def split_into_sections(md: str):
    """Split a markdown document into a preface and a list of (heading, content) sections."""
    headings = list(HEADING_RE.finditer(md))
    if not headings:
        return md.strip(), []
    pre = md[: headings[0].start()].strip()
    sections = []
    for i, m in enumerate(headings):
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(md)
        heading = m.group(0).strip()
        content = md[start:end].strip()
        sections.append((heading, content))
    return pre, sections


def trim_to_summary_and_intro(md: str) -> str:
    """Keep only the `RESUMO|ABSTRACT` section and the `INTRODUÇÃO` section onward.

    If `RESUMO` not found, return original. If `INTRODUÇÃO` not found, keep from resumo to end.
    """
    pre, sections = split_into_sections(md)
    if not sections:
        return md
    # find resumo/abstract and introduction indices
    idx_res = None
    idx_intro = None
    for i, (h, _) in enumerate(sections):
        if idx_res is None and re.search(r"(?i)\b(resumo|abstract)\b", h):
            idx_res = i
        if idx_intro is None and re.search(
            r"(?i)^(?:#{0,}\s*)?(?:\d+\s*)?(introduc|introdução|introducao)\b", h
        ):
            idx_intro = i
        if idx_res is not None and idx_intro is not None:
            break
    if idx_res is None:
        return md
    if idx_intro is None:
        new_sections = sections[idx_res:]
    else:
        # keep resumo section and then everything from introducao onward
        new_sections = [sections[idx_res]] + sections[idx_intro:]

    parts = []
    for h, c in new_sections:
        parts.append(h)
        if c:
            parts.append(c)
    return "\n\n".join(parts)


def extract_summary(text: str) -> str:
    # find heading RESUMO / ABSTRACT (case-insensitive)
    m = re.search(r"(?im)^(?:\s*#{1,}\s*)?(resumo|abstract)\b.*$", text)
    if not m:
        return ""
    start = m.end()
    # find next heading INTRODUÇÃO or REFERENCES
    next_m = re.search(
        r"(?im)^(?:\s*#{1,}\s*)?(introduc|introdução|introducao|1\s+introduc|referen|references)\b",
        text[start:],
    )
    end = start + next_m.start() if next_m else len(text)
    return text[start:end].strip()


def clean_piece(
    text: str, keep_inline_math: bool = False, convert_html_tables: bool = False
) -> str:
    if not text:
        return ""
    t = text
    if not convert_html_tables:
        t = remove_html_blocks(t)
        # remove HTML/Markdown tables
        t = remove_markdown_tables(t)
    # remove markdown image syntax
    t = remove_markdown_images(t)
    # remove code blocks
    t = remove_fenced_code_blocks(t)
    # remove display math
    t = remove_display_math_blocks(t)
    # remove LaTeX envs
    t = remove_latex_environments(t)
    # inline math according to flag
    t = remove_inline_math(t, keep=keep_inline_math)
    # final whitespace normalization
    t = normalize_whitespace(t)
    return t


def process_file(
    path: Path,
    out_dir: Path,
    keep_inline_math: bool = False,
    convert_html_tables: bool = False,
) -> Optional[dict]:
    text = path.read_text(encoding="utf-8")
    summary_raw = extract_summary(text)
    summary = clean_piece(
        summary_raw,
        keep_inline_math=keep_inline_math,
        convert_html_tables=convert_html_tables,
    )
    # build a markdown-preserving cleaned version for body/output
    cleaned_md = clean_preserve_structure(
        text, keep_inline_math=keep_inline_math, convert_html_tables=convert_html_tables
    )
    # trim to keep only summary and introduction-onward, and remove everything before resumo
    cleaned_md = trim_to_summary_and_intro(cleaned_md)
    # ensure any REFERENCES section (with or without heading markdown) is removed
    cleaned_md = remove_references_section(cleaned_md)
    doc_id = path.stem
    out_dir.mkdir(parents=True, exist_ok=True)
    # write per-file markdown preserving headings/structure
    md_path = out_dir / f"{doc_id}.md"
    # include a small header referencing source path and write cleaned markdown preserving headings
    md_content = f"<!-- source: {path} -->\n\n" + cleaned_md
    md_path.write_text(md_content, encoding="utf-8")
    # append to jsonl
    jsonl_path = out_dir / "clean_texts.jsonl"
    record = {"id": doc_id, "path": str(path), "summary": summary, "body": cleaned_md}
    with jsonl_path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def main() -> None:
    p = argparse.ArgumentParser(
        description="Extract and clean main content from markdown files"
    )
    p.add_argument("--input", required=True, help="Input file or directory")
    p.add_argument(
        "--out", default="data/processed/clean_texts", help="Output directory"
    )
    p.add_argument(
        "--keep-inline-math", action="store_true", help="Preserve inline math"
    )
    p.add_argument(
        "--convert-html-tables",
        action="store_true",
        help="Convert HTML tables instead of removing (not implemented)",
    )
    args = p.parse_args()

    inp = Path(args.input)
    out = Path(args.out)
    files = []
    if inp.is_dir():
        files = sorted([p for p in inp.glob("*.md")])
    elif inp.is_file():
        files = [inp]
    else:
        raise FileNotFoundError(f"No such input: {inp}")

    results = []
    for f in files:
        try:
            rec = process_file(
                f,
                out,
                keep_inline_math=args.keep_inline_math,
                convert_html_tables=args.convert_html_tables,
            )
            results.append(rec)
            print(f"[OK] Processed {f}")
        except Exception as e:
            print(f"[ERROR] {f}: {e}")


if __name__ == "__main__":
    main()
