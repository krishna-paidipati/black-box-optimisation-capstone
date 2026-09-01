# Datasheet - BBO Capstone Query and Evaluation Dataset

Confirmed portal responses are available for all 13 submitted rounds,
including the final Week 13 evaluation.

The dataset consists of the initial course observations plus one sequential
query/output pair per function per completed evaluation round. The eight hidden
maximisation functions range from 2D to 8D.

The repository stores each round's submitted query separately from the outputs
that subsequently informed the next round. For the final iteration,
`weeks/week_13/week_12_outputs.json` contains the confirmed Week 12 feedback
used to select the final queries, `weeks/week_13/queries.json` records the
submitted Week 13 inputs, and `weeks/week_13/week_13_outputs.json` records
their confirmed final portal responses.

The original course-provided raw data are not redistributed in this public
repository. Authorised users can supply those files locally when reproducing
data-dependent analyses.

Later rounds became increasingly concentrated around high-performing regions.
This adaptive sampling creates exploitation bias: the observed query
distribution is not a uniform representation of the full unit hypercube.
Consequently, PCA, clustering, feature importance and feature/objective
correlations are treated as diagnostics of the sampled history rather than
proof of global structure or causality.

Function 3 returned different values for an identical previously repeated
query. Possible observation variability is therefore retained as a limitation
rather than silently assuming a deterministic response surface.

Week 12 produced new observed best values for Functions 3, 4, 5, 6, 7 and 8
within the recorded project history and informed a predominantly exploitative
final policy.

Week 13 subsequently produced new observed best values for Functions 3, 4, 5,
7 and 8. Functions 1 and 2 improved relative to Week 12 but did not exceed
their earlier historical best observations. Function 6 deteriorated relative
to its Week 12 best. The complete history therefore illustrates both the value
and the limitations of increasingly local exploitation under a constrained
black-box query budget.