#!/usr/bin/env python3
"""Keep consulting plugin references in sync with repo-root mirrors and plugin copies."""

from __future__ import annotations

import argparse
import filecmp
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_DIR = REPO_ROOT / "consulting" / "references"
MIRROR_DIR = REPO_ROOT / "references"

REFERENCE_FILES = (
    "minto-pyramid.md",
    "hypothesis-driven-approach.md",
    "bluf-conventions.md",
    "mece.md",
    "trust-conventions.md",
    "practice-setup-framework.md",
    "org-profile-template.md",
)

FIRST_PARTY_PLUGINS = (
    "consulting",
    "corporate-strategy",
    "market-intelligence",
    "transformation",
    "change-management",
    "operating-model",
    "performance",
    "balanced-scorecard",
    "okr",
    "pmo",
    "value-realisation",
)

SHARED_PLUGIN_REFERENCES = (
    "practice-setup-framework.md",
    "org-profile-template.md",
)


def _missing_paths() -> list[Path]:
    missing: list[Path] = []
    for name in REFERENCE_FILES:
        for directory in (CANONICAL_DIR, MIRROR_DIR):
            path = directory / name
            if not path.is_file():
                missing.append(path)
    return missing


def _sync(direction: str) -> None:
    src_dir = CANONICAL_DIR if direction == "to-mirror" else MIRROR_DIR
    dst_dir = MIRROR_DIR if direction == "to-mirror" else CANONICAL_DIR
    for name in REFERENCE_FILES:
        shutil.copy2(src_dir / name, dst_dir / name)


def _sync_plugin_copies() -> None:
    for plugin in FIRST_PARTY_PLUGINS:
        if plugin == "consulting":
            continue
        plugin_refs = REPO_ROOT / plugin / "references"
        plugin_refs.mkdir(parents=True, exist_ok=True)
        for name in SHARED_PLUGIN_REFERENCES:
            shutil.copy2(CANONICAL_DIR / name, plugin_refs / name)


def _check() -> bool:
    ok = True
    for name in REFERENCE_FILES:
        canonical = CANONICAL_DIR / name
        mirror = MIRROR_DIR / name
        if not filecmp.cmp(canonical, mirror, shallow=False):
            print(f"out of sync: {canonical} != {mirror}", file=sys.stderr)
            ok = False
    for plugin in FIRST_PARTY_PLUGINS:
        if plugin == "consulting":
            continue
        for name in SHARED_PLUGIN_REFERENCES:
            canonical = CANONICAL_DIR / name
            plugin_copy = REPO_ROOT / plugin / "references" / name
            if not plugin_copy.is_file():
                print(f"missing plugin copy: {plugin_copy}", file=sys.stderr)
                ok = False
            elif not filecmp.cmp(canonical, plugin_copy, shallow=False):
                print(f"out of sync: {canonical} != {plugin_copy}", file=sys.stderr)
                ok = False
    return ok


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Sync consulting/references/ (plugin payload) with repo-root "
            "references/ (contributor mirror) and shared refs across plugins."
        )
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 if canonical, mirror, or plugin copies differ",
    )
    parser.add_argument(
        "--from-mirror",
        action="store_true",
        help="copy repo-root references/ into consulting/references/",
    )
    args = parser.parse_args()

    missing = _missing_paths()
    if missing:
        for path in missing:
            print(f"missing: {path}", file=sys.stderr)
        return 1

    if args.check:
        return 0 if _check() else 1

    direction = "from-mirror" if args.from_mirror else "to-mirror"
    _sync(direction)
    _sync_plugin_copies()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
