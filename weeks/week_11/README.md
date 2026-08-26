# Week 11 — Cluster-guided local refinement

Week 11 adds KMeans and nearest-neighbour diagnostics to identify recurring
local regions in input space. Clustering is used for interpretation only; the
primary numerical optimisation workflow remains GP/acquisition based.

## Files
- `run_week_11.py`
- `cluster_diagnostics.py`
- `week_10_outputs.json`
- `queries.json`
- `reflection.md`

## Week 11 queries
| Function | Query |
|---|---|
| F1 | `0.655000-0.680000` |
| F2 | `0.700000-0.350000` |
| F3 | `0.495000-0.452500-0.404000` |
| F4 | `0.413000-0.414000-0.384000-0.399000` |
| F5 | `0.015000-0.999999-0.999999-0.999999` |
| F6 | `0.512000-0.318000-0.670000-0.952000-0.108000` |
| F7 | `0.000100-0.390000-0.361000-0.212000-0.370000-0.790000` |
| F8 | `0.087000-0.054000-0.079000-0.082000-0.999950-0.523000-0.219000-0.272000` |
