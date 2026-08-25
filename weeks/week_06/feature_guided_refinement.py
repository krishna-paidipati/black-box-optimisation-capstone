"""Feature-guided multi-resolution candidate refinement for Week 6.

The BBO observations are small, tabular datasets, so a CNN is not appropriate.
Instead, Week 6 borrows the *hierarchical refinement* idea: an Extra Trees model
provides a non-linear feature-importance diagnostic, and those importances
control how tightly each dimension is perturbed around strong observed points.

High-importance dimensions receive smaller local steps for fine refinement.
Lower-importance dimensions receive wider steps, preserving exploration.
Candidates are ultimately ranked by Gaussian Process Expected Improvement.
"""

from __future__ import annotations

import numpy as np
from sklearn.ensemble import ExtraTreesRegressor

from bbo.acquisition import expected_improvement


def estimate_feature_importance(
    X: np.ndarray,
    y: np.ndarray,
    *,
    random_state: int = 42,
) -> np.ndarray:
    """Estimate non-linear feature importance using an Extra Trees regressor."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)

    model = ExtraTreesRegressor(
        n_estimators=500,
        min_samples_leaf=2,
        max_features=1.0,
        random_state=random_state,
        n_jobs=-1,
    )
    model.fit(X, y)

    importance = np.asarray(model.feature_importances_, dtype=float)
    total = float(importance.sum())
    if total <= 0.0:
        return np.full(X.shape[1], 1.0 / X.shape[1])
    return importance / total


def feature_guided_candidates(
    gp,
    X: np.ndarray,
    y: np.ndarray,
    *,
    n_elite: int = 5,
    points_per_elite: int = 8_000,
    base_scale: float = 0.08,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Generate local candidates using dimension-specific perturbation scales.

    Returns
    -------
    candidates:
        Candidate matrix sorted from highest Expected Improvement to lowest.
    scores:
        Expected Improvement score for each candidate.
    importance:
        Extra Trees feature-importance vector used to set perturbation scales.
    """
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)

    if X.ndim != 2 or len(X) != len(y):
        raise ValueError("X and y must contain the same number of observations")

    importance = estimate_feature_importance(
        X,
        y,
        random_state=random_state,
    )

    # Important dimensions are refined more finely. Less important dimensions
    # retain wider perturbations so that the search does not collapse too soon.
    normalised = importance / (importance.max() + 1e-12)
    scales = base_scale * (1.35 - 0.85 * normalised)
    scales = np.clip(scales, 0.01, 0.12)

    elite_index = np.argsort(y)[-min(n_elite, len(y)):]
    rng = np.random.default_rng(random_state)

    batches = []
    for index in elite_index:
        noise = rng.normal(
            loc=0.0,
            scale=scales,
            size=(points_per_elite, X.shape[1]),
        )
        batch = np.clip(X[index] + noise, 0.000001, 0.999999)
        batches.append(batch)

    candidates = np.vstack(batches)
    mean, std = gp.predict(candidates, return_std=True)

    scores = expected_improvement(
        mean,
        std,
        best_y=float(np.max(y)),
        xi=0.01,
    )

    order = np.argsort(scores)[::-1]
    return candidates[order], scores[order], importance
