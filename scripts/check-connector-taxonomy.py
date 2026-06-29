#!/usr/bin/env python3
"""Validate connector placeholders in markdown and machine categories in .mcp.json.

Canonical taxonomy: references/connector-taxonomy.json

  - Markdown uses human placeholders: `~~chat`, `~~knowledge base`, …
  - .mcp.json recommendedCategories uses machine slugs: chat, knowledge-base, …

Exits non-zero when unknown or deprecated placeholders/categories are found.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
TAXONOMY_PATH = REPO_ROOT / "references" / "connector-taxonomy.json"

_PLACEHOLDER_RE = re.compile(r"~~([a-z][a-z0-9 -]*)")
_SKIP_DIRS = {".git", ".cursor", "node_modules", "__pycache__"}


def _load_taxonomy() -> tuple[dict[str, str], set[str], set[str], dict[str, str]]:
    with TAXONOMY_PATH.open(encoding="utf-8") as handle:
        data = json.load(handle)

    placeholder_to_machine: dict[str, str] = {}
    machine_categories: set[str] = set()
    valid_placeholders: set[str] = set()

    for entry in data["categories"]:
        machine = entry["machine"]
        placeholder = entry["placeholder"]
        placeholder_to_machine[placeholder] = machine
        machine_categories.add(machine)
        valid_placeholders.add(placeholder)

    meta = set(data.get("meta_placeholders", []))
    valid_placeholders.update(meta)

    deprecated: dict[str, str] = dict(data.get("deprecated_placeholders", {}))

    return placeholder_to_machine, machine_categories, valid_placeholders, deprecated


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _iter_markdown_files() -> list[Path]:
    paths: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        paths.append(path)
    return sorted(paths)


def _iter_mcp_json_files() -> list[Path]:
    return sorted(REPO_ROOT.glob("**/.mcp.json"))


def _normalize_placeholder(raw: str) -> str:
    return raw.strip().rstrip(".,;:")


def check_markdown(
    path: Path,
    valid_placeholders: set[str],
    deprecated: dict[str, str],
) -> list[str]:
    rel = _display_path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read file: {exc}"]

    errors: list[str] = []
    seen: set[tuple[int, str]] = set()

    for match in _PLACEHOLDER_RE.finditer(text):
        placeholder = _normalize_placeholder(match.group(1))
        key = (match.start(), placeholder)
        if key in seen:
            continue
        seen.add(key)

        if placeholder in deprecated:
            replacement = deprecated[placeholder]
            errors.append(
                f"{rel}: deprecated placeholder ~~{placeholder} "
                f"(use ~~{replacement})"
            )
            continue

        if placeholder not in valid_placeholders:
            errors.append(f"{rel}: unknown placeholder ~~{placeholder}")

    return errors


def check_mcp_json(path: Path, machine_categories: set[str]) -> list[str]:
    rel = _display_path(path)
    try:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{rel}: cannot read JSON: {exc}"]

    errors: list[str] = []
    categories = data.get("recommendedCategories")
    if categories is None:
        return errors
    if not isinstance(categories, list):
        return [f"{rel}: recommendedCategories must be a list"]
    for category in categories:
        if not isinstance(category, str):
            errors.append(f"{rel}: recommendedCategories entries must be strings")
            continue
        if category not in machine_categories:
            errors.append(f"{rel}: unknown machine category {category!r}")
    return errors


def check_connector_taxonomy() -> list[str]:
    if not TAXONOMY_PATH.is_file():
        return [f"missing taxonomy file: {_display_path(TAXONOMY_PATH)}"]

    _, machine_categories, valid_placeholders, deprecated = _load_taxonomy()
    errors: list[str] = []

    md_paths = _iter_markdown_files()
    mcp_paths = _iter_mcp_json_files()

    for path in md_paths:
        errors.extend(check_markdown(path, valid_placeholders, deprecated))

    for path in mcp_paths:
        errors.extend(check_mcp_json(path, machine_categories))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate connector placeholders in markdown and categories in "
            ".mcp.json against references/connector-taxonomy.json."
        )
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when any violation is found (default)",
    )
    args = parser.parse_args()

    if not args.check and len(sys.argv) == 1:
        args.check = True

    errors = check_connector_taxonomy()
    if errors:
        print("connector taxonomy lint FAILED:", file=sys.stderr)
        for message in errors:
            print(f"  {message}", file=sys.stderr)
        return 1

    md_count = len(_iter_markdown_files())
    mcp_count = len(_iter_mcp_json_files())
    print(
        f"  ✓ connector taxonomy clean "
        f"({md_count} markdown file(s), {mcp_count} .mcp.json file(s))"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
