# Black-Box Optimisation Capstone

Portfolio repository for Stage 2 of the black-box optimisation (BBO) capstone challenge.
The challenge contains eight unknown maximisation functions with input dimensionality from 2D to 8D. One new query point is submitted per function in each weekly round, and the returned observations are incorporated into the next round.

## Objectives

- Maintain a reproducible record of every submitted query and returned observation.
- Compare exploration and exploitation strategies across functions with different dimensionality and behaviour.
- Use surrogate modelling and acquisition functions where appropriate.
- Document what was learned after every round and how the next strategy changed.
- Produce a portfolio-ready record of the complete optimisation process.

## Repository structure

```text
bbo-capstone/
├── README.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── data/
│   └── raw/
│       └── README.md
├── scripts/
│   └── validate_submission.py
├── src/
│   └── bbo/
│       ├── __init__.py
│       ├── acquisition.py
│       ├── candidates.py
│       ├── data.py
│       ├── formatting.py
│       └── surrogate.py
└── weeks/
    ├── week_01/
    │   ├── README.md
    │   ├── queries.json
    │   ├── reflection.md
    │   └── run_week_01.py
    └── week_02 ... week_13/
```

## Initial data

The course-provided `.npy` files are intentionally not committed by default. Place the supplied directory locally at:

```text
data/raw/initial_data/function_1/initial_inputs.npy
data/raw/initial_data/function_1/initial_outputs.npy
...
data/raw/initial_data/function_8/initial_inputs.npy
data/raw/initial_data/function_8/initial_outputs.npy
```

This keeps the repository focused on reproducible code and avoids redistributing course material unless permission is explicit.

## Optimisation workflow

For each weekly round:

1. Load all observations available so far.
2. Inspect the current best value for each function.
3. Fit or update a surrogate model where appropriate.
4. Generate candidate points in the unit hypercube `[0, 1]^d`.
5. Score candidates using an acquisition rule such as UCB or Expected Improvement.
6. Select one query per function, balancing exploration and exploitation.
7. Validate portal formatting to six decimal places.
8. Submit queries and record returned outputs when released.
9. Update the weekly reflection and strategy for the next round.

## Week 1 strategy

The first round used a mixed strategy rather than one rule for all eight functions:

- **F1:** exploration because initial outputs provide little localisation information.
- **F2–F4:** Bayesian-optimisation-style balance of predicted performance and uncertainty.
- **F5:** stronger exploitation because the supplied description indicates a typically unimodal landscape and the initial data contain a standout high value.
- **F6–F8:** surrogate-guided search with increasing attention to uncertainty as dimensionality rises.

The exact Week 1 portal submissions are recorded in `weeks/week_01/queries.json`.

## Reproducibility

Create an environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# .venv\\Scripts\\activate       # Windows
pip install -r requirements.txt
```

Validate a weekly query file:

```bash
python scripts/validate_submission.py weeks/week_01/queries.json
```

Run the Week 1 data summary locally after placing the initial data under `data/raw/`:

```bash
python weeks/week_01/run_week_01.py
```

## Weekly version-control convention

Suggested branch and commit convention:

```text
branch: week-01-analysis
commit: capstone: add Week 1 BBO queries and baseline workflow
```

Future rounds should use similarly focused commits such as:

```text
capstone: add Week 2 observations and update acquisition strategy
```

## Notes on interpretation

All eight challenge functions are already framed as **maximisation** tasks. Negative objective values must therefore still be maximised: a value of `-0.5` is better than `-4.0`.
