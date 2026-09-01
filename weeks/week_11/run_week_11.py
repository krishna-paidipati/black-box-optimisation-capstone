"""Week 11 cluster-diagnostic runner."""
import json, sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[2]
WEEK=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"src")); sys.path.insert(0,str(WEEK))
from bbo.data import best_observation, load_function_data
from cluster_diagnostics import cluster_observations, nearest_neighbour_distance
DATA_ROOT=ROOT/"data"/"raw"/"initial_data"
DIMS={1:2,2:2,3:3,4:4,5:4,6:5,7:6,8:8}

def load_json(p): return json.loads(Path(p).read_text())
def parse(q): return np.array([float(v) for v in q.split("-")])
def history(fid):
    X,y=load_function_data(DATA_ROOT,fid); key=f"function_{fid}"
    rounds=[
      ("week_01","week_02","week_01_outputs.json"),
      ("week_02","week_03","week_02_outputs.json"),
      ("week_03","week_04","week_03_outputs.json"),
      ("week_04","week_05","week_04_outputs.json"),
      ("week_05","week_06","week_05_outputs.json"),
      ("week_06","week_07","week_06_outputs.json"),
      ("week_07","week_08","week_07_outputs.json"),
      ("week_08","week_09","week_08_outputs.json"),
      ("week_09","week_10","week_09_outputs.json"),
      ("week_10","week_11","week_10_outputs.json")]
    for qw,ow,of in rounds:
        q=parse(load_json(ROOT/"weeks"/qw/"queries.json")[key])
        o=float(load_json(ROOT/"weeks"/ow/of)[key])
        X=np.vstack([X,q]); y=np.concatenate([y,[o]])
    return X,y
def validate(q,d):
    p=q.split("-")
    if len(p)!=d: raise ValueError("wrong dimension")
    for v in p:
        if not v.startswith("0.") or len(v.split(".")[-1])!=6:
            raise ValueError(f"bad format {v}")
        if not 0<=float(v)<1: raise ValueError(f"out of range {v}")
def main():
    if not DATA_ROOT.exists():
        raise SystemExit(
        "Initial data not found. Place the authorised course-provided "
        f"initial_data directory at {DATA_ROOT}"
        )
    for fid in range(1,9):
        X,y=history(fid); bx,by,_=best_observation(X,y)
        _,s=cluster_observations(X,y,random_state=1100+fid)
        nn=nearest_neighbour_distance(X)
        print(f"F{fid}: best_y={by:.12g}, best_x={bx}")
        print(f"  strongest_cluster_centroid={s[0].centroid}")
        print(f"  median_nn_distance={np.nanmedian(nn):.6f}")
    q=load_json(WEEK/"queries.json")
    print("\nAuthoritative Week 11 portal submissions")
    for fid in range(1,9):
        validate(q[f"function_{fid}"],DIMS[fid])
        print(f"F{fid}: {q[f'function_{fid}']}")
if __name__=="__main__": main()
