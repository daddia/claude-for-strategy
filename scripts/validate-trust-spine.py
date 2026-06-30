#!/usr/bin/env python3
"""Assertion-graded checks for the trust/provenance spine (V20-03).

Validates the canonical trust reference, plugin mirrors, and upgraded
high-traffic skills that must read and apply it before producing output.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_TRUST = REPO_ROOT / "consulting/references/trust-conventions.md"

UPGRADED_SKILLS: tuple[tuple[str, Path], ...] = (
    ("business-case", REPO_ROOT / "transformation/skills/business-case/SKILL.md"),
    (
        "map-competitive-landscape",
        REPO_ROOT / "market-intelligence/skills/map-competitive-landscape/SKILL.md",
    ),
    ("roadmap-builder", REPO_ROOT / "transformation/skills/roadmap-builder/SKILL.md"),
    ("benefits-map", REPO_ROOT / "value-realisation/skills/benefits-map/SKILL.md"),
    (
        "reference-class-forecaster",
        REPO_ROOT / "consulting/skills/reference-class-forecaster/SKILL.md",
    ),
    (
        "pre-mortem-and-red-team",
        REPO_ROOT / "consulting/skills/pre-mortem-and-red-team/SKILL.md",
    ),
)

_TRUST_SECTION_CHECKS: tuple[tuple[str, re.Pattern[str], str], ...] = (
    (
        "source-tagging",
        re.compile(r"Source and provenance tagging|\[sourced:", re.IGNORECASE),
        "must define source-tagging on external claims",
    ),
    (
        "[verify]",
        re.compile(r"\[verify\]", re.IGNORECASE),
        "must define [verify] flags on model-only numbers",
    ),
    (
        "assumptions-surfaced",
        re.compile(r"Assumptions surfaced|LOAD-BEARING ASSUMPTIONS", re.IGNORECASE),
        "must define assumptions surfaced at top of deliverables",
    ),
    (
        "numbers-provenance",
        re.compile(r"Numbers provenance|flag, never invent", re.IGNORECASE),
        "must define numbers provenance rules",
    ),
    (
        "board-ready-gate",
        re.compile(r"Board-ready gate", re.IGNORECASE),
        "must define an explicit board-ready human-review gate",
    ),
)

_WORKFLOW_RE = re.compile(r"^## Workflow\b", re.MULTILINE | re.IGNORECASE)
_READ_APPLY_RE = re.compile(
    r"read and apply\s+`?\.\./\.\./references/trust-conventions\.md`?",
    re.IGNORECASE,
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _workflow_section(body: str) -> str:
    match = _WORKFLOW_RE.search(body)
    if not match:
        return ""
    return body[match.start() :]


def _assertions_for_trust_reference(name: str, body: str) -> list[str]:
    failures: list[str] = []
    for check_name, pattern, message in _TRUST_SECTION_CHECKS:
        if not pattern.search(body):
            failures.append(f"{name}: {message} ({check_name})")
    return failures


def _assertions_for_upgraded_skill(name: str, body: str) -> list[str]:
    failures: list[str] = []
    workflow = _workflow_section(body)
    if not workflow:
        failures.append(f"{name}: missing ## Workflow section")
        return failures
    if not _READ_APPLY_RE.search(workflow):
        failures.append(
            f"{name}: workflow must instruct reading and applying "
            "../../references/trust-conventions.md before producing output"
        )
    return failures


def _sync_check() -> list[str]:
    script = REPO_ROOT / "scripts/sync-references.py"
    result = subprocess.run(
        [sys.executable, str(script), "--check"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return []
    lines = (result.stderr or result.stdout).strip().splitlines()
    return [f"sync-references: {line}" for line in lines if line.strip()]


def check_all() -> list[str]:
    failures: list[str] = []

    if not CANONICAL_TRUST.is_file():
        failures.append(f"missing canonical trust reference: {CANONICAL_TRUST}")
    else:
        failures.extend(
            _assertions_for_trust_reference("trust-conventions.md", _read(CANONICAL_TRUST))
        )

    failures.extend(_sync_check())

    for name, path in UPGRADED_SKILLS:
        if not path.is_file():
            failures.append(f"{name}: missing file {path}")
            continue
        failures.extend(_assertions_for_upgraded_skill(name, _read(path)))

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate trust/provenance spine.")
    parser.add_argument(
        "--check",
        action="store_true",
        help="exit 1 when any assertion fails (default)",
    )
    args = parser.parse_args()
    if not args.check and len(sys.argv) == 1:
        args.check = True

    failures = check_all()
    if failures:
        print("trust-spine eval FAILED:", file=sys.stderr)
        for message in failures:
            print(f"  {message}", file=sys.stderr)
        return 1

    total = len(UPGRADED_SKILLS) + 1
    print(f"  ✓ trust spine passes ({total} checks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
