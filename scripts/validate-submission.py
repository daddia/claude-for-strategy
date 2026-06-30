#!/usr/bin/env python3
"""Pre-submission checks for the claude-for-strategy plugin marketplace.

Encodes directory-submission constraints that ``claude plugin validate`` does
not enforce on its own:

  - every first-party skill ``description`` is present and under 1024 characters
  - pure-reference skills (description begins with ``Reference:``) set
    ``user-invocable: false``

With ``--with-cli``, also runs ``claude plugin validate`` on the marketplace
manifest and each first-party plugin directory.

Exits 0 when all checks pass, 1 on violation, 2 on usage or tooling error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

DESCRIPTION_MAX_LEN = 1024

_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_FRONTMATTER_KEY_RE = re.compile(r"^(\s*)([A-Za-z0-9_-]+):\s*(.*)$")
_REFERENCE_PREFIX_RE = re.compile(r"^reference:\s*", re.IGNORECASE)


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _strip_scalar(value: str) -> str | None:
    value = value.strip()
    if not value or value in {"|", ">"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def _parse_description(raw_frontmatter: str) -> str | None:
    """Return the flattened description string, or None when absent."""
    lines = raw_frontmatter.splitlines()
    i = 0
    while i < len(lines):
        match = _FRONTMATTER_KEY_RE.match(lines[i])
        if not match or match.group(1):
            i += 1
            continue
        key, rest = match.group(2), match.group(3).strip()
        if key != "description":
            i += 1
            continue

        scalar = _strip_scalar(rest)
        if scalar is not None:
            return scalar

        if rest in {">", "|"}:
            block: list[str] = []
            i += 1
            while i < len(lines):
                line = lines[i]
                if line and not line[0].isspace():
                    break
                block.append(line.strip())
                i += 1
            return " ".join(part for part in block if part)

        return rest or None

    return None


def _parse_frontmatter_bool(raw_frontmatter: str, key: str) -> bool | None:
    for line in raw_frontmatter.splitlines():
        match = _FRONTMATTER_KEY_RE.match(line)
        if not match or match.group(1):
            continue
        if match.group(2) != key:
            continue
        scalar = _strip_scalar(match.group(3))
        if scalar is None:
            return None
        lowered = scalar.lower()
        if lowered in {"false", "no", "0"}:
            return False
        if lowered in {"true", "yes", "1"}:
            return True
        return None
    return None


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


def _first_party_plugin_dirs() -> list[Path]:
    with MARKETPLACE_PATH.open(encoding="utf-8") as handle:
        marketplace = json.load(handle)
    dirs: list[Path] = []
    for entry in marketplace.get("plugins", []):
        source = entry.get("source")
        if not isinstance(source, str) or not source.startswith("./"):
            continue
        dirs.append(REPO_ROOT / source.removeprefix("./"))
    return dirs


def check_skill_submission_constraints(path: Path) -> list[str]:
    rel = _display_path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"{rel}: cannot read file: {exc}"]

    match = _FRONTMATTER_RE.match(text)
    if not match:
        return [f"{rel}: missing YAML frontmatter delimiters (---)"]

    raw_frontmatter = match.group(1)
    description = _parse_description(raw_frontmatter)
    errs: list[str] = []

    if description is None or not description.strip():
        errs.append(f"{rel}: missing description")
    elif len(description) >= DESCRIPTION_MAX_LEN:
        errs.append(
            f"{rel}: description length {len(description)} "
            f"(must be < {DESCRIPTION_MAX_LEN})"
        )
    elif _REFERENCE_PREFIX_RE.match(description):
        invocable = _parse_frontmatter_bool(raw_frontmatter, "user-invocable")
        if invocable is not False:
            errs.append(
                f"{rel}: pure-reference skill must set user-invocable: false"
            )

    return errs


def check_skills(paths: list[Path] | None = None) -> list[str]:
    skill_paths = paths if paths is not None else _first_party_skill_paths()
    errs: list[str] = []
    for path in skill_paths:
        errs.extend(check_skill_submission_constraints(path))
    return errs


def run_cli_validate(target: Path) -> tuple[int, str]:
    result = subprocess.run(
        ["claude", "plugin", "validate", str(target)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode, output.strip()


def run_marketplace_sync_check() -> int:
    script = REPO_ROOT / "scripts" / "check-marketplace-sync.py"
    return subprocess.run(
        [sys.executable, str(script), "--check"],
        cwd=REPO_ROOT,
    ).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--with-cli",
        action="store_true",
        help="also run claude plugin validate on marketplace and each plugin",
    )
    parser.add_argument(
        "files",
        nargs="*",
        help="specific SKILL.md paths to check (default: all first-party skills)",
    )
    args = parser.parse_args()

    errs: list[str] = []

    if args.files:
        skill_paths = [Path(p).resolve() for p in args.files]
    else:
        skill_paths = _first_party_skill_paths()

    if not skill_paths:
        print("no SKILL.md files found to check", file=sys.stderr)
        return 2

    errs.extend(check_skills(skill_paths))

    if run_marketplace_sync_check() != 0:
        return 1

    if args.with_cli:
        cli_targets = [MARKETPLACE_PATH, *_first_party_plugin_dirs()]
        for target in cli_targets:
            code, output = run_cli_validate(target)
            if code != 0:
                label = _display_path(target)
                detail = output or f"claude plugin validate exited {code}"
                errs.append(f"{label}: {detail}")

    if errs:
        print("submission validation FAILED:", file=sys.stderr)
        for message in errs:
            print(f"  {message}", file=sys.stderr)
        return 1

    print(f"  ✓ {len(skill_paths)} skill(s) meet submission constraints")
    if args.with_cli:
        print("  ✓ claude plugin validate passed for marketplace and plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
