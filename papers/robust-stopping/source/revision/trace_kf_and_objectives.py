"""Exact traces of the KF26 support prescription and two objective optima.

No claim that inconsistent published pseudocode has a unique executable output.
The corrected-index trace uses the source cost and KF26 Lemma 5.1 moment.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent


def cost(b, p, t):
    return sum(v * (b + t - 1 if t <= x else x) for x, v in p.items())


def feasible(b, r, f):
    return (sum(f.values()) == 1 and min(f.values()) >= 0
            and all(sum((b - 1 + t - x) * v for t, v in f.items() if t <= x) <= r * x
                    for x in range(1, b))
            and sum((t - 1) * v for t, v in f.items()) <= r * b)


def check_bound(b, p, lam, alpha, equal_days):
    # For both examples p is on 1,2: g is constant for all t>=3.
    assert set(p) == {1, 2} and lam > 0
    for t in range(1, 4):
        slack = cost(b, p, t) + lam * (t - 1) - alpha
        assert slack >= 0 and (slack == 0) == (t in equal_days)
    # Beyond 3 the slack increases by lam each day: this is the infinite check.


def main():
    b, r = 3, F(1, 2)
    p = {1: F(2, 5), 2: F(3, 5)}
    levels = []
    for h in (F(3, 2), F(8, 5), F(2), F(14, 5), F(29, 10)):
        allowed_prefix = [t for t in (1, 2) if cost(b, p, t) <= h]
        f, mass, mu = {}, F(0), F(0)
        updates = []
        for t in allowed_prefix:
            # D.3-D.4 tight prefix/gap update, in the source's (t-1) convention.
            atom = (r * t - mu - (b - t) * mass) / (b - 1)
            f[t] = atom
            mass += atom
            mu += (t - 1) * atom
            updates.append({"day": t, "atom": atom, "F": mass, "mu": mu})
        remaining = 1 - mass
        first_allowed_tail = 3 if cost(b, p, 3) <= h else None
        budget = r * b - mu
        possible = (first_allowed_tail is not None and
                    remaining * (first_allowed_tail - 1) <= budget)
        if possible:
            f[first_allowed_tail] = remaining
            assert feasible(b, r, f)
        levels.append({"h": h, "allowed_prefix": allowed_prefix,
                       "updates": updates, "remaining_mass": remaining,
                       "remaining_moment_budget": budget,
                       "first_allowed_tail": first_allowed_tail,
                       "tail_required_moment": None if first_allowed_tail is None else remaining * 2,
                       "feasible": possible, "policy_if_feasible": f if possible else None,
                       "expected_cost_if_feasible": sum(cost(b, p, t) * v for t, v in f.items()) if possible else None})
    threshold = F(14, 5)
    at = next(v for v in levels if v["h"] == threshold)
    assert at["policy_if_feasible"] == {2: F(1, 2), 3: F(1, 2)}
    assert at["expected_cost_if_feasible"] == F(11, 5)
    global_f = {1: F(1, 4), 3: F(3, 4)}
    assert feasible(b, r, global_f)
    check_bound(b, p, F(7, 10), F(3), {1, 3})
    assert sum(cost(b, p, t) * v for t, v in global_f.items()) == F(39, 20)
    assert F(3) - F(7, 10) * r * b == F(39, 20)
    # Literal Algorithm 3 tail candidates are forecast atoms dj>=b; here none.
    literal_candidates = [d for d in p if d >= b]
    assert literal_candidates == []
    # Its lines 11-16 on the singleton active interval s=e=2:
    atom = r * 2 / (b - 1)
    mu_after_line12 = atom * 2
    F_after_line15 = (atom + r) * F(b, b - 1) ** 0 - r
    mu_after_line16 = r * 2 - (b - 2) * F_after_line15
    assert (atom, mu_after_line12, mu_after_line16) == (F(1, 2), F(1), F(1, 2))

    p2 = {1: F(1, 2), 2: F(1, 2)}
    ratio_weights = {x: v / min(x, b) for x, v in p2.items()}
    fcost, fratio = global_f, {2: F(1, 2), 3: F(1, 2)}
    assert feasible(b, r, fcost) and feasible(b, r, fratio)
    check_bound(b, p2, F(3, 4), F(3), {1, 3})
    check_bound(b, ratio_weights, F(1, 2), F(2), {2, 3})
    Jcost = sum(cost(b, p2, t) * v for t, v in fcost.items())
    Jratio = sum(cost(b, p2, t) * v for t, v in fratio.items())
    Qcost = sum(cost(b, ratio_weights, t) * v for t, v in fcost.items())
    Qratio = sum(cost(b, ratio_weights, t) * v for t, v in fratio.items())
    assert (Jcost, Jratio, Qcost, Qratio) == (F(15, 8), F(2), F(21, 16), F(5, 4))
    assert Jcost == 3 - F(3, 4) * r * b
    assert Qratio == 2 - F(1, 2) * r * b
    result = {"job_id": "robust-stopping-research-cd75b220d422", "status": "passed",
              "KF26_target": "arXiv:2603.29233v1, Appendix D.2, eq. (26), Algorithms 2 and 3",
              "support_threshold": threshold, "support_threshold_policy_is_forced": at["policy_if_feasible"],
              "threshold_prescription_cost": F(11, 5), "true_expected_optimum": F(39, 20),
              "threshold_prescription_trace": levels,
              "literal_algorithm3_singleton_trace": {"s": 2, "e": 2, "line11_atom": atom,
                  "line12_mu": mu_after_line12, "line15_F": F_after_line15,
                  "line16_mu": mu_after_line16, "line26_tail_candidates": literal_candidates},
              "literal_algorithm3_output": "not asserted: no dj>=b in its written tail loop; zero-slope tail and indexing require conventions not supplied",
              "normalization_example": {"b": b, "R": 1 + r, "p": p2,
                  "cost_policy": fcost, "cost_minimum": Jcost,
                  "cost_certificate": {"lambda": F(3, 4), "alpha": 3, "y": {}},
                  "ratio_policy": fratio, "ratio_minimum": Qratio,
                  "ratio_certificate": {"lambda": F(1, 2), "alpha": 2, "y": {}},
                  "ratio_at_cost_policy": Qcost, "cost_at_ratio_policy": Jratio},
              "infinite_tail_check": "For t>=3 the objective coefficients are constant; reduced costs increase by the strictly positive lambda at each later integer."}
    path = ROOT / "revision/kf-and-objective-checks.json"
    path.write_text(json.dumps(result, default=str, indent=2) + "\n")
    print(json.dumps({"status": "passed", "minimum_support_level": str(threshold),
                      "prescription_J": "11/5", "global_J": "39/20",
                      "literal_Algorithm3_unique_output_asserted": False,
                      "objective_normalization_certificates": "passed"}, indent=2))


if __name__ == "__main__":
    main()
