"""Mastery progression prediction.

Two independent methods are provided so the UI can show whichever is more
reliable for the current student:

1. **Exponential model** (``find_sessions_to_target``)
   Assumes mastery follows the exponential learning curve
       m(t) = 1 - (1 - m₀) · exp(-λ · t)
   where λ is the *effective learning rate* computed from the student's
   prerequisite readiness and the skill difficulty (see mastery_model.py).
   The model is solved analytically (binary search) to find the number of
   sessions t* such that m(t*) = target_mastery.

   This is the *default* estimate shown before the student has enough
   practice history.

2. **Linear regression** (``linear_regression_prediction``)
   Fits a straight line y = m·x + b to the student's recorded mastery
   snapshots using least-squares (numpy.polyfit).  When the fit is good
   (R² > 0.4) this estimate replaces the exponential model because it is
   grounded in real observed progress — not a theoretical assumption.

   Extrapolation: from the fitted slope we solve for the session index x*
   where y = target_mastery, then subtract the number of already-completed
   sessions to get attempts_remaining.

Both functions return attempt counts; the caller multiplies by
MINS_PER_ATTEMPT to convert to minutes.
"""

import numpy as np

from core.mastery_model import mastery_after_sessions


def find_sessions_to_target(
    initial_mastery,
    learning_rate,
    target_mastery,
    max_sessions=100,
    eps=0.01,
):
    """Estimate sessions needed to reach *target_mastery* using the exponential model.

    The exponential learning curve   m(t) = 1 - (1 - m₀)·exp(-λ·t)
    approaches 1 asymptotically but never quite reaches it.  We therefore
    check first whether m(max_sessions) ≥ target_mastery; if not the skill
    is considered unreachable within the budget and we return (max_sessions, False).

    When reachable, a binary search on t finds the crossing point to within
    *eps* sessions.  Binary search works here because m(t) is strictly
    monotone increasing for λ > 0.

    Parameters
    ----------
    initial_mastery : float   Current mastery level in [0, 1].
    learning_rate   : float   λ — effective rate from effective_learning_rate().
    target_mastery  : float   Mastery threshold to reach (e.g. 0.8).
    max_sessions    : int     Upper bound on the search; also the cap returned
                              when the skill is unreachable.
    eps             : float   Stopping criterion for binary search (session precision).

    Returns
    -------
    (sessions, reachable) : (float, bool)
        sessions  — estimated sessions to reach target (≤ max_sessions).
        reachable — True if target_mastery is achievable within max_sessions.
    """
    if initial_mastery >= target_mastery:
        return 0, True

    # Check whether the target is reachable at all within the budget.
    final_mastery = mastery_after_sessions(initial_mastery, learning_rate, max_sessions)
    if final_mastery < target_mastery:
        return max_sessions, False

    # Binary search: find t* s.t. m(t*) = target_mastery.
    # Invariant: m(left) < target ≤ m(right).
    left, right = 0, max_sessions
    while right - left > eps:
        mid = (left + right) / 2
        if mastery_after_sessions(initial_mastery, learning_rate, mid) >= target_mastery:
            right = mid
        else:
            left = mid
    return right, True


def linear_regression_prediction(mastery_history, target_mastery):
    """Predict remaining attempts to *target_mastery* using linear regression.

    Algorithm
    ---------
    Given a sequence of mastery snapshots [m₀, m₁, …, mₙ] (one per practice
    session), we fit the linear model

        m̂(x) = slope · x + intercept

    by minimising the sum of squared residuals (OLS via numpy.polyfit).

    The *coefficient of determination* R² measures goodness of fit:
        R² = 1 - SS_res / SS_tot
    where SS_res = Σ(mᵢ - m̂ᵢ)² and SS_tot = Σ(mᵢ - mean(m))².
    R² = 1 means perfect linear fit; R² ≤ 0 means the line is no better
    than predicting the mean.  We only trust the regression when R² > 0.4
    (checked by the caller).

    Extrapolation
    -------------
    Solve m̂(x*) = target_mastery for x*:
        x* = (target_mastery - intercept) / slope
    Remaining sessions = max(0, x* - (n − 1)) where n is the history length.

    Why linear and not exponential?
    --------------------------------
    In the *early* learning phase mastery rises roughly linearly per attempt
    because exp(-λt) ≈ 1 - λt for small λt.  Linear regression is therefore
    a good short-horizon approximation and is data-driven — it adapts to each
    student's actual pace rather than relying on theoretical λ.

    Parameters
    ----------
    mastery_history : list[float]
        Chronologically ordered mastery values, one per completed attempt.
        Minimum 3 points required; returns (None, None) otherwise.
    target_mastery  : float
        The mastery level to predict reaching (e.g. 0.8).

    Returns
    -------
    (attempts_remaining, r_squared) : (float, float) or (None, None)
        attempts_remaining — estimated additional sessions to reach target.
        r_squared          — R² of the linear fit (quality indicator).
        Both are None when there is insufficient data or slope ≤ 0.
    """
    if len(mastery_history) < 3:
        return None, None

    x = np.arange(len(mastery_history), dtype=float)
    y = np.array(mastery_history, dtype=float)

    slope, intercept = np.polyfit(x, y, 1)

    # A non-positive slope means mastery is flat or declining — the linear
    # model cannot project a future crossing of target_mastery.
    if slope <= 0:
        return None, None

    # R² — goodness of linear fit.
    y_pred  = slope * x + intercept
    ss_res  = float(np.sum((y - y_pred) ** 2))
    ss_tot  = float(np.sum((y - np.mean(y)) ** 2))
    r_squared = 1.0 - ss_res / ss_tot if ss_tot > 1e-9 else 0.0

    current = mastery_history[-1]
    if current >= target_mastery:
        return 0.0, r_squared

    # x* where the regression line crosses target_mastery.
    x_target = (target_mastery - intercept) / slope
    attempts_remaining = max(0.0, x_target - (len(mastery_history) - 1))

    return float(attempts_remaining), float(r_squared)
