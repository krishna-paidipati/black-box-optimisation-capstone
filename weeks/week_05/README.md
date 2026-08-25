# Week 5 — Coarse-to-fine optimisation

Week 5 incorporates the confirmed Week 4 responses and uses a structured
coarse-to-fine Gaussian Process search. The Week 4 neural ensemble is retained
as a secondary consistency check rather than replacing the GP.

## Files

- `run_week_05.py` — reproducible Week 5 entry point. Reconstructs all data
  available before the Week 5 submission, executes the coarse-to-fine search,
  checks high-EI candidates with the neural ensemble, and prints the exact
  historical portal queries.
- `coarse_to_fine.py` — two-stage Expected Improvement candidate-refinement
  helper.
- `week_04_outputs.json` — confirmed Week 4 portal responses used for Week 5.
- `queries.json` — exact Week 5 portal submissions.
- `reflection.md` — Week 5 discussion-board reflection.

## Reproduce the analysis

From the repository root:

```bash
python weeks/week_05/run_week_05.py
```

The course-provided initial `.npy` files must exist locally under
`data/raw/initial_data/`. They are intentionally excluded from the public
repository.

As in earlier rounds, `queries.json` is the authoritative record of the actual
submission. The reproducible runner documents the modelling evidence available
at that stage without rewriting the historical decision process.
