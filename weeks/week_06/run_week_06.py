"""Week 6 analysis runner for the BBO capstone.

This runner reconstructs the data available before the Week 6 submission:
course-provided initial observations plus confirmed Week 1 through Week 5
queries and outputs.

The primary surrogate remains a Gaussian Process. Week 6 adds an Extra Trees
feature-importance diagnostic and a feature-guided multi-resolution candidate
generator. This is inspired by the idea of progressive feature extraction but
does not claim that a CNN is appropriate for the small tabular BBO datasets.

The exact Week 6 portal submissions are stored in ``queries.json`` and printed
as the authoritative historical record.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
WEEK_DIR = Path(__file__).resolve().parent

sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(WEEK_DIR))

from bbo.data import best_observation, load_function_data  # noqa: E402
from bbo.surrogate import fit_gp  # noqa: E402
from feature_guided_refinement import feature_guided_candidates  # noqa: E402

DATA_ROOT = ROOT / "data" / "raw" / "initial_data"

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


def load_json(path: Path) -> dict:
    """Load a JSON historical record."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return json.loads(path.read_text())


def parse_query(query: str) -> np.ndarray:
    """Convert a portal query string into a NumPy vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def build_history(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    """Build initial data plus confirmed Week 1 through Week 5 observations."""
    X, y = load_function_data(DATA_ROOT, function_id)
    key = f"function_{function_id}"

    historical_rounds = [
        ("week_01", "week_02", "week_01_outputs.json"),
        ("week_02", "week_03", "week_02_outputs.json"),
        ("week_03", "week_04", "week_03_outputs.json"),
        ("week_04", "week_05", "week_04_outputs.json"),
        ("week_05", "week_06", "week_05_outputs.json"),
    ]

    for query_week, output_week, output_name in historical_rounds:
        query_path = ROOT / "weeks" / query_week / "queries.json"
        output_path = ROOT / "weeks" / output_week / output_name

        query = parse_query(load_json(query_path)[key])
        output = float(load_json(output_path)[key])

        if query.size != X.shape[1]:
            raise ValueError(
                f"{key}: historical query has {query.size} coordinates; "
                f"expected {X.shape[1]}"
            )

        X = np.vstack([X, query])
        y = np.concatenate([y, [output]])

    return X, y


def analyse_function(function_id: int) -> None:
    """Fit the Week 6 models and print feature-guided search diagnostics."""
    X, y = build_history(function_id)
    best_x, best_y, best_idx = best_observation(X, y)

    gp = fit_gp(X, y)

    candidates, scores, importance = feature_guided_candidates(
        gp,
        X,
        y,
        n_elite=5,
        points_per_elite=4_000,
        base_scale=0.08,
        random_state=600 + function_id,
    )

    print(f"\nFunction {function_id}")
    print("-" * 72)
    print(f"Observations available for Week 6: {len(y)}")
    print(f"Dimensions: {X.shape[1]}")
    print(f"Best observed row: {best_idx}")
    print(f"Best observed y: {best_y:.12g}")
    print(f"Best observed x: {np.array2string(best_x, precision=6)}")
    print(
        "Feature importance:           "
        f"{np.array2string(importance, precision=4)}"
    )
    print(
        "Top feature-guided EI point:  "
        f"{np.array2string(candidates[0], precision=6)}"
    )
    print(f"Top EI score:                 {scores[0]:.6g}")


def print_submitted_queries() -> None:
    """Print the exact Week 6 portal submissions."""
    queries = load_json(WEEK_DIR / "queries.json")

    print("\nAuthoritative Week 6 portal submissions")
    print("=" * 72)

    for function_id in range(1, 9):
        key = f"function_{function_id}"
        query = queries[key]
        expected_dim = EXPECTED_DIMS[key]

        if len(query.split("-")) != expected_dim:
            raise ValueError(
                f"{key}: stored query does not have {expected_dim} coordinates"
            )

        print(f"F{function_id}: {query}")


def main() -> None:
    """Run the complete Week 6 analysis."""
    if not DATA_ROOT.exists():
        raise SystemExit(
            "Initial data not found. Place the course-provided initial_data "
            f"directory at {DATA_ROOT}"
        )

    for function_id in range(1, 9):
        analyse_function(function_id)

    print_submitted_queries()


if __name__ == "__main__":
    main()
