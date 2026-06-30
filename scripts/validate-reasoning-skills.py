#!/usr/bin/env python3
"""Assertion-graded eval rubric for reasoning-tool upgraded skills (V20-02).

Mechanically checks that upgraded high-traffic skills and flagship skills
encode judgment — not just format — per the acceptance criteria in
`.claude/TASKS.md` (V20-02).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

UPGRADED_SKILLS: tuple[tuple[str, Path], ...] = (
    ("business-case", REPO_ROOT / "transformation/skills/business-case/SKILL.md"),
    (
        "map-competitive-landscape",
        REPO_ROOT / "market-intelligence/skills/map-competitive-landscape/SKILL.md",
    ),
    ("roadmap-builder", REPO_ROOT / "transformation/skills/roadmap-builder/SKILL.md"),
    ("benefits-map", REPO_ROOT / "value-realisation/skills/benefits-map/SKILL.md"),
)

FLAGSHIP_SKILLS: tuple[tuple[str, Path], ...] = (
    (
        "reference-class-forecaster",
        REPO_ROOT / "consulting/skills/reference-class-forecaster/SKILL.md",
    ),
    (
        "pre-mortem-and-red-team",
        REPO_ROOT / "consulting/skills/pre-mortem-and-red-team/SKILL.md",
    ),
)

_ASSUMPTION_AUDIT_RE = re.compile(r"^## Assumption audit\b", re.MULTILINE | re.IGNORECASE)
_RED_FLAGS_RE = re.compile(r"^## Red flags\b", re.MULTILINE | re.IGNORECASE)
_OUTSIDE_VIEW_RE = re.compile(
    r"^## (Outside-view|Base-rate)\b|outside-view step|base-rate step",
    re.MULTILINE | re.IGNORECASE,
)
_REASONING_RE = re.compile(
    r"(?:do|must|always)\s+[^.\n]{0,120}\bbecause\b[^.\n]{0,120}\b(?:cause|causes|tends to|leads to)\b",
    re.IGNORECASE,
)
_NON_NEGOTIABLE_RE = re.compile(
    r"\b(?:MUST NOT|do not proceed|non-negotiable|hard stop|halt\b[^.\n]{0,40}before)",
    re.IGNORECASE,
)
_FLYVBJERG_RE = re.compile(r"Flyvbjerg|outside[- ]view", re.IGNORECASE)
_GREEN_BOOK_RE = re.compile(r"Green Book|optimism[- ]bias", re.IGNORECASE)
_DISCONFIRM_RE = re.compile(r"dis-confirming|disconfirming", re.IGNORECASE)
_DEVILS_ADVOCATE_RE = re.compile(r"devil'?s advocate", re.IGNORECASE)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _assertions_for_upgraded(name: str, body: str) -> list[str]:
    failures: list[str] = []
    if not _ASSUMPTION_AUDIT_RE.search(body):
        failures.append(f"{name}: missing ## Assumption audit section")
    if not _RED_FLAGS_RE.search(body):
        failures.append(f"{name}: missing ## Red flags section")
    elif not _NON_NEGOTIABLE_RE.search(body):
        failures.append(f"{name}: Red flags section lacks non-negotiable language")
    if not _REASONING_RE.search(body):
        failures.append(
            f"{name}: missing reasoning instruction (do/must X because Y causes/tends to Z)"
        )
    if not _OUTSIDE_VIEW_RE.search(body):
        failures.append(f"{name}: missing outside-view or base-rate step")
    return failures


def _assertions_for_reference_class(name: str, body: str) -> list[str]:
    failures = _assertions_for_upgraded(name, body)
    if not _FLYVBJERG_RE.search(body):
        failures.append(f"{name}: must reference Flyvbjerg outside-view")
    if not _GREEN_BOOK_RE.search(body):
        failures.append(f"{name}: must reference Green Book optimism-bias calibration")
    return failures


def _assertions_for_pre_mortem(name: str, body: str) -> list[str]:
    failures = _assertions_for_upgraded(name, body)
    if not _DISCONFIRM_RE.search(body):
        failures.append(f"{name}: must require dis-confirming evidence")
    if not _DEVILS_ADVOCATE_RE.search(body):
        failures.append(f"{name}: must require devil's-advocate pass")
    return failures


def check_all() -> list[str]:
    failures: list[str] = []
    for name, path in UPGRADED_SKILLS:
        if not path.is_file():
            failures.append(f"{name}: missing file {path}")
            continue
        failures.extend(_assertions_for_upgraded(name, _read(path)))

    for name, path in FLAGSHIP_SKILLS:
        if not path.is_file():
            failures.append(f"{name}: missing file {path}")
            continue
        body = _read(path)
        if name == "reference-class-forecaster":
            failures.extend(_assertions_for_reference_class(name, body))
        else:
            failures.extend(_assertions_for_pre_mortem(name, body))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate reasoning-tool skill rubric.")
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
        print("reasoning-skill eval FAILED:", file=sys.stderr)
        for message in failures:
            print(f"  {message}", file=sys.stderr)
        return 1

    total = len(UPGRADED_SKILLS) + len(FLAGSHIP_SKILLS)
    print(f"  ✓ {total} reasoning skill(s) pass assertion-graded eval")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
