#!/usr/bin/env python3
"""Unit tests for scripts/validate-trust-spine.py."""
from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "validate-trust-spine.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("validate_trust_spine", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_trust_spine"] = module
    spec.loader.exec_module(module)
    return module


class ValidateTrustSpineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mod = _load_module()

    def test_passing_trust_reference(self) -> None:
        body = """
## 1. Source and provenance tagging
[sourced: example]
[verify] on model-only numbers.

## 2. Assumptions surfaced
LOAD-BEARING ASSUMPTIONS:

## 3. Numbers provenance — flag, never invent

## 5. Board-ready gate
"""
        failures = self.mod._assertions_for_trust_reference("trust-conventions.md", body)
        self.assertEqual(failures, [])

    def test_missing_sections_reported(self) -> None:
        failures = self.mod._assertions_for_trust_reference("trust-conventions.md", "# empty")
        self.assertGreaterEqual(len(failures), 5)

    def test_passing_upgraded_workflow(self) -> None:
        body = """
## Workflow

**Before step 1:** Read and apply `../../references/trust-conventions.md` — apply gates.

1. Do work.
"""
        failures = self.mod._assertions_for_upgraded_skill("sample", body)
        self.assertEqual(failures, [])

    def test_missing_read_apply_reported(self) -> None:
        body = """
## Workflow

1. Do work without reading trust reference.
"""
        failures = self.mod._assertions_for_upgraded_skill("sample", body)
        self.assertEqual(len(failures), 1)

    def test_check_all_passes_on_repo(self) -> None:
        failures = self.mod.check_all()
        self.assertEqual(
            failures,
            [],
            msg="expected repo to pass trust-spine rubric:\n" + "\n".join(failures),
        )


if __name__ == "__main__":
    unittest.main()
