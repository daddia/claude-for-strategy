#!/usr/bin/env python3
"""Check that marketplace.json fields stay in sync with per-plugin plugin.json.

For each first-party plugin entry in marketplace.json, verifies that:
  - name matches plugin.json name
  - description matches plugin.json description
  - author.name and author.url match plugin.json author.*

Exits 0 when all checked plugins pass. Exits 1 with one error line per mismatch.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

CHECKED_FIELDS = ("name", "description")
CHECKED_AUTHOR_FIELDS = ("name", "url")


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _load_json(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot load {_display_path(path)}: {exc}", file=sys.stderr)
        sys.exit(2)


def check_sync() -> list[str]:
    marketplace = _load_json(MARKETPLACE_PATH)
    errors: list[str] = []

    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("./"):
            continue

        plugin_dir = REPO_ROOT / source.removeprefix("./")
        plugin_json_path = plugin_dir / ".claude-plugin" / "plugin.json"

        if not plugin_json_path.is_file():
            errors.append(
                f"{source}: missing {_display_path(plugin_json_path)}"
            )
            continue

        plugin = _load_json(plugin_json_path)

        for field in CHECKED_FIELDS:
            market_val = entry.get(field)
            plugin_val = plugin.get(field)
            if market_val != plugin_val:
                errors.append(
                    f"{source}: {field} mismatch\n"
                    f"  marketplace.json: {market_val!r}\n"
                    f"  plugin.json:      {plugin_val!r}"
                )

        market_author = entry.get("author") or {}
        plugin_author = plugin.get("author") or {}
        for field in CHECKED_AUTHOR_FIELDS:
            market_val = market_author.get(field)
            plugin_val = plugin_author.get(field)
            if market_val != plugin_val:
                errors.append(
                    f"{source}: author.{field} mismatch\n"
                    f"  marketplace.json: {market_val!r}\n"
                    f"  plugin.json:      {plugin_val!r}"
                )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check that marketplace.json name, description, and author fields "
            "match each plugin's .claude-plugin/plugin.json."
        )
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when any mismatch is found (default)",
    )
    args = parser.parse_args()

    if not args.check and len(sys.argv) == 1:
        args.check = True

    errors = check_sync()

    if errors:
        print("marketplace sync FAILED:", file=sys.stderr)
        for message in errors:
            print(f"  {message}", file=sys.stderr)
        return 1

    plugins = _load_json(MARKETPLACE_PATH).get("plugins", [])
    first_party = sum(
        1 for p in plugins
        if isinstance(p.get("source"), str) and p["source"].startswith("./")
    )
    print(f"  ✓ marketplace in sync ({first_party} first-party plugin(s) checked)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
