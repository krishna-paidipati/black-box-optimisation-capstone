# Datasheet — BBO Capstone Query and Evaluation Dataset

Confirmed portal responses are available through **Week 12**. The final-round
queries have been submitted; their outputs are not yet recorded.

The dataset consists of the initial course observations plus one sequential
query/output pair per function per completed evaluation round. The eight hidden
maximisation functions range from 2D to 8D.

The repository stores each round's submitted query separately from the outputs
that later informed the next round. `weeks/week_13/week_12_outputs.json`
therefore contains the confirmed Week 12 feedback used to select the final
queries, while `weeks/week_13/queries.json` records the final submitted
inputs.

Later rounds are increasingly concentrated around high-performing regions. This
adaptive sampling creates exploitation bias: the observed query distribution is
not a uniform representation of the full unit hypercube. Consequently, PCA,
clustering, feature importance and feature/objective correlations are treated as
diagnostics of the sampled history rather than proof of global structure or
causality.

Function 3 has shown different returned values for an identical previously
repeated query, so possible observation variability is retained as a limitation
rather than silently assuming a deterministic response surface.

Week 12 produced new observed best values for Functions 3, 4, 5, 6, 7 and 8
within the recorded project history. Those results strengthened the case for a
predominantly exploitative final policy, while Functions 1 and 2 continued to
require boundary/local-region caution.
