# Week 9 — Scaling-aware optimisation

Week 9 incorporates the confirmed Week 8 outputs and adds explicit diagnostics
for diminishing returns and best-so-far improvement.

The project does not claim that LLM parameter scaling laws directly describe
the hidden mathematical functions. Instead, the implementation measures
**optimisation scaling**: how the best objective value changes as additional
queries are evaluated.

`scaling_aware_search.py` uses this progress signal to adapt the proportion of
candidate-search budget allocated to local exploitation versus global
exploration. Gaussian Process Expected Improvement remains the numerical
ranking mechanism.

## Files

- `run_week_09.py` — Week 9 entry point and portal-query validation.
- `scaling_aware_search.py` — best-so-far and adaptive local/global search
  diagnostics.
- `week_08_outputs.json` — confirmed Week 8 responses.
- `queries.json` — exact Week 9 portal submissions.
- `reflection.md` — Week 9 discussion-board reflection.

## Week 9 queries

| Function | Query |
|---|---|
| F1 | `0.685000-0.700000` |
| F2 | `0.700000-0.600000` |
| F3 | `0.501500-0.441000-0.421500` |
| F4 | `0.414500-0.418500-0.386000-0.387500` |
| F5 | `0.001000-0.999999-0.999999-0.999999` |
| F6 | `0.475000-0.335000-0.705000-0.985000-0.130000` |
| F7 | `0.000100-0.382000-0.365000-0.195000-0.382000-0.795000` |
| F8 | `0.120000-0.055000-0.050000-0.160000-0.999999-0.460000-0.205000-0.350000` |
