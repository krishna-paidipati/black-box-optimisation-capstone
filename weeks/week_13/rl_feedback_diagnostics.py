"""RL-inspired diagnostics for the final BBO decision round.

This module does not replace the Gaussian Process optimiser with reinforcement
learning. It uses reinforcement-learning concepts as an interpretive layer:
recent reward changes are treated as feedback, and the final query policy is
classified as exploitation, boundary refinement, or cautious exploration.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass(frozen=True)
class FeedbackSignal:
    function: str
    previous_reward: float
    latest_reward: float
    improvement: float
    policy: str
    rationale: str


def reward_improvement(previous_reward: float, latest_reward: float) -> float:
    """Return the maximisation improvement from one round to the next."""
    return latest_reward - previous_reward


def build_feedback_signals(
    previous: Dict[str, float],
    latest: Dict[str, float],
) -> Iterable[FeedbackSignal]:
    """Create transparent final-round feedback records.

    Policies are intentionally supplied from the observed BBO history rather
    than inferred from a generic threshold rule. This keeps the diagnostic
    faithful to the actual decisions made in the capstone.
    """
    decisions = {
        "function_1": (
            "boundary refinement",
            "Week 12 recovered from the Week 11 deterioration, so the final query moves back toward the stronger historical region.",
        ),
        "function_2": (
            "local refinement",
            "Week 12 weakened relative to the historically stronger x2≈0.40 neighbourhood, so the final query stays close to that region without repeating it exactly.",
        ),
        "function_3": (
            "cautious exploration",
            "The latest result improved only marginally and earlier repeated-input behaviour suggested possible noise or flatness.",
        ),
        "function_4": (
            "exploitation",
            "Week 12 produced a clear new best, supporting another very small local step.",
        ),
        "function_5": (
            "exploitation",
            "With x2–x4 stable at the upper boundary, controlled increases in x1 continued to improve reward.",
        ),
        "function_6": (
            "exploitation",
            "Week 12 produced a strong new best, so the final query remains tightly centred on that neighbourhood.",
        ),
        "function_7": (
            "exploitation",
            "Several consecutive rounds improved the objective, supporting a smaller continuation along the same local trajectory.",
        ),
        "function_8": (
            "plateau-aware exploitation",
            "Reward is still improving but by very small amounts, so only a tiny continuation is justified.",
        ),
    }

    for function, latest_reward in latest.items():
        previous_reward = previous[function]
        policy, rationale = decisions[function]
        yield FeedbackSignal(
            function=function,
            previous_reward=previous_reward,
            latest_reward=latest_reward,
            improvement=reward_improvement(previous_reward, latest_reward),
            policy=policy,
            rationale=rationale,
        )
