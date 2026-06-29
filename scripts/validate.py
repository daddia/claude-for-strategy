#!/usr/bin/env python3
"""Validate managed-agent worker output against a JSON Schema.

Usage: validate.py <output.json> <schema.json|schema.yaml>
Exits 0 on valid, 1 on invalid (message to stderr), 2 on usage error.

The CMA API does not enforce structured output today, so the deploy harness
runs this between a reader subagent and the orchestrator. Schemas live in each
subagent yaml under `output_schema:` — the deploy script extracts them.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import jsonschema
import yaml


def load_document(path: Path) -> Any:
    text = path.read_text(encoding="utf-8")
    if path.suffix in (".yaml", ".yml"):
        return yaml.safe_load(text)
    return json.loads(text)


def format_path(error: jsonschema.ValidationError) -> str:
    if not error.absolute_path:
        return "/"
    return "/" + "/".join(str(part) for part in error.absolute_path)


def validate_instance(instance: Any, schema: Any) -> jsonschema.ValidationError | None:
    validator_cls = jsonschema.validators.validator_for(schema)
    validator_cls.check_schema(schema)
    validator = validator_cls(schema)
    return next(validator.iter_errors(instance), None)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 2:
        print(__doc__, file=sys.stderr)
        return 2

    instance_path = Path(args[0])
    schema_path = Path(args[1])

    try:
        instance = load_document(instance_path)
        schema = load_document(schema_path)
    except (OSError, json.JSONDecodeError, yaml.YAMLError) as exc:
        print(f"INVALID: could not load input: {exc}", file=sys.stderr)
        return 1

    try:
        error = validate_instance(instance, schema)
    except jsonschema.SchemaError as exc:
        print(f"INVALID: schema error: {exc.message}", file=sys.stderr)
        return 1

    if error is not None:
        message = getattr(error, "message", str(error))
        print(f"INVALID: {message} at {format_path(error)}", file=sys.stderr)
        return 1

    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
