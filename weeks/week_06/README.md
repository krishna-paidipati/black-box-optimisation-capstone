# Week 6 — Feature-guided multi-resolution refinement

Week 6 incorporates the confirmed Week 5 outputs and introduces a
feature-guided local refinement stage.

A CNN is **not** fitted to the BBO data because the observations are small
tabular datasets. Instead, the CNN concept of progressive feature extraction is
translated into the search process:

1. fit the Gaussian Process surrogate;
2. estimate non-linear feature importance with Extra Trees;
3. assign smaller perturbation scales to influential dimensions;
4. allow wider perturbations in less influential dimensions;
5. rank the resulting candidates by Gaussian Process Expected Improvement.

## Files

- `run_week_06.py` — reproducible Week 6 entry point.
- `feature_guided_refinement.py` — feature-importance and multi-resolution
  candidate-generation implementation.
- `week_05_outputs.json` — confirmed Week 5 responses.
- `queries.json` — exact Week 6 portal submissions.
- `reflection.md` — Week 6 discussion-board reflection.

## Week 6 portal queries

| Function | Query |
|---|---|
| F1 | `0.721000-0.725000` |
| F2 | `0.693500-0.999999` |
| F3 | `0.525000-0.452000-0.404000` |
| F4 | `0.413000-0.412000-0.384000-0.400000` |
| F5 | `0.000002-0.999999-0.999999-0.999999` |
| F6 | `0.520000-0.340000-0.750000-0.980000-0.120000` |
| F7 | `0.000001-0.370000-0.365000-0.176000-0.397000-0.805000` |
| F8 | `0.030000-0.080000-0.060000-0.070000-0.999999-0.620000-0.220000-0.230000` |

Run from the repository root with:

```bash
python weeks/week_06/run_week_06.py
```
