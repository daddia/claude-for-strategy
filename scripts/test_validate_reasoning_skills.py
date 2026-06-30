#!/usr/bin/env python3
"""Unit tests for scripts/validate-reasoning-skills.py."""
from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "validate-reasoning-skills.py"


def _load_module():
    spec = importlib.util.spec_from_file_location("validate_reasoning_skills", SCRIPT_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_reasoning_skills"] = module
    spec.loader.exec_module(module)
    return module


class ValidateReasoningSkillsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.mod = _load_module()

    def test_passing_upgraded_body(self) -> None:
        body = """
## Assumption audit
List load-bearing assumptions.

## Red flags
You MUST NOT proceed without a named decision type — non-negotiable.

## Outside-view step
Compare to reference class.

Do apply a haircut because optimism causes systematic overstatement of benefits.
"""
        failures = self.mod._assertions_for_upgraded("sample", body)
        self.assertEqual(failures, [])

    def test_missing_sections_reported(self) -> None:
        failures = self.mod._assertions_for_upgraded("sample", "# empty")
        self.assertGreaterEqual(len(failures), 4)

    def test_reference_class_requires_flyvbjerg_and_green_book(self) -> None:
        body = """
## Assumption audit
x
## Red flags
MUST NOT skip.
## Outside-view step
Flyvbjerg outside-view.
Green Book optimism-bias uplift.
Do calibrate because bias causes overrun.
"""
        failures = self.mod._assertions_for_reference_class("rcf", body)
        self.assertEqual(failures, [])

    def test_pre_mortem_requires_disconfirm_and_devils_advocate(self) -> None:
        body = """
## Assumption audit
x
## Red flags
do not proceed without scope.
## Outside-view step
base-rate step
Must run devil's advocate because groupthink causes blind spots.
Collect dis-confirming evidence.
"""
        failures = self.mod._assertions_for_pre_mortem("pm", body)
        self.assertEqual(failures, [])

    def test_check_all_passes_on_repo_skills(self) -> None:
        failures = self.mod.check_all()
        self.assertEqual(
            failures,
            [],
            msg="expected repo skills to pass rubric:\n" + "\n".join(failures),
        )


if __name__ == "__main__":
    unittest.main()
