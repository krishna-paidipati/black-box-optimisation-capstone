"""Transparent decision records for Week 10.

The goal is not to claim that these explanations mathematically prove the
queries are optimal. They record the empirical evidence, assumption and search
intent behind each portal submission so another reviewer can audit the logic.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class DecisionRecord:
    function: int
    intent: str
    evidence: str
    assumption: str

RECORDS = (
    DecisionRecord(1, "local exploitation",
        "Weeks 7-9 improved by orders of magnitude as both coordinates moved downward.",
        "The improving local direction continues over a small additional step."),
    DecisionRecord(2, "controlled interpolation",
        "Recent x2=0.6 recovered performance, while earlier x2 near 0.145 produced stronger historical values.",
        "A point between the two regimes can reveal whether the response changes smoothly."),
    DecisionRecord(3, "return to best recent basin",
        "Week 8 outperformed the Week 9 perturbation.",
        "The Week 8 neighbourhood remains locally promising."),
    DecisionRecord(4, "local exploitation",
        "Weeks 6 and 8 were stronger than Week 9.",
        "Small movement around their shared neighbourhood is preferable to broad exploration."),
    DecisionRecord(5, "one-dimensional sensitivity probe",
        "x2-x4 remain saturated near one; increasing x1 to 0.001 produced a tiny new best.",
        "Holding three coordinates fixed makes the x1 effect easier to interpret."),
    DecisionRecord(6, "return toward stronger basin",
        "Week 7 remains better than Weeks 8 and 9.",
        "A conservative move toward that region is preferable to continuing the weaker trajectory."),
    DecisionRecord(7, "local exploitation",
        "Week 9 produced a substantial new best of 1.697238.",
        "The new basin is worth refining with small coordinate changes."),
    DecisionRecord(8, "return to recent high basin",
        "Week 9's larger move weakened performance; Weeks 5 and 8 were stronger.",
        "The tighter previous region remains the best-supported local target."),
)
