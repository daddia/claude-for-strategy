#!/usr/bin/env python3
"""Set allowed-tools and metadata.permission_tier on first-party SKILL.md files.

Implements the three permission tiers in skill-design-framework.md § Permission
tiers. Run with --check to verify; without --check to rewrite frontmatter.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

ADVISORY_TOOLS = "Read, Grep, Glob"
ARTEFACT_TOOLS = "Read, Grep, Glob, Write"
ARTEFACT_BASH_TOOLS = "Read, Grep, Glob, Write, Bash"
ELEVATED_TOOLS = "Read, Grep, Glob, Write"
ELEVATED_WEBFETCH_TOOLS = "Read, Grep, Glob, Write, WebFetch"

ARTEFACT_SKILL_NAMES = frozenset(
    {
        "practice-setup",
        "decision-log",
        "raid-log",
        "check-in",
        "benefits-tracking",
        "build-strategy-map",
        "tracker-builder",
    }
)
ELEVATED_SKILL_NAMES = frozenset(
    {
        "skill-installer",
        "registry-browser",
        "auto-updater",
        "skill-manager",
        "disable",
        "uninstall",
    }
)
ELEVATED_WEBFETCH_SKILL_NAMES = frozenset({"skill-installer", "registry-browser"})
ARTEFACT_BASH_SKILL_NAMES = frozenset({"tracker-builder"})

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
_ALLOWED_TOOLS_RE = re.compile(r"^allowed-tools:\s*.+$", re.MULTILINE)
_PERMISSION_TIER_RE = re.compile(r"^  permission_tier:\s*.+$", re.MULTILINE)


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


def _skill_name(frontmatter: str) -> str | None:
    match = _NAME_RE.search(frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def _tier_for_name(name: str) -> str:
    if name in ELEVATED_SKILL_NAMES:
        return "elevated"
    if name in ARTEFACT_SKILL_NAMES:
        return "artefact-writer"
    return "advisory"


def _tools_for_tier(name: str, tier: str) -> str:
    if tier == "advisory":
        return ADVISORY_TOOLS
    if tier == "elevated":
        if name in ELEVATED_WEBFETCH_SKILL_NAMES:
            return ELEVATED_WEBFETCH_TOOLS
        return ELEVATED_TOOLS
    if name in ARTEFACT_BASH_SKILL_NAMES:
        return ARTEFACT_BASH_TOOLS
    return ARTEFACT_TOOLS


def _expected_for_path(path: Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing frontmatter")
    name = _skill_name(match.group(1))
    if not name:
        raise ValueError(f"{path}: missing name in frontmatter")
    tier = _tier_for_name(name)
    return tier, _tools_for_tier(name, tier)


def _upsert_frontmatter(frontmatter: str, tier: str, tools: str) -> str:
    if _ALLOWED_TOOLS_RE.search(frontmatter):
        frontmatter = _ALLOWED_TOOLS_RE.sub(f"allowed-tools: {tools}", frontmatter, count=1)
    else:
        frontmatter = frontmatter.rstrip() + f"\nallowed-tools: {tools}\n"

    if _PERMISSION_TIER_RE.search(frontmatter):
        frontmatter = _PERMISSION_TIER_RE.sub(
            f"  permission_tier: {tier}", frontmatter, count=1
        )
    elif "  work_shape:" in frontmatter:
        frontmatter = frontmatter.replace(
            re.search(r"^  work_shape:.*$", frontmatter, re.MULTILINE).group(0),
            f"{re.search(r'^  work_shape:.*$', frontmatter, re.MULTILINE).group(0)}\n  permission_tier: {tier}",
            1,
        )
    else:
        frontmatter = frontmatter.rstrip() + f"\n  permission_tier: {tier}\n"
    return frontmatter


def _parse_tools(value: str) -> frozenset[str]:
    return frozenset(part.strip() for part in value.split(",") if part.strip())


def _apply_path(path: Path, dry_run: bool) -> list[str]:
    rel = path.relative_to(REPO_ROOT)
    text = path.read_text(encoding="utf-8")
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return [f"{rel}: missing frontmatter"]
    tier, tools = _expected_for_path(path)
    frontmatter = match.group(1)
    current_tools = _ALLOWED_TOOLS_RE.search(frontmatter)
    current_tier = _PERMISSION_TIER_RE.search(frontmatter)
    current_tools_val = (
        current_tools.group(0).split(":", 1)[1].strip() if current_tools else None
    )
    current_tier_val = (
        current_tier.group(0).split(":", 1)[1].strip() if current_tier else None
    )
    errs: list[str] = []
    if current_tools_val is None or _parse_tools(current_tools_val) != _parse_tools(tools):
        errs.append(f"{rel}: allowed-tools is {current_tools_val!r}, want {tools!r}")
    if current_tier_val != tier:
        errs.append(f"{rel}: permission_tier is {current_tier_val!r}, want {tier!r}")
    if not errs:
        return []
    if dry_run:
        return errs
    new_frontmatter = _upsert_frontmatter(frontmatter, tier, tools)
    new_text = f"---\n{new_frontmatter}\n---\n{text[match.end() :]}"
    path.write_text(new_text, encoding="utf-8")
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="report drift only; exit 1 on mismatch",
    )
    args = parser.parse_args()
    dry_run = args.check
    paths = _first_party_skill_paths()
    all_errs: list[str] = []
    for path in paths:
        all_errs.extend(_apply_path(path, dry_run=dry_run))
    if all_errs:
        label = "permission tier check FAILED" if dry_run else "permission tier sync FAILED"
        print(label + ":", file=sys.stderr)
        for message in all_errs:
            print(f"  {message}", file=sys.stderr)
        return 1
    verb = "checked" if dry_run else "synced"
    print(f"  ✓ {len(paths)} skill(s) permission tiers {verb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
