"""Data loading and observation-summary utilities for the BBO capstone."""

from pathlib import Path
from typing import Tuple

import numpy as np


def load_function_data(data_root: Path, function_id: int) -> Tuple[np.ndarray, np.ndarray]:
    """Load input and output arrays for one black-box function.

    Parameters
    ----------
    data_root:
        Path to the directory containing ``function_1`` ... ``function_8``.
    function_id:
        Integer function identifier from 1 to 8.

    Returns
    -------
    X, y:
        Input matrix with shape ``(n_samples, n_dimensions)`` and output
        vector with shape ``(n_samples,)``.
    """
    folder = Path(data_root) / f"function_{function_id}"
    X = np.load(folder / "initial_inputs.npy")
    y = np.load(folder / "initial_outputs.npy").reshape(-1)
    return X, y


def best_observation(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, float, int]:
    """Return the best observed input, objective value, and row index."""
    idx = int(np.argmax(y))
    return X[idx].copy(), float(y[idx]), idx
