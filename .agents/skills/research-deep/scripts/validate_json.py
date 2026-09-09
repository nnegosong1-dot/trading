#!/usr/bin/env python3
"""Lightweight schema coverage validator for Shen Heng research JSON.

Usage: python validate_json.py -f fields.yaml -j result.json
The validator checks that every field declared in fields.yaml exists somewhere
in the JSON. It intentionally does not reject additional fields.
"""
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


def flatten_fields(obj):
    out = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key in {"uncertain", "execution", "topic", "items"}:
                continue
            if isinstance(value, dict):
                if "description" in value or "detail_level" in value:
                    out.append(key)
                else:
                    out.extend(flatten_fields(value))
            elif isinstance(value, list):
                if value and all(isinstance(x, dict) for x in value):
                    for x in value:
                        out.extend(flatten_fields(x))
                else:
                    out.append(key)
    elif isinstance(obj, list):
        for x in obj:
            out.extend(flatten_fields(x))
    return out


def keyset(obj):
    keys = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            keys.add(k)
            keys |= keyset(v)
    elif isinstance(obj, list):
        for x in obj:
            keys |= keyset(x)
    return keys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--fields", required=True)
    ap.add_argument("-j", "--json", required=True)
    args = ap.parse_args()

    fields = yaml.safe_load(Path(args.fields).read_text(encoding="utf-8")) or {}
    data = json.loads(Path(args.json).read_text(encoding="utf-8"))
    required = set(flatten_fields(fields.get("fields", fields)))
    actual = keyset(data)
    missing = sorted(required - actual)

    if missing:
        print("VALIDATION FAILED")
        for x in missing:
            print(f"- missing: {x}")
        raise SystemExit(1)

    print(f"VALIDATION PASSED: {args.json}")


if __name__ == "__main__":
    main()
