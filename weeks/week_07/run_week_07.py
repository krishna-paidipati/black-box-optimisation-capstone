"""Week 7 analysis runner for the BBO capstone.

Week 7 explicitly tunes Gaussian Process hyperparameters before reporting
acquisition diagnostics. The runner reconstructs all observations that were
available before the Week 7 submission: initial course data plus confirmed
Week 1 through Week 6 queries and outputs.

The hyperparameters tuned are the GP kernel family and ``alpha``. The exact
portal submissions are stored in ``queries.json`` and remain the authoritative
record of what was submitted.
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

from bbo.acquisition import expected_improvement  # noqa: E402
from bbo.candidates import random_candidates  # noqa: E402
from bbo.data import best_observation, load_function_data  # noqa: E402
from gp_hyperparameter_tuning import tune_gp  # noqa: E402

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
    """Load one historical JSON record."""
    if not path.exists():
        raise FileNotFoundError(f"Required file not found: {path}")
    return json.loads(path.read_text())


def parse_query(query: str) -> np.ndarray:
    """Convert a portal query string to a numeric vector."""
    return np.asarray([float(value) for value in query.split("-")], dtype=float)


def build_history(function_id: int) -> tuple[np.ndarray, np.ndarray]:
    """Build initial data plus confirmed Week 1 through Week 6 observations."""
    X, y = load_function_data(DATA_ROOT, function_id)
    key = f"function_{function_id}"

    historical_rounds = [
        ("week_01", "week_02", "week_01_outputs.json"),
        ("week_02", "week_03", "week_02_outputs.json"),
        ("week_03", "week_04", "week_03_outputs.json"),
        ("week_04", "week_05", "week_04_outputs.json"),
        ("week_05", "week_06", "week_05_outputs.json"),
        ("week_06", "week_07", "week_06_outputs.json"),
    ]

    for query_week, output_week, output_file in historical_rounds:
        query = parse_query(
            load_json(ROOT / "weeks" / query_week / "queries.json")[key]
        )
        output = float(
            load_json(ROOT / "weeks" / output_week / output_file)[key]
        )

        if query.size != X.shape[1]:
            raise ValueError(
                f"{key}: query contains {query.size} coordinates; "
                f"expected {X.shape[1]}"
            )

        X = np.vstack([X, query])
        y = np.concatenate([y, [output]])

    return X, y


def analyse_function(function_id: int) -> None:
    """Tune the GP and report the Week 7 acquisition diagnostics."""
    X, y = build_history(function_id)
    best_x, best_y, best_index = best_observation(X, y)

    # Function 1 spans hundreds of orders of magnitude. Log transformation is
    # used only for model fitting so the surrogate can distinguish the narrow
    # non-zero region. The portal objective itself remains unchanged.
    if function_id == 1:
        model_y = np.log10(np.maximum(y, 1e-300))
    else:
        model_y = y

    gp, best_config, all_results = tune_gp(
        X,
        model_y,
        random_state=700 + function_id,
    )

    candidates = random_candidates(
        100_000,
        X.shape[1],
        seed=7000 + function_id,
    )
    mean, std = gp.predict(candidates, return_std=True)

    acquisition = expected_improvement(
        mean,
        std,
        best_y=float(np.max(model_y)),
        xi=0.01 * float(np.std(model_y) + 1e-12),
    )
    top = int(np.argmax(acquisition))

    print(f"\nFunction {function_id}")
    print("-" * 78)
    print(f"Observations available for Week 7: {len(y)}")
    print(f"Best observed objective: {best_y:.12g}")
    print(f"Best observed x: {np.array2string(best_x, precision=6)}")
    print(f"Selected kernel: {best_config.kernel_name}")
    print(f"Selected alpha: {best_config.alpha:g}")
    print(
        "Cross-validated normalised RMSE: "
        f"{best_config.normalised_rmse:.6f}"
    )
    print(f"Fitted kernel: {gp.kernel_}")
    print(
        "Highest global EI diagnostic: "
        f"{np.array2string(candidates[top], precision=6)}"
    )


def print_submitted_queries() -> None:
    """Print and validate the exact Week 7 portal submissions."""
    queries = load_json(WEEK_DIR / "queries.json")

    print("\nAuthoritative Week 7 portal submissions")
    print("=" * 78)

    for function_id in range(1, 9):
        key = f"function_{function_id}"
        query = queries[key]
        parts = query.split("-")

        if len(parts) != EXPECTED_DIMS[key]:
            raise ValueError(
                f"{key}: expected {EXPECTED_DIMS[key]} coordinates, "
                f"received {len(parts)}"
            )

        for part in parts:
            if not part.startswith("0.") or len(part.split(".")[1]) != 6:
                raise ValueError(
                    f"{key}: {part!r} is not valid six-decimal portal format"
                )

        print(f"F{function_id}: {query}")


def main() -> None:
    """Run the complete Week 7 analysis."""
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
