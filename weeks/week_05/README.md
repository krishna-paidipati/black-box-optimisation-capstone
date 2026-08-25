# Week 5 — Coarse-to-fine optimisation

Week 5 incorporates the confirmed Week 4 responses and uses a more structured coarse-to-fine search process.

## Confirmed Week 4 outcomes

Function 5 improved strongly to `4436.361460610766`. Functions 2, 3, 4 and 6 did not improve on their previous best values, Function 7 recovered but remained below its Week 2 best, and Function 8 remained in the same high-performing basin.

## Strategy

The implementation does **not** introduce a deep CNN-style architecture because the BBO observations are small tabular datasets. Instead, the idea of hierarchical learning is applied to the optimisation workflow:

1. score a broad candidate set with the Gaussian Process;
2. retain the strongest candidates;
3. generate local perturbations around those candidates;
4. re-score the refined set;
5. use the neural surrogate only as a secondary consistency check.

This keeps the model complexity appropriate to the available data while making the query-selection procedure more systematic.

## Week 5 portal queries

| Function | Query |
|---|---|
| F1 | `0.726000-0.729000` |
| F2 | `0.700250-0.145615` |
| F3 | `0.430000-0.300000-0.403000` |
| F4 | `0.406212-0.395272-0.376650-0.416511` |
| F5 | `0.000001-0.999999-0.999999-0.999999` |
| F6 | `0.515000-0.310000-0.630000-0.920000-0.090000` |
| F7 | `0.000001-0.327863-0.361066-0.187758-0.389478-0.851552` |
| F8 | `0.080614-0.057829-0.080296-0.080738-0.999935-0.533313-0.221092-0.271013` |
