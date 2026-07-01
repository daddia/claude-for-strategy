#!/usr/bin/env python3
"""Add ## Propose profile update to first-party skills that lack it (except practice-setup)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

SECTION_TEMPLATE = """\
## Propose profile update

When a stable convention surfaces during this run (thresholds, naming, tone, output format, or recurring corrections), **propose a profile update**: show the exact diff against `~/.claude/plugins/config/claude-for-strategy/{plugin}/CLAUDE.md` (org-wide facts go to `org-profile.md`), ask for confirmation, and write only on yes. Only `/{plugin}:practice-setup` auto-applies a full profile write.

"""


def _first_party_skill_paths() -> list[Path]:
    with MARKETPLACE_PATH.open(encoding="utf-8") as handle:
        marketplace = json.load(handle)
    paths: list[Path] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("./"):
            continue
        plugin_dir = REPO_ROOT / source.removeprefix("./")
        paths.extend(sorted(plugin_dir.glob("skills/**/SKILL.md")))
    return paths


def _plugin_name(skill_path: Path) -> str:
    try:
        rel = skill_path.relative_to(REPO_ROOT)
    except ValueError:
        return skill_path.parts[0]
    return rel.parts[0]


def _skill_name(skill_path: Path) -> str:
    return skill_path.parent.name


def add_section(skill_path: Path, dry_run: bool = False) -> bool:
    if _skill_name(skill_path) == "practice-setup":
        return False
    text = skill_path.read_text(encoding="utf-8")
    if "## Propose profile update" in text:
        return False
    plugin = _plugin_name(skill_path)
    section = SECTION_TEMPLATE.format(plugin=plugin)
    match = re.search(r"^## Outputs\s*$", text, re.MULTILINE)
    if not match:
        print(f"skip (no ## Outputs): {skill_path}", file=sys.stderr)
        return False
    updated = text[: match.start()] + section + text[match.start() :]
    if not dry_run:
        skill_path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = 0
    for path in _first_party_skill_paths():
        if add_section(path, dry_run=dry_run):
            changed += 1
            print(path.relative_to(REPO_ROOT))
    print(f"{'would update' if dry_run else 'updated'} {changed} skill(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
