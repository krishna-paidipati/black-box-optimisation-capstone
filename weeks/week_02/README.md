# Week 2 — BBO Capstone

Week 2 incorporates the first returned observation for each black-box function and adapts the query strategy function-by-function.

## Week 1 outcome summary

| Function | Week 1 output | Direction versus initial best | Week 2 strategy |
|---|---:|---|---|
| F1 | 0.000000 | No informative improvement | Maximin exploration |
| F2 | 0.614339 | Small improvement | Local exploitation with a new value of x2 |
| F3 | -0.061921 | Worse than current best | Conservative exploitation between two strong historical points |
| F4 | 0.464810 | Large improvement | Local GP/EI exploitation around the successful Week 1 point |
| F5 | 2741.310044 | Very large improvement | Strong exploitation of the apparent unimodal peak |
| F6 | -0.457471 | Improvement | GP/EI search toward a higher (less negative) output |
| F7 | 1.208424 | Below historical best | Controlled local search near the strong region |
| F8 | 9.924448 | Improvement | GP/EI search around the newly promising 8D region |

## Modelling approach

The update uses the initial observations plus the Week 1 result. Gaussian Process surrogates with Matern/RBF kernels were used as decision-support models for most functions. Expected Improvement and UCB candidates were compared with simple local reasoning. The final query was not selected mechanically: prior structural information supplied in the challenge and the observed Week 1 response were also considered.

F1 remains a special case because nearly all responses are zero. A regression surrogate has little useful signal, so Week 2 uses a maximin space-filling query instead.

F5 is treated more exploitatively because the challenge describes it as typically unimodal and the Week 1 query increased the best value from approximately 1088.86 to 2741.31.

See `queries.json` for portal-ready values.
