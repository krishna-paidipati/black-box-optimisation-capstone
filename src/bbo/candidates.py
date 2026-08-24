"""Candidate generation and diversity checks for weekly BBO queries."""

from __future__ import annotations

import numpy as np
from scipy.spatial.distance import cdist


def random_candidates(n_candidates: int, n_dims: int, seed: int = 42) -> np.ndarray:
    """Draw reproducible candidates uniformly from the unit hypercube."""
    rng = np.random.default_rng(seed)
    return rng.uniform(0.0, 1.0, size=(n_candidates, n_dims))


def min_distance_to_observations(candidates: np.ndarray, X_observed: np.ndarray) -> np.ndarray:
    """Return each candidate's Euclidean distance to its nearest observation."""
    return cdist(candidates, X_observed).min(axis=1)
