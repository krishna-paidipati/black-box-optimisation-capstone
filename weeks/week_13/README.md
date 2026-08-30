# Final Round — Reinforcement-Learning-Informed Decision Policy

This folder records the final submitted BBO queries and the confirmed Week 12
portal outputs that informed them.

The final strategy is predominantly exploitative because the accumulated
history identifies several stable high-performing neighbourhoods. Reinforcement
learning concepts are used as an interpretive framework rather than as a new
replacement optimiser:

- **MAB:** exploration is reduced as confidence in productive regions grows.
- **Q-learning analogy:** each returned objective value updates the expected
  usefulness of a local search direction.
- **MDP/feedback adaptation:** the next decision depends on the observed state
  of the search, including improvement, deterioration, plateauing and possible
  noise.
- **Model-based planning:** Gaussian Process and acquisition reasoning remain
  the primary numerical foundation for anticipating useful queries.

## Files

- `week_12_outputs.json`: confirmed Week 12 portal responses.
- `queries.json`: authoritative final-round portal inputs.
- `reflection.md`: submitted final reflection connecting BBO to RL concepts.
- `rl_feedback_diagnostics.py`: transparent reward-feedback interpretation.
- `run_week_13.py`: validates dimensions/ranges and prints portal-formatted
  queries plus Week 11-to-Week 12 feedback signals.

Final-round outputs are not recorded here unless and until they are returned by
the portal.
