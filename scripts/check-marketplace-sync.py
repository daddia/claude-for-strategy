#!/usr/bin/env python3
"""Fail if marketplace.json plugin entries drift from each plugin's plugin.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SYNC_FIELDS = ("name", "description", "author")


def _load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _plugin_manifest_path(source: str) -> Path | None:
    if not source.startswith("./"):
        return None
    manifest = REPO_ROOT / source.removeprefix("./") / ".claude-plugin" / "plugin.json"
    return manifest if manifest.is_file() else None


def _field_drift(
    plugin_name: str,
    marketplace_entry: dict,
    plugin_manifest: dict,
) -> list[str]:
    drift: list[str] = []
    for field in SYNC_FIELDS:
        marketplace_value = marketplace_entry.get(field)
        plugin_value = plugin_manifest.get(field)
        if marketplace_value != plugin_value:
            drift.append(
                f"{plugin_name}.{field}: marketplace={marketplace_value!r} "
                f"plugin={plugin_value!r}"
            )
    return drift


def check_marketplace_sync() -> list[str]:
    marketplace = _load_json(MARKETPLACE_PATH)
    errors: list[str] = []

    for entry in marketplace.get("plugins", []):
        plugin_name = entry.get("name", "<unnamed>")
        source = entry.get("source")
        if not isinstance(source, str):
            errors.append(f"{plugin_name}: missing or invalid source")
            continue

        manifest_path = _plugin_manifest_path(source)
        if manifest_path is None:
            continue

        plugin_manifest = _load_json(manifest_path)
        errors.extend(_field_drift(plugin_name, entry, plugin_manifest))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Verify marketplace.json name, description, and author match each "
            "first-party plugin's .claude-plugin/plugin.json."
        )
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when marketplace entries drift from plugin.json (default)",
    )
    args = parser.parse_args()

    if not args.check and len(sys.argv) == 1:
        args.check = True

    if not args.check:
        parser.error("only --check is supported")

    errors = check_marketplace_sync()
    if errors:
        for message in errors:
            print(message, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
