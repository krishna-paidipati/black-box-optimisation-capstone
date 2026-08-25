"""Week 2 analysis for the Stage 2 BBO capstone.

This script reconstructs the information that was available before the Week 2
submission:

1. course-provided initial observations;
2. the eight Week 1 submitted query points; and
3. the eight Week 1 returned objective values.

It then refits the Gaussian Process surrogate for each function and prints
Expected Improvement, UCB, and maximin-exploration diagnostics.  The exact
Week 2 portal queries are loaded from ``queries.json`` and printed separately
as the authoritative historical record of what was actually submitted.

The diagnostic models do not evaluate the hidden black-box functions locally.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from bbo.acquisition import expected_improvement, upper_confidence_bound  # noqa: E402
from bbo.candidates import min_distance_to_observations, random_candidates  # noqa: E402
from bbo.data import best_observation, load_function_data  # noqa: E402
from bbo.surrogate import fit_gp  # noqa: E402

DATA_ROOT = ROOT / "data" / "raw" / "initial_data"
WEEK_01_DIR = ROOT / "weeks" / "week_01"
WEEK_02_DIR = Path(__file__).resolve().parent

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


def parse_query(query: str) -> np.ndarray:
    """Convert the portal query format into a floating-point vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def load_json(path: Path) -> dict:
    """Load a JSON file with a clear error if it is missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return json.loads(path.read_text())


def build_week_2_dataset(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    """Return initial observations plus the confirmed Week 1 observation."""
    X_initial, y_initial = load_function_data(DATA_ROOT, function_id)

    week_1_queries = load_json(WEEK_01_DIR / "queries.json")
    week_1_outputs = load_json(WEEK_02_DIR / "week_01_outputs.json")

    key = f"function_{function_id}"
    x_week_1 = parse_query(week_1_queries[key])
    y_week_1 = float(week_1_outputs[key])

    if x_week_1.size != X_initial.shape[1]:
        raise ValueError(
            f"{key}: Week 1 query has {x_week_1.size} coordinates, "
            f"expected {X_initial.shape[1]}"
        )

    X = np.vstack([X_initial, x_week_1])
    y = np.concatenate([y_initial, [y_week_1]])
    return X, y


def analyse_function(function_id: int, n_candidates: int = 100_000) -> None:
    """Print Week 2 surrogate diagnostics for one black-box function."""
    X, y = build_week_2_dataset(function_id)
    best_x, best_y, best_idx = best_observation(X, y)

    gp = fit_gp(X, y)

    candidates = random_candidates(
        n_candidates,
        X.shape[1],
        seed=200 + function_id,
    )
    mean, std = gp.predict(candidates, return_std=True)

    ei = expected_improvement(
        mean,
        std,
        best_y=best_y,
        xi=0.01,
    )
    ucb = upper_confidence_bound(
        mean,
        std,
        kappa=1.96,
    )
    nearest = min_distance_to_observations(candidates, X)

    ei_idx = int(np.argmax(ei))
    ucb_idx = int(np.argmax(ucb))
    explore_idx = int(np.argmax(nearest))

    print(f"\nFunction {function_id}")
    print("-" * 62)
    print(f"Observations available for Week 2: {len(y)}")
    print(f"Dimensions: {X.shape[1]}")
    print(f"Best observed row: {best_idx}")
    print(f"Best observed y: {best_y:.12g}")
    print(f"Best observed x: {np.array2string(best_x, precision=6)}")
    print(
        "Top EI diagnostic:      "
        f"{np.array2string(candidates[ei_idx], precision=6)}"
    )
    print(
        "Top UCB diagnostic:     "
        f"{np.array2string(candidates[ucb_idx], precision=6)}"
    )
    print(
        "Maximin diagnostic:     "
        f"{np.array2string(candidates[explore_idx], precision=6)}"
    )


def print_submitted_week_2_queries() -> None:
    """Print the exact historical Week 2 queries stored in the repository."""
    queries = load_json(WEEK_02_DIR / "queries.json")

    print("\nAuthoritative Week 2 portal submissions")
    print("=" * 62)
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
    """Run the complete Week 2 diagnostic workflow."""
    if not DATA_ROOT.exists():
        raise SystemExit(
            "Initial data not found. Place the course-provided initial_data "
            f"directory at {DATA_ROOT}"
        )

    for function_id in range(1, 9):
        analyse_function(function_id)

    print_submitted_week_2_queries()


if __name__ == "__main__":
    main()
