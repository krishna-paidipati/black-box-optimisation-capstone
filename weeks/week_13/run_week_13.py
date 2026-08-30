"""Validate and summarise the submitted final-round BBO queries."""

from __future__ import annotations

import json
from pathlib import Path

from rl_feedback_diagnostics import build_feedback_signals

HERE = Path(__file__).resolve().parent
EXPECTED_DIMS = {
    "function_1": 2,
    "function_2": 2,
    "function_3": 3,
    "function_4": 4,
    "function_5": 4,
    "function_6": 5,
    "function_7": 6,
    "function_8": 8,
}

WEEK_11_OUTPUTS = {
    "function_1": -0.0021654630322400148,
    "function_2": 0.616348459156891,
    "function_3": -0.008916974174324521,
    "function_4": 0.47244555378051034,
    "function_5": 4440.489438186355,
    "function_6": -0.32254704813855806,
    "function_7": 1.771420983168533,
    "function_8": 9.94601959875,
}


def load_json(name: str):
    with (HERE / name).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def portal_string(values):
    return "-".join(f"{value:.6f}" for value in values)


def validate_queries(queries):
    if set(queries) != set(EXPECTED_DIMS):
        raise ValueError("queries.json must contain function_1 through function_8")

    for function, dimension in EXPECTED_DIMS.items():
        values = queries[function]
        if len(values) != dimension:
            raise ValueError(f"{function}: expected {dimension} dimensions")
        if not all(0.0 <= value <= 1.0 for value in values):
            raise ValueError(f"{function}: all coordinates must lie in [0, 1]")


def main():
    queries = load_json("queries.json")
    week_12 = load_json("week_12_outputs.json")
    validate_queries(queries)

    print("Submitted final-round portal queries")
    for function in EXPECTED_DIMS:
        print(f"{function}: {portal_string(queries[function])}")

    print("\nWeek 11 -> Week 12 feedback used for the final policy")
    for signal in build_feedback_signals(WEEK_11_OUTPUTS, week_12):
        print(
            f"{signal.function}: improvement={signal.improvement:+.12g}; "
            f"policy={signal.policy}"
        )


if __name__ == "__main__":
    main()
