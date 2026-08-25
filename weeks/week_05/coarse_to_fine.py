"""Coarse-to-fine candidate refinement used in Week 5.

The procedure uses an already-fitted Gaussian Process. It first ranks a broad
candidate population and then samples locally around the best coarse
candidates. This is intentionally lightweight because the capstone data remain
small.
"""

from __future__ import annotations

import numpy as np

from bbo.acquisition import expected_improvement


def coarse_to_fine_candidates(
    gp,
    observed_y: np.ndarray,
    *,
    n_dims: int,
    n_coarse: int = 100_000,
    n_elite: int = 20,
    local_per_elite: int = 2_000,
    local_scale: float = 0.04,
    random_state: int = 42,
) -> tuple[np.ndarray, np.ndarray]:
    """Generate and score candidates in two stages.

    Returns
    -------
    candidates:
        Refined candidate matrix in the unit hypercube.
    scores:
        Expected-improvement score for each refined candidate.
    """
    rng = np.random.default_rng(random_state)

    coarse = rng.uniform(0.0, 1.0, size=(n_coarse, n_dims))
    coarse_mean, coarse_std = gp.predict(coarse, return_std=True)
    coarse_score = expected_improvement(
        coarse_mean,
        coarse_std,
        best=float(np.max(observed_y)),
    )

    elite_index = np.argsort(coarse_score)[-n_elite:]
    elite = coarse[elite_index]

    local = []
    for centre in elite:
        points = centre + rng.normal(
            loc=0.0,
            scale=local_scale,
            size=(local_per_elite, n_dims),
        )
        local.append(np.clip(points, 0.000001, 0.999999))

    refined = np.vstack([elite, *local])
    mean, std = gp.predict(refined, return_std=True)
    score = expected_improvement(
        mean,
        std,
        best=float(np.max(observed_y)),
    )

    order = np.argsort(score)[::-1]
    return refined[order], score[order]
