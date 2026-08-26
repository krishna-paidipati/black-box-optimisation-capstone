"""Week 10 audit and submission-validation runner."""
import json, sys
from pathlib import Path

WEEK = Path(__file__).resolve().parent
sys.path.insert(0, str(WEEK))
from decision_trace import RECORDS

DIMS={1:2,2:2,3:3,4:4,5:4,6:5,7:6,8:8}

def validate(q, dim):
    parts=q.split("-")
    if len(parts)!=dim:
        raise ValueError(f"Expected {dim} coordinates")
    for p in parts:
        if not p.startswith("0.") or len(p.split(".")[-1]) != 6:
            raise ValueError(f"Invalid six-decimal coordinate: {p}")
        if not 0 <= float(p) < 1:
            raise ValueError(f"Out-of-range coordinate: {p}")

def main():
    outputs=json.loads((WEEK/"week_09_outputs.json").read_text())
    queries=json.loads((WEEK/"queries.json").read_text())
    for record in RECORDS:
        key=f"function_{record.function}"
        validate(queries[key], DIMS[record.function])
        print(f"\nF{record.function}: {queries[key]}")
        print(f"Week 9 output: {outputs[key]:.12g}")
        print(f"Intent: {record.intent}")
        print(f"Evidence: {record.evidence}")
        print(f"Assumption: {record.assumption}")

if __name__=="__main__":
    main()
