#!/usr/bin/env python3
"""Validate repository documentation links and public identity policy."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

markdown_files = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.parts)
for path in markdown_files:
    content = path.read_text(encoding="utf-8")
    relative = path.relative_to(ROOT)
    if content.count("```") % 2:
        ERRORS.append(f"{relative}: unmatched fenced code block")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", content):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        clean_target = target.split("#", 1)[0]
        if clean_target and not (path.parent / clean_target).resolve().exists():
            ERRORS.append(f"{relative}: missing local link target {target}")

scannable = [path for path in ROOT.rglob("*") if path.is_file() and ".git" not in path.parts]
all_text = "\n".join(path.read_text(encoding="utf-8", errors="ignore") for path in scannable).lower()
for forbidden in ("mamu" + "duri", "jeevanm.aws" + "@gmail.com", "akia" + "iosf"):
    if forbidden in all_text:
        ERRORS.append("Repository contains a prohibited identity or credential pattern")

if ERRORS:
    print("Repository validation failed:", file=sys.stderr)
    for error in ERRORS:
        print(f"- {error}", file=sys.stderr)
    raise SystemExit(1)

print(f"Documentation and identity checks passed for {len(markdown_files)} Markdown files.")
