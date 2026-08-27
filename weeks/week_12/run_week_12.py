"""Week 12 PCA-informed diagnostic runner."""

import json
from pathlib import Path

WEEK = Path(__file__).resolve().parent
DIMS = {1:2, 2:2, 3:3, 4:4, 5:4, 6:5, 7:6, 8:8}


def validate_query(query, expected_dim):
    parts = query.split("-")
    if len(parts) != expected_dim:
        raise ValueError("Wrong query dimensionality")
    for part in parts:
        if not part.startswith("0.") or len(part.split(".")[-1]) != 6:
            raise ValueError(f"Invalid coordinate format: {part}")
        if not 0.0 <= float(part) < 1.0:
            raise ValueError(f"Coordinate outside [0,1): {part}")


def main():
    outputs = json.loads((WEEK/"week_11_outputs.json").read_text())
    queries = json.loads((WEEK/"queries.json").read_text())

    print("Confirmed Week 11 outputs and Week 12 submissions")
    print("=" * 72)
    for fid in range(1, 9):
        key = f"function_{fid}"
        validate_query(queries[key], DIMS[fid])
        print(f"F{fid}: Week 11 y={outputs[key]:.12g}")
        print(f"    Week 12 query={queries[key]}")

    print("\nUse pca_diagnostics.py with the reconstructed historical X/y data")
    print("to inspect explained variance, loadings and redundancy.")


if __name__ == "__main__":
    main()
