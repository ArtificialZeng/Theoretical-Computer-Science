"""Closed-form uniform-forecast candidate; exact arithmetic, no LP dependency.

Research artifact pending a new frozen-claim referee, not acceptance.
"""
from fractions import Fraction as F


def frontier(b):
    """Shared O(b)-size representation. Rows encode V=m+lambda*b+slope*r."""
    if b < 2:
        raise ValueError("b must be at least 2")
    a = b - 1
    m = F(b + 1, 2)
    z, A, C, W, rows = [], F(0), F(0), F(0), []
    term = F(1, a)
    upper = F(1)
    for j in range(1, b + 1):
        lam = F(b + j - 2, 2 * b)
        slope = W - lam * (b + C)
        d = F((b + 1 - j) * (b + j - 2), 2 * b)
        z.append(term)
        A += term
        C += (b + 1 - j) * term
        lower = F(b, b + C)
        rows.append({"j": j, "lower": lower, "upper": upper,
                     "lambda": lam, "intercept": m + lam * b,
                     "slope": slope, "A": A, "C": C})
        W += d * term
        upper = lower
        term *= F(b, a)
    return {"b": b, "m": m, "z": z, "segments": rows}


def policy(b, r, *, segment=None):
    """Query in O(b) arithmetic operations; r is R-1, not R."""
    r = F(r)
    data = frontier(b)
    if r < data["segments"][-1]["lower"]:
        raise ValueError("robustness below the classical minimum")
    if r > 1 or (r == 1 and segment is None):
        return {"policy": {b + 1: F(1)}, "lambda": F(0),
                "alpha": data["m"], "y": {}, "j": 0,
                "value": data["m"]}
    row = (data["segments"][segment - 1] if segment is not None else
           next(s for s in data["segments"] if s["lower"] <= r <= s["upper"]))
    if not row["lower"] <= r <= row["upper"]:
        raise ValueError("query outside selected segment")
    j = row["j"]
    Cprev = data["segments"][j - 2]["C"] if j > 1 else F(0)
    f = {i: r * data["z"][i - 1] for i in range(1, j)}
    f[j] = (b - r * (b + Cprev)) / (b + 1 - j)
    f[b + 1] = 1 - sum(f.values())
    f = {t: v for t, v in f.items() if v}
    lam, alpha = row["lambda"], row["intercept"]
    # Backward equality solve in O(b), using suffix sums.
    y, Y, X = {}, F(0), F(0)
    for i in range(j - 1, 0, -1):
        g = data["m"] + F((b + 1 - i) * (b + i - 2), 2 * b)
        y[i] = (alpha - g - lam * (i - 1) - (b - 1 + i) * Y + X) / (b - 1)
        Y += y[i]
        X += i * y[i]
    return {"policy": f, "lambda": lam, "alpha": alpha, "y": y,
            "j": j, "value": alpha + row["slope"] * r}
