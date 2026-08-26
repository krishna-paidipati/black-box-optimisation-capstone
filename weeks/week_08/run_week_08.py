"""Week 8 repository entry point.

Validates the exact historical Week 8 submissions and demonstrates the
structured prompting layer. Numerical GP/EI optimisation remains implemented
in the reusable project modules and prior weekly analyses.
"""
import json, sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
WEEK=Path(__file__).resolve().parent
sys.path.insert(0,str(WEEK))
from prompt_decision_support import build_decision_prompt, validate_query

DIMS={1:2,2:2,3:3,4:4,5:4,6:5,7:6,8:8}

def main():
    queries=json.loads((WEEK/"queries.json").read_text())
    outputs=json.loads((WEEK/"week_07_outputs.json").read_text())
    print("Confirmed Week 7 outputs used for Week 8 reasoning")
    for fid in range(1,9):
        key=f"function_{fid}"
        validate_query(queries[key],DIMS[fid])
        print(f"F{fid}: previous y={outputs[key]:.12g}")
        print(f"    Week 8 query: {queries[key]}")
    # Minimal example showing how the prompt helper is intended to be called.
    X=np.array([[0.716,0.721]])
    y=np.array([outputs["function_1"]])
    print("\nPrompt-support example:\n")
    print(build_decision_prompt(1,X,y))

if __name__=="__main__":
    main()
