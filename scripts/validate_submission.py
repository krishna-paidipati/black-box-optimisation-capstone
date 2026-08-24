"""Validate a weekly JSON query file against the capstone portal format."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from bbo.formatting import validate_query_string  # noqa: E402


DIMENSIONS = {
    "function_1": 2,
    "function_2": 2,
    "function_3": 3,
    "function_4": 4,
    "function_5": 4,
    "function_6": 5,
    "function_7": 6,
    "function_8": 8,
}


def main(path: str) -> None:
    data = json.loads(Path(path).read_text())
    failures = []

    for name, dims in DIMENSIONS.items():
        query = data["queries"].get(name, "")
        if not validate_query_string(query, dims):
            failures.append(f"{name}: invalid query {query!r}; expected {dims} coordinates")

    if failures:
        raise SystemExit("\n".join(failures))

    print("All eight queries have valid six-decimal portal formatting.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/validate_submission.py <queries.json>")
    main(sys.argv[1])
