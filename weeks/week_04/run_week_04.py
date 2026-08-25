"""Week 4 analysis runner for the BBO capstone.

This entry point reconstructs every observation available before the Week 4
submission, then fits:

1. the Gaussian Process surrogate used as the primary uncertainty-aware model;
2. the compact PyTorch neural ensemble introduced in Week 4; and
3. neural input gradients at the current best observed point.

The exact Week 4 portal submissions remain stored in ``queries.json`` and are
printed as the authoritative historical record. The hidden black-box functions
are never evaluated locally.
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

from bbo.acquisition import expected_improvement, upper_confidence_bound  # noqa: E402
from bbo.candidates import random_candidates  # noqa: E402
from bbo.data import best_observation, load_function_data  # noqa: E402
from bbo.surrogate import fit_gp  # noqa: E402
from neural_surrogate import (  # noqa: E402
    fit_neural_ensemble,
    mean_input_gradient,
    predict_ensemble,
)

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
    """Load a JSON file and fail clearly if the historical record is missing."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return json.loads(path.read_text())


def parse_query(query: str) -> np.ndarray:
    """Convert the portal's hyphen-delimited query into a numeric vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def build_history(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    """Build initial data + confirmed Week 1, Week 2 and Week 3 observations."""
    X, y = load_function_data(DATA_ROOT, function_id)
    key = f"function_{function_id}"

    historical_rounds = [
        (
            ROOT / "weeks" / "week_01" / "queries.json",
            ROOT / "weeks" / "week_02" / "week_01_outputs.json",
        ),
        (
            ROOT / "weeks" / "week_02" / "queries.json",
            ROOT / "weeks" / "week_03" / "week_02_outputs.json",
        ),
        (
            ROOT / "weeks" / "week_03" / "queries.json",
            ROOT / "weeks" / "week_04" / "week_03_outputs.json",
        ),
    ]

    for query_path, output_path in historical_rounds:
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


def analyse_function(function_id: int, n_candidates: int = 25_000) -> None:
    """Print GP and neural-surrogate diagnostics for one function."""
    X, y = build_history(function_id)
    best_x, best_y, best_idx = best_observation(X, y)

    gp = fit_gp(X, y)
    candidates = random_candidates(
        n_candidates,
        X.shape[1],
        seed=400 + function_id,
    )
    gp_mean, gp_std = gp.predict(candidates, return_std=True)

    ei = expected_improvement(
        gp_mean,
        gp_std,
        best_y=best_y,
        xi=0.01,
    )
    ucb = upper_confidence_bound(gp_mean, gp_std, kappa=1.96)

    ensemble = fit_neural_ensemble(X, y)
    nn_mean, nn_disagreement = predict_ensemble(ensemble, candidates)
    gradient_mean, gradient_std = mean_input_gradient(ensemble, best_x)

    ei_idx = int(np.argmax(ei))
    ucb_idx = int(np.argmax(ucb))
    nn_idx = int(np.argmax(nn_mean))

    print(f"\nFunction {function_id}")
    print("-" * 72)
    print(f"Observations available for Week 4: {len(y)}")
    print(f"Dimensions: {X.shape[1]}")
    print(f"Best observed row: {best_idx}")
    print(f"Best observed y: {best_y:.12g}")
    print(f"Best observed x: {np.array2string(best_x, precision=6)}")
    print(
        "Top GP Expected Improvement: "
        f"{np.array2string(candidates[ei_idx], precision=6)}"
    )
    print(
        "Top GP UCB:                  "
        f"{np.array2string(candidates[ucb_idx], precision=6)}"
    )
    print(
        "Top neural mean:             "
        f"{np.array2string(candidates[nn_idx], precision=6)}"
    )
    print(
        "Neural disagreement there:   "
        f"{nn_disagreement[nn_idx]:.6g}"
    )
    print(
        "Mean gradient at best x:     "
        f"{np.array2string(gradient_mean, precision=6)}"
    )
    print(
        "Gradient disagreement:       "
        f"{np.array2string(gradient_std, precision=6)}"
    )


def print_submitted_queries() -> None:
    """Print the exact Week 4 portal queries stored in the repository."""
    queries = load_json(WEEK_DIR / "queries.json")

    print("\nAuthoritative Week 4 portal submissions")
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
    """Run the complete Week 4 diagnostic workflow."""
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
