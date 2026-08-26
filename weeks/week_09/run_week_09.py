"""Week 9 BBO analysis runner.

This runner records the confirmed Week 8 results and adds scaling-aware search
diagnostics. "Scaling" is interpreted as optimisation progress versus the
number of black-box evaluations, not as an unsupported claim about LLM
parameter scaling.

Gaussian Process / Expected Improvement remains the quantitative optimisation
foundation. The exact Week 9 query strings in queries.json are the
authoritative portal submissions.
"""

from __future__ import annotations

import json
from pathlib import Path

from scaling_aware_search import scaling_diagnostics

WEEK = Path(__file__).resolve().parent

DIMS = {
    "function_1": 2, "function_2": 2, "function_3": 3, "function_4": 4,
    "function_5": 4, "function_6": 5, "function_7": 6, "function_8": 8,
}


def validate_query(query: str, expected_dim: int) -> None:
    """Validate portal query dimensionality and six-decimal formatting."""
    parts = query.split("-")
    if len(parts) != expected_dim:
        raise ValueError(f"Expected {expected_dim} coordinates, got {len(parts)}")
    for value in parts:
        if not value.startswith("0.") or len(value.split(".")[-1]) != 6:
            raise ValueError(f"Invalid portal coordinate: {value}")
        number = float(value)
        if not 0.0 <= number < 1.0:
            raise ValueError(f"Coordinate outside [0,1): {value}")


def main() -> None:
    """Validate the Week 9 historical record."""
    outputs = json.loads((WEEK / "week_08_outputs.json").read_text())
    queries = json.loads((WEEK / "queries.json").read_text())

    print("Confirmed Week 8 outputs and Week 9 submissions")
    print("=" * 72)

    for key, dim in DIMS.items():
        validate_query(queries[key], dim)
        print(f"{key}: Week 8 y={outputs[key]:.12g}")
        print(f"  Week 9 query={queries[key]}")

    print(
        "\nFor full scaling diagnostics, combine these outputs with the "
        "historical objective sequence and call scaling_diagnostics(y)."
    )


if __name__ == "__main__":
    main()
