#!/usr/bin/env python3
"""Validate Strategy Builder Hub trust-gated install workflow invariants.

Checks that skill-installer, skills-qa, and auto-updater document the
V20/X5 trust layer: allowlist gate, nine design-parameter QA, injection scan,
raw SKILL.md display, SHA-pinned install log, and watched registries.

Exits 0 when all checks pass; non-zero with one error line per violation.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HUB = REPO_ROOT / "strategy-builder-hub"

INSTALLER = HUB / "skills" / "skill-installer" / "SKILL.md"
SKILLS_QA = HUB / "skills" / "skills-qa" / "SKILL.md"
AUTO_UPDATER = HUB / "skills" / "auto-updater" / "SKILL.md"
REGISTRY_BROWSER = HUB / "skills" / "registry-browser" / "SKILL.md"
INSTALL_LOG_SCHEMA = (
    HUB / "skills" / "skill-installer" / "references" / "install-log-schema.md"
)
ALLOWLIST_SCHEMA = HUB / "skills" / "skill-installer" / "references" / "allowlist.md"
INSTALL_LOG_TEMPLATE = HUB / "references" / "install-log-template.yaml"
REGISTRY_SYNC = HUB / "agents" / "registry-sync.md"


def _read(path: Path) -> str:
    if not path.is_file():
        return ""
    return path.read_text(encoding="utf-8")


def _require(text: str, needle: str, label: str, errors: list[str]) -> None:
    if needle not in text:
        errors.append(f"{label}: missing {needle!r}")


def validate(errors: list[str]) -> None:
    installer = _read(INSTALLER)
    skills_qa = _read(SKILLS_QA)
    auto_updater = _read(AUTO_UPDATER)
    registry_browser = _read(REGISTRY_BROWSER)
    install_log_schema = _read(INSTALL_LOG_SCHEMA)
    allowlist_schema = _read(ALLOWLIST_SCHEMA)
    registry_sync = _read(REGISTRY_SYNC)

    for path in (
        INSTALLER,
        SKILLS_QA,
        AUTO_UPDATER,
        INSTALL_LOG_SCHEMA,
        ALLOWLIST_SCHEMA,
        INSTALL_LOG_TEMPLATE,
        REGISTRY_BROWSER,
        REGISTRY_SYNC,
    ):
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(REPO_ROOT)}")

    # skill-installer trust workflow
    _require(installer, "Step 1: Read the allowlist", "skill-installer", errors)
    _require(installer, "Step 3: Show the RAW SKILL.md", "skill-installer", errors)
    _require(installer, "Step 5: Run skills-qa", "skill-installer", errors)
    _require(installer, "pinned_sha", "skill-installer", errors)
    _require(installer, "install-log-schema.md", "skill-installer", errors)
    _require(installer, "read-only subagent", "skill-installer", errors)

    # skills-qa: nine design parameters + trust surface + injection scan
    for n in range(1, 10):
        _require(skills_qa, f"### {n}.", "skills-qa", errors)
    _require(skills_qa, "### 10. Trust Surface", "skills-qa", errors)
    _require(skills_qa, "Prompt-injection heuristic scan", "skills-qa", errors)
    _require(skills_qa, "nine design-parameter", "skills-qa", errors)

    # auto-updater SHA pinning
    _require(auto_updater, "commit SHA", "auto-updater", errors)
    _require(auto_updater, "install-log", "auto-updater", errors)
    _require(auto_updater, "pinned_sha", "auto-updater", errors)

    # install-log schema
    _require(install_log_schema, "pinned_sha", "install-log-schema", errors)
    _require(install_log_schema, "skills_qa_verdict", "install-log-schema", errors)
    _require(install_log_schema, "Append only", "install-log-schema", errors)

    # allowlist
    _require(allowlist_schema, "restrictive", "allowlist", errors)
    _require(allowlist_schema, "permissive", "allowlist", errors)

    # watched registries
    _require(registry_browser, "watched registries", "registry-browser", errors)
    _require(registry_sync, "watched registries", "registry-sync", errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate and exit (default behaviour)",
    )
    parser.parse_args()

    errors: list[str] = []
    validate(errors)

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        print(f"\n{len(errors)} builder-hub trust violation(s)", file=sys.stderr)
        return 1

    print("builder-hub trust layer: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
