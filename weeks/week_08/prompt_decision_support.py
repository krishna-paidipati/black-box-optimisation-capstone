"""Structured prompt decision support for Week 8.

Prompting supplements rather than replaces the numerical BBO optimiser.
"""
import numpy as np

def build_decision_prompt(function_id, X, y):
    """Create a compact evidence-grounded review prompt."""
    X=np.asarray(X,float); y=np.asarray(y,float).reshape(-1)
    top=np.argsort(y)[::-1][:min(5,len(y))]
    obs="\n".join(
        f"- x={np.array2string(X[i],precision=6)}, y={y[i]:.12g}" for i in top
    )
    return f"""Function {function_id} BBO review.
Objective: maximise. Dimensions: {X.shape[1]}. Observations: {len(y)}.
Five best observed points:
{obs}
Compare exploration and exploitation using only supplied evidence.
Do not invent hidden equations or objective values.
"""

def validate_query(query, expected_dim):
    """Validate portal dimensionality, six decimals and [0,1) bounds."""
    parts=query.split("-")
    if len(parts)!=expected_dim:
        raise ValueError(f"Expected {expected_dim} coordinates")
    for p in parts:
        if not p.startswith("0.") or len(p.split(".")[-1])!=6:
            raise ValueError(f"Invalid coordinate format: {p}")
    values=np.array([float(p) for p in parts])
    if np.any(values<0) or np.any(values>=1):
        raise ValueError("Coordinates must be in [0,1).")
    return values
