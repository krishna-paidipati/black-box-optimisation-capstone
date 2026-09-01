# Week 13 - Final Round: Reinforcement-Learning-Informed Decision Policy

This folder records the final submitted BBO queries, the confirmed Week 12
portal outputs that informed them, and the confirmed Week 13 final results.

The final strategy was predominantly exploitative because the accumulated
history identified several stable high-performing neighbourhoods.
Reinforcement-learning concepts were used as an interpretive framework rather
than as a replacement optimiser:

- **MAB:** exploration was reduced as confidence in productive regions grew.
- **Q-learning analogy:** each returned objective value updated the expected
  usefulness of a local search direction.
- **MDP/feedback adaptation:** each decision depended on the observed state of
  the search, including improvement, deterioration, plateauing and possible
  noise.
- **Model-based planning:** Gaussian Process and acquisition reasoning remained
  the primary numerical foundation for anticipating useful queries.

## Final results

| Function | Week 12 output | Week 13 output | Final-round interpretation |
| --- | ---: | ---: | --- |
| Function 1 | -0.000257625 | 0.000009275 | Improved from Week 12; earlier historical best remains stronger |
| Function 2 | 0.466468 | 0.580837 | Improved from Week 12; earlier historical best remains stronger |
| Function 3 | -0.008870836 | **-0.008177177** | New observed best |
| Function 4 | 0.489870 | **0.506202790** | New observed best |
| Function 5 | 4440.508976 | **4440.569946** | New observed best |
| Function 6 | **-0.279008828** | -0.301653119 | Deteriorated relative to Week 12 |
| Function 7 | 1.783677 | **1.795256370** | New observed best |
| Function 8 | 9.946174 | **9.946284399** | New observed best; improvement remains small |

The final round therefore produced new observed best values for five of the
eight functions. Functions 1 and 2 recovered relative to Week 12 but remained
below stronger observations from earlier rounds. Function 6 moved away from
its Week 12 best, illustrating that even tightly focused local exploitation
does not guarantee improvement under a sparse black-box evaluation budget.

## Files

- `week_12_outputs.json`: confirmed Week 12 portal responses used to select the
  final queries.
- `queries.json`: authoritative Week 13 final-round portal inputs.
- `week_13_outputs.json`: confirmed Week 13 final-round portal responses.
- `reflection.md`: submitted final reflection connecting BBO to
  reinforcement-learning concepts.
- `rl_feedback_diagnostics.py`: transparent reward-feedback interpretation.
- `run_week_13.py`: validates dimensions and ranges and prints portal-formatted
  queries together with the Week 11-to-Week 12 feedback signals used before
  the final submission.