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


def normalise_query(value):
    """Convert a stored query into the six-decimal portal string format."""
    if isinstance(value, str):
        return value

    if isinstance(value, list):
        return "-".join(f"{float(x):.6f}" for x in value)

    raise TypeError(f"Unsupported query representation: {type(value).__name__}")


def main(path: str) -> None:
    data = json.loads(Path(path).read_text(encoding="utf-8"))

    # Historical files may store queries under a top-level "queries" key,
    # while later rounds may store the function mapping directly.
    queries = data.get("queries", data)

    failures = []

    for name, dims in DIMENSIONS.items():
        if name not in queries:
            failures.append(f"{name}: missing query")
            continue

        try:
            query = normalise_query(queries[name])
        except (TypeError, ValueError) as exc:
            failures.append(f"{name}: {exc}")
            continue

        if not validate_query_string(query, dims):
            failures.append(
                f"{name}: invalid query {query!r}; "
                f"expected {dims} six-decimal coordinates"
            )

    if failures:
        raise SystemExit("\n".join(failures))

    print("All eight queries have valid six-decimal portal formatting.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage: python scripts/validate_submission.py <queries.json>"
        )

    main(sys.argv[1])
