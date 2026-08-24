# Week 1

## Status

Queries submitted. Returned outputs are pending.

## Strategy

Week 1 intentionally used different levels of exploration and exploitation across the eight functions rather than forcing a single acquisition rule onto every landscape.

- **Function 1:** exploration-oriented because the initial observations provide little evidence about the location of narrow peaks.
- **Function 2:** balanced exploration/exploitation for a noisy 2D landscape with local optima.
- **Functions 3–4:** surrogate-guided search using expected improvement / uncertainty.
- **Function 5:** stronger exploitation because the supplied prior indicates a typically unimodal function and the initial data contain a standout observation.
- **Functions 6–8:** surrogate-guided search, with uncertainty becoming increasingly important as dimensionality rises.

## Next action

When Week 1 outputs are released:

1. Record the eight returned outputs in `queries.json` (or a separate observations file).
2. Append the query/output pairs to the modelling dataset.
3. Compare actual outcomes against the previous best and GP predictions.
4. Refit the surrogate for each function.
5. Select Week 2 points independently based on the new evidence.
