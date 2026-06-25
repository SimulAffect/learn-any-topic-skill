#!/usr/bin/env python3
"""Lightweight tutorial draft review.

This script uses only the Python standard library. It checks common issues in
Markdown or plain text tutorials and prints actionable warnings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


GENERIC_TERMS = [
    "better",
    "good",
    "great",
    "stable",
    "smooth",
    "simple",
    "easy",
    "user-friendly",
    "robust",
    "更好",
    "更稳",
    "更顺",
    "很好",
]

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b",
    r"\bTBD\b",
    r"\bFIXME\b",
    r"\[TODO[^\]]*\]",
    r"\{\{[^}]+\}\}",
]

NEGATIVE_OPENING_PATTERNS = [
    r"^\s*(this|it|the topic)\s+is\s+not\b",
    r"^\s*not\s+",
    r"^\s*不是",
    r"^\s*并不是",
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        if line.strip():
            return line.strip()
    return ""


def has_any(text: str, markers: list[str]) -> bool:
    lower = text.lower()
    return any(marker.lower() in lower for marker in markers)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: review_tutorial.py path/to/tutorial.md", file=sys.stderr)
        return 2

    path = Path(argv[1])
    if not path.exists():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2

    text = read_text(path)
    lower = text.lower()
    warnings: list[str] = []

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            warnings.append(f"Placeholder pattern remains: {pattern}")

    opening = first_nonempty_line(text)
    for pattern in NEGATIVE_OPENING_PATTERNS:
        if re.search(pattern, opening, re.IGNORECASE):
            warnings.append("Opening starts by saying what the topic is not; define what it is first.")
            break

    repeated_generic = []
    for term in GENERIC_TERMS:
        count = lower.count(term.lower())
        if count >= 3:
            repeated_generic.append(f"{term} ({count})")
    if repeated_generic:
        warnings.append("Repeated generic wording: " + ", ".join(repeated_generic))

    source_markers = ["http://", "https://", "doi:", "references", "sources", "参考", "来源"]
    glossary_markers = ["glossary", "terms", "术语", "词汇"]
    practice_markers = ["exercise", "practice", "checklist", "self-check", "练习", "检查清单"]

    if not has_any(text, source_markers):
        warnings.append("No clear source or reference marker found.")
    if not has_any(text, glossary_markers):
        warnings.append("No clear glossary or terminology section marker found.")
    if not has_any(text, practice_markers):
        warnings.append("No clear practice, exercise, or checklist marker found.")

    heading_count = len(re.findall(r"(?m)^#{1,6}\s+\S+", text))
    if heading_count < 4 and len(text) > 4000:
        warnings.append("Long tutorial has few Markdown headings; navigation may be weak.")

    print(f"Reviewed: {path}")
    print(f"Characters: {len(text)}")
    print(f"Markdown headings: {heading_count}")
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
    else:
        print("No obvious tutorial quality warnings found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
