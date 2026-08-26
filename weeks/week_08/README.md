# Week 8 — Structured prompt decision support

Week 8 incorporates the confirmed Week 7 outputs and applies the module's
prompting concepts as a decision-support layer around the established BBO
workflow.

The LLM is **not** represented as the numerical optimiser. Gaussian Process
modelling, acquisition diagnostics and accumulated empirical evidence remain
the quantitative foundation. The Week 8 prompt utility instead creates compact,
function-specific evidence summaries and validates the strict portal format.

## Files

- `run_week_08.py` — Week 8 entry point and submission validation.
- `prompt_decision_support.py` — structured prompt builder and query validator.
- `week_07_outputs.json` — confirmed Week 7 responses.
- `queries.json` — exact Week 8 portal submissions.
- `reflection.md` — Week 8 discussion-board reflection.

## Week 8 queries

| Function | Query |
|---|---|
| F1 | `0.700000-0.710000` |
| F2 | `0.699550-0.145500` |
| F3 | `0.490000-0.452500-0.404000` |
| F4 | `0.412000-0.410000-0.383000-0.402000` |
| F5 | `0.000003-0.999999-0.999999-0.999999` |
| F6 | `0.518000-0.322000-0.680000-0.945000-0.102000` |
| F7 | `0.000100-0.375500-0.368500-0.177500-0.396000-0.800000` |
| F8 | `0.081000-0.055000-0.081000-0.078000-0.999950-0.530000-0.220000-0.268000` |

Run with:

```bash
python weeks/week_08/run_week_08.py
```
