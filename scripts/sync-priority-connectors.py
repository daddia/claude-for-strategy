#!/usr/bin/env python3
"""Merge priority MCP server entries from references/priority-mcp-servers.json into plugin .mcp.json files."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PRIORITY_PATH = REPO_ROOT / "references" / "priority-mcp-servers.json"
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

BI_PLUGINS = {
    "performance",
    "corporate-strategy",
    "balanced-scorecard",
    "transformation",
    "value-realisation",
    "pmo",
}


def _first_party_plugins() -> list[str]:
    with MARKETPLACE_PATH.open(encoding="utf-8") as handle:
        marketplace = json.load(handle)
    names: list[str] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if isinstance(source, str) and source.startswith("./"):
            names.append(source.removeprefix("./"))
    return sorted(names)


def _load_priority() -> dict:
    with PRIORITY_PATH.open(encoding="utf-8") as handle:
        return json.load(handle)


def _merge_servers(mcp_path: Path, servers: dict[str, dict]) -> bool:
    with mcp_path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    existing = data.setdefault("mcpServers", {})
    changed = False
    for key, entry in servers.items():
        if key not in existing:
            existing[key] = entry
            changed = True
    if not changed:
        return False
    with mcp_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return True


def _ensure_categories(mcp_path: Path, categories: list[str]) -> bool:
    with mcp_path.open(encoding="utf-8") as handle:
        data = json.load(handle)
    rec = data.setdefault("recommendedCategories", [])
    changed = False
    for category in categories:
        if category not in rec:
            rec.append(category)
            changed = True
    if not changed:
        return False
    with mcp_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    return True


def sync_priority_connectors() -> list[str]:
    priority = _load_priority()
    updated: list[str] = []
    for plugin in _first_party_plugins():
        mcp_path = REPO_ROOT / plugin / ".mcp.json"
        if not mcp_path.is_file():
            continue
        servers: dict[str, dict] = {}
        servers.update(priority.get("universal", {}))
        if plugin in BI_PLUGINS:
            servers.update(priority.get("bi_analytics", {}))
        if _merge_servers(mcp_path, servers):
            updated.append(str(mcp_path.relative_to(REPO_ROOT)))
        extra_categories: list[str] = []
        if plugin in BI_PLUGINS:
            extra_categories.append("bi-analytics")
        if _ensure_categories(mcp_path, extra_categories):
            rel = str(mcp_path.relative_to(REPO_ROOT))
            if rel not in updated:
                updated.append(rel)
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync priority MCP servers into plugin .mcp.json files.")
    parser.add_argument("--check", action="store_true", help="exit 1 if any plugin is missing priority entries")
    args = parser.parse_args()

    priority = _load_priority()
    expected_keys = set(priority.get("universal", {}))
    if args.check:
        errors: list[str] = []
        for plugin in _first_party_plugins():
            mcp_path = REPO_ROOT / plugin / ".mcp.json"
            if not mcp_path.is_file():
                continue
            with mcp_path.open(encoding="utf-8") as handle:
                data = json.load(handle)
            servers = data.get("mcpServers", {})
            for key in expected_keys:
                if key not in servers:
                    errors.append(f"{mcp_path.relative_to(REPO_ROOT)}: missing priority server {key!r}")
            if plugin in BI_PLUGINS:
                for key in priority.get("bi_analytics", {}):
                    if key not in servers:
                        errors.append(f"{mcp_path.relative_to(REPO_ROOT)}: missing bi server {key!r}")
        if errors:
            print("priority connector sync FAILED:", file=sys.stderr)
            for message in errors:
                print(f"  {message}", file=sys.stderr)
            return 1
        print(f"  ✓ priority connectors present in {len(_first_party_plugins())} plugin(s)")
        return 0

    updated = sync_priority_connectors()
    if updated:
        for path in updated:
            print(f"  updated {path}")
    else:
        print("  ✓ all plugins already have priority connectors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
