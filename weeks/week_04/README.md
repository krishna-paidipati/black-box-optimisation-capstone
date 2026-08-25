# Week 4 — Neural-surrogate and gradient diagnostics

Week 4 incorporates the confirmed Week 3 responses and adds a compact PyTorch
neural-network ensemble as a **secondary** surrogate diagnostic. Gaussian
Process modelling remains the primary uncertainty-aware optimisation method.

## Files

- `run_week_04.py` — reproducible Week 4 entry point. Reconstructs all data
  available before the Week 4 submission, fits the GP and neural ensemble,
  reports acquisition diagnostics and input gradients, and prints the exact
  historical portal queries.
- `neural_surrogate.py` — compact MLP ensemble, prediction-disagreement and
  input-gradient utilities.
- `week_03_outputs.json` — confirmed Week 3 portal responses used for Week 4.
- `queries.json` — exact Week 4 portal submissions.
- `reflection.md` — Week 4 discussion-board reflection.

## Reproduce the analysis

From the repository root:

```bash
python weeks/week_04/run_week_04.py
```

The course-provided initial `.npy` files must exist locally under
`data/raw/initial_data/`. They are intentionally excluded from the public
repository.

The stored `queries.json` file is the authoritative record of what was actually
submitted; diagnostic model outputs are not retroactively treated as the
historical query-selection mechanism.
