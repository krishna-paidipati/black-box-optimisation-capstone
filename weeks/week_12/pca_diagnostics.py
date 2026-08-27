"""PCA diagnostics for Week 12.

PCA is interpretive only. It summarises variance and redundancy in the observed
input distribution and does not replace the objective-aware optimiser.
"""

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def fit_pca_summary(X, y):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    Z = StandardScaler().fit_transform(X)
    pca = PCA().fit(Z)

    cumulative = np.cumsum(pca.explained_variance_ratio_)
    n90 = int(np.searchsorted(cumulative, 0.90) + 1)

    correlations = []
    for j in range(X.shape[1]):
        if np.std(X[:, j]) < 1e-12 or np.std(y) < 1e-12:
            correlations.append(0.0)
        else:
            correlations.append(float(np.corrcoef(X[:, j], y)[0, 1]))

    return {
        "explained_variance_ratio": pca.explained_variance_ratio_,
        "components": pca.components_,
        "n_components_90pct": n90,
        "feature_objective_correlation": np.asarray(correlations),
    }


def high_performance_subset(X, y, quantile=0.60):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float).reshape(-1)
    threshold = float(np.quantile(y, quantile))
    mask = y >= threshold
    if mask.sum() < 2:
        idx = np.argsort(y)[-2:]
        return X[idx], y[idx]
    return X[mask], y[mask]
