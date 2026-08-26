# Week 10 — Transparent and interpretable query selection

Week 10 makes the reasoning behind each query explicit. The implementation
adds an auditable `DecisionRecord` for every function containing:

- search intent;
- empirical evidence used;
- the assumption behind the next move.

This does not claim the hidden functions are interpretable. It makes the
**decision process** interpretable and reproducible from the evidence available
at submission time.

## Files
- `run_week_10.py` — validates submissions and prints the decision audit.
- `decision_trace.py` — function-specific evidence and assumptions.
- `week_09_outputs.json` — confirmed Week 9 responses.
- `queries.json` — exact Week 10 portal submissions.
- `reflection.md` — Week 10 discussion reflection.

## Week 10 queries

| Function | Query |
|---|---|
| F1 | `0.670000-0.690000` |
| F2 | `0.700000-0.400000` |
| F3 | `0.490000-0.452500-0.404000` |
| F4 | `0.413000-0.413000-0.384000-0.398000` |
| F5 | `0.005000-0.999999-0.999999-0.999999` |
| F6 | `0.510000-0.320000-0.680000-0.950000-0.105000` |
| F7 | `0.000100-0.386000-0.363000-0.205000-0.375000-0.792000` |
| F8 | `0.085000-0.055000-0.080000-0.080000-0.999950-0.525000-0.220000-0.270000` |
