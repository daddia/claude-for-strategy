#!/usr/bin/env python3
"""Unit tests for submission validation helpers."""

from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent


def _load_script_module(module_name: str, filename: str):
    path = SCRIPTS_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


validate_submission = _load_script_module(
    "validate_submission", "validate-submission.py"
)
check_marketplace_sync = _load_script_module(
    "check_marketplace_sync", "check-marketplace-sync.py"
)

check_sync = check_marketplace_sync.check_sync
check_skill_submission_constraints = (
    validate_submission.check_skill_submission_constraints
)
_parse_description = validate_submission._parse_description
DESCRIPTION_MAX_LEN = validate_submission.DESCRIPTION_MAX_LEN


class ParseDescriptionTests(unittest.TestCase):
    def test_block_scalar(self) -> None:
        raw = (
            "name: demo\n"
            "description: >\n"
            "  Reference: helper workflows loaded by other skills.\n"
            "  Second line.\n"
            "allowed-tools: Read\n"
        )
        self.assertEqual(
            _parse_description(raw),
            "Reference: helper workflows loaded by other skills. Second line.",
        )

    def test_inline_scalar(self) -> None:
        raw = 'name: demo\ndescription: Short inline description.\n'
        self.assertEqual(_parse_description(raw), "Short inline description.")


class SkillSubmissionConstraintTests(unittest.TestCase):
    def _write_skill(self, directory: Path, body: str) -> Path:
        path = directory / "SKILL.md"
        path.write_text(body, encoding="utf-8")
        return path

    def test_missing_description_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_skill(
                Path(tmp),
                "---\nname: demo\n---\n\n# Demo\n",
            )
            errs = check_skill_submission_constraints(path)
            self.assertTrue(any("missing description" in err for err in errs))

    def test_long_description_fails(self) -> None:
        long_text = "x" * DESCRIPTION_MAX_LEN
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_skill(
                Path(tmp),
                f"---\nname: demo\ndescription: {long_text}\n---\n\n# Demo\n",
            )
            errs = check_skill_submission_constraints(path)
            self.assertTrue(any("description length" in err for err in errs))

    def test_reference_skill_requires_user_invocable_false(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_skill(
                Path(tmp),
                (
                    "---\n"
                    "name: helper\n"
                    "description: Reference: loaded by parent skill.\n"
                    "---\n\n# Helper\n"
                ),
            )
            errs = check_skill_submission_constraints(path)
            self.assertTrue(any("user-invocable: false" in err for err in errs))

    def test_reference_skill_with_flag_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_skill(
                Path(tmp),
                (
                    "---\n"
                    "name: helper\n"
                    "description: Reference: loaded by parent skill.\n"
                    "user-invocable: false\n"
                    "---\n\n# Helper\n"
                ),
            )
            self.assertEqual(check_skill_submission_constraints(path), [])

    def test_user_facing_skill_without_flag_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self._write_skill(
                Path(tmp),
                (
                    "---\n"
                    "name: demo\n"
                    "description: This skill should be used when the user asks.\n"
                    "---\n\n# Demo\n"
                ),
            )
            self.assertEqual(check_skill_submission_constraints(path), [])


class MarketplaceSyncTests(unittest.TestCase):
    def test_detects_description_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            marketplace_dir = root / ".claude-plugin"
            marketplace_dir.mkdir()
            plugin_dir = root / "demo-plugin" / ".claude-plugin"
            plugin_dir.mkdir(parents=True)

            marketplace = {
                "plugins": [
                    {
                        "name": "demo-plugin",
                        "source": "./demo-plugin",
                        "description": "Marketplace copy",
                        "author": {"name": "Author", "url": "https://example.com"},
                    }
                ]
            }
            plugin_manifest = {
                "name": "demo-plugin",
                "description": "Plugin copy",
                "author": {"name": "Author", "url": "https://example.com"},
            }

            marketplace_path = marketplace_dir / "marketplace.json"
            marketplace_path.write_text(
                json.dumps(marketplace), encoding="utf-8"
            )
            (plugin_dir / "plugin.json").write_text(
                json.dumps(plugin_manifest), encoding="utf-8"
            )

            original_root = check_marketplace_sync.REPO_ROOT
            original_path = check_marketplace_sync.MARKETPLACE_PATH
            try:
                check_marketplace_sync.REPO_ROOT = root
                check_marketplace_sync.MARKETPLACE_PATH = marketplace_path
                errs = check_sync()
            finally:
                check_marketplace_sync.REPO_ROOT = original_root
                check_marketplace_sync.MARKETPLACE_PATH = original_path

            self.assertTrue(any("description mismatch" in err for err in errs))


if __name__ == "__main__":
    raise SystemExit(unittest.main())
