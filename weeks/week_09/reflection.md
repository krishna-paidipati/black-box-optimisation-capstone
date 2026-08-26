# Week 9 Reflection — Scaling, Emergence and Risk

## How do scaling laws influence your current query choices?

I interpreted scaling in this capstone as the relationship between additional
black-box evaluations and best-so-far improvement. The results now show both
steady progress and diminishing returns. Function 1 improved by several orders
of magnitude in recent rounds, while Function 5 has effectively plateaued near
4440.48. I therefore do not allocate the same exploration/exploitation balance
to every function. Sustained improvement supports tighter local refinement,
whereas a plateau justifies reserving more search effort for alternative
regions.

## Where might emergent behaviours alter your expectations?

An unknown function can exhibit a sharp threshold or narrow high-performing
region that is not obvious from sparse observations. Function 1 is the clearest
example: small movements around the current region changed the output by
orders of magnitude. I treat such behaviour as evidence that smooth local
assumptions may fail. I therefore keep uncertainty-aware exploration available
instead of assuming every response surface changes gradually.

## What trade-offs between cost, robustness and performance shape the strategy?

Each function allows only one new evaluation per round, so the opportunity cost
of a poor query is high. Pure exploitation is computationally and statistically
efficient when a basin is well established, but it can miss another optimum.
Pure exploration improves coverage but may sacrifice immediate performance.
My current strategy uses Gaussian Process uncertainty and best-so-far trends to
decide how much candidate-search budget should be local versus global.

## How do you balance predictable optimisation with sudden emergent capability?

I do not treat a single surprising result as proof of a new optimum. I compare
it with nearby observations and the complete historical trajectory. Where
performance improves repeatedly, I exploit more aggressively. Where a sudden
jump occurs without nearby confirmation, I retain exploratory alternatives.
This balances the opportunity presented by unexpected behaviour with the risk
of overreacting to sparse or noisy evidence.

The same principle applies to prompting and decoding. Structured prompts and
conservative decoding are useful for reproducible decision support, while
numerical GP/acquisition evidence remains the primary basis for the submitted
queries. This keeps the workflow robust as the amount of context and modelling
complexity increase.
