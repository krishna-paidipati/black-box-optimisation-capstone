"""Portal formatting and validation helpers."""

from __future__ import annotations

import re
from collections.abc import Sequence


QUERY_RE = re.compile(r"^0\.\d{6}(?:-0\.\d{6})*$")


def format_query(values: Sequence[float]) -> str:
    """Format a query exactly as required by the capstone portal."""
    values = [float(v) for v in values]
    if not all(0.0 <= v < 1.0 for v in values):
        raise ValueError("Every coordinate must satisfy 0 <= x < 1 for portal formatting.")
    return "-".join(f"{v:.6f}" for v in values)


def validate_query_string(query: str, expected_dimensions: int) -> bool:
    """Validate six-decimal portal syntax and dimensionality."""
    if not QUERY_RE.fullmatch(query):
        return False
    return len(query.split("-")) == expected_dimensions
