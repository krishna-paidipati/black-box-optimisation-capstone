# Week 7 — Gaussian Process hyperparameter tuning

Week 7 incorporates the confirmed Week 6 outputs and makes Gaussian Process
hyperparameter tuning an explicit part of the BBO workflow.

## Tuned hyperparameters

The runner compares:

- RBF and Matérn (`ν = 0.5`, `1.5`, `2.5`) kernel families;
- `alpha` values from `1e-8` to `1e-2`.

Configurations are compared with shuffled K-fold validation using normalised
RMSE. After selection, the winning GP is refitted on all observations and used
to report Expected Improvement diagnostics.

Function 1 is modelled in log-output space because its positive responses span
many orders of magnitude. This transformation is used only by the surrogate;
the black-box objective remains the original maximisation problem.

## Files

- `run_week_07.py` — reproducible Week 7 entry point.
- `gp_hyperparameter_tuning.py` — explicit GP tuning implementation.
- `week_06_outputs.json` — confirmed Week 6 portal responses.
- `queries.json` — exact Week 7 portal submissions.
- `reflection.md` — Week 7 discussion-board reflection.

## Week 7 portal queries

| Function | Query |
|---|---|
| F1 | `0.716000-0.721000` |
| F2 | `0.699800-0.145615` |
| F3 | `0.485000-0.452500-0.404000` |
| F4 | `0.414800-0.416500-0.385000-0.392000` |
| F5 | `0.000000-0.999999-0.999999-0.999999` |
| F6 | `0.517500-0.325000-0.690000-0.950000-0.105000` |
| F7 | `0.000050-0.374000-0.368000-0.178000-0.396000-0.801500` |
| F8 | `0.082000-0.050000-0.082000-0.070000-0.999999-0.520000-0.218000-0.255000` |

Run from the repository root:

```bash
python weeks/week_07/run_week_07.py
```
