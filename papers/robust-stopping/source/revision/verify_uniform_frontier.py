"""Adversarial finite checks, direct costs and small exact vertex enumeration.

The analytic proof, not the finite range, establishes quantified claims.
Run from any directory; prints JSON and writes only its own evidence output.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib
import importlib.util
import json
import random
from uniform_frontier import frontier, policy

ROOT = Path(__file__).resolve().parent.parent


def solve(A, rhs):
    n = len(rhs)
    M = [[F(v) for v in row] + [F(v)] for row, v in zip(A, rhs)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if M[i][col]), None)
        if pivot is None:
            return None
        M[col], M[pivot] = M[pivot], M[col]
        d = M[col][col]
        M[col] = [x / d for x in M[col]]
        for i in range(n):
            if i != col and M[i][col]:
                d = M[i][col]
                M[i] = [u - d * v for u, v in zip(M[i], M[col])]
    return tuple(row[-1] for row in M)


def enumerate_optimum(b, r, costs):
    # All vertices of the finite law on 1,...,b+1. Independent of oracle.
    n = b + 1
    inequalities = []
    for x in range(1, b):
        inequalities.append(([b - 1 + t - x if t <= x else 0
                              for t in range(1, n + 1)], r * x))
    inequalities.append((list(range(n)), r * b))
    for i in range(n):
        inequalities.append(([-int(k == i) for k in range(n)], F(0)))
    best, minimizers, feasible = None, set(), set()
    for chosen in combinations(inequalities, n - 1):
        f = solve([[1] * n] + [row for row, _ in chosen],
                  [1] + [bound for _, bound in chosen])
        if f is None or f in feasible:
            continue
        if not all(sum(a * v for a, v in zip(row, f)) <= bound
                   for row, bound in inequalities):
            continue
        feasible.add(f)
        value = sum(c * v for c, v in zip(costs, f))
        if best is None or value < best:
            best, minimizers = value, {f}
        elif value == best:
            minimizers.add(f)
    return best, minimizers, len(feasible)


def direct_cost(b, t):
    return sum(F(b + t - 1 if t <= x else x, b) for x in range(1, b + 1))


def check(b, r, segment=None):
    out = policy(b, r, segment=segment)
    f, lam, alpha, y = (out[k] for k in ("policy", "lambda", "alpha", "y"))
    assert sum(f.values()) == 1 and min(f.values()) > 0
    assert lam >= 0 and all(v > 0 for v in y.values())
    assert all(sum((b - 1 + t - x) * v for t, v in f.items() if t <= x) <= r * x
               for x in range(1, b))
    mu = sum((t - 1) * v for t, v in f.items())
    assert mu <= r * b
    if r <= 1:
        assert mu == r * b
    J = sum(direct_cost(b, t) * v for t, v in f.items())
    assert J == out["value"] == alpha - r * sum(x * v for x, v in y.items()) - lam * r * b
    j = out["j"]
    for t in range(1, b + 6):
        reduced = direct_cost(b, t) + lam * (t - 1) - alpha + sum(
            (b - 1 + t - x) * v for x, v in y.items() if x >= t)
        assert reduced >= 0
        if t in f:
            assert reduced == 0
        if j and (j < t <= b or t > b + 1):
            assert reduced > 0
    return out


def main():
    rng = random.Random(20261031)
    summary, certificate_examples = [], []
    total = alternate_endpoints = comparisons = vertex_cases = vertex_count = 0
    spec = importlib.util.spec_from_file_location("previous_oracle", ROOT / "evidence/prefix_oracle.py")
    old = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    for b in list(range(2, 26)) + [41, 79, 101]:
        data = frontier(b)
        a = b - 1
        rows = data["segments"]
        assert rows[-1]["lower"] == F(a ** b, b ** b - a ** b)
        assert rows[0]["slope"] == -F(b - 1, 2)
        for i, row in enumerate(rows, 1):
            q = F(b, a) ** i
            assert row["A"] == q - 1
            assert row["C"] == (2 * b - i) * q - 2 * b
            assert sum((k - 1) * data["z"][k - 1] for k in range(1, i + 1)) == b - (b - i) * q
            assert row["lower"] < row["upper"]
            if i < b:
                assert rows[i]["slope"] - row["slope"] == -(b + row["C"]) / (2 * b)
        indices = range(1, b + 1) if b <= 25 else sorted({1, 2, b // 3, b // 2, b - 1, b})
        probes = {F(1), F(5, 4), F(11, 3)}
        for j in indices:
            row = rows[j - 1]
            # Both endpoint formulas, thirds (not seed midpoints), and random rational interior.
            for r in (row["lower"], row["upper"]):
                one = check(b, r, j)
                assert one["policy"] == check(b, r)["policy"]
                total += 1
                alternate_endpoints += 1
            for theta in (F(1, 3), F(2, 3), F(rng.randint(1, 996), 997)):
                probes.add(row["lower"] + theta * (row["upper"] - row["lower"]))
            probes.update((row["lower"], row["upper"]))
        for r in sorted(probes):
            out = check(b, r)
            total += 1
            if b <= 9:
                prior = old.optimize(b, 1 + r, {i: F(1, b) for i in range(1, b + 1)})
                assert prior["policy"] == out["policy"] if r <= 1 else True
                assert sum(direct_cost(b, t) * v for t, v in prior["policy"].items()) == out["value"]
                comparisons += 1
            if b <= 5 and r <= 1:
                J, vs, nv = enumerate_optimum(b, r, [direct_cost(b, t) for t in range(1, b + 2)])
                assert J == out["value"] and len(vs) == 1
                assert next(iter(vs)) == tuple(out["policy"].get(t, F(0)) for t in range(1, b + 2))
                vertex_cases += 1
                vertex_count += nv
        r = (rows[-1]["lower"] + rows[-1]["upper"]) / 2
        sharp = check(b, r)
        assert len(sharp["policy"]) == b + 1
        assert sum(t >= b for t in sharp["policy"]) == 2
        summary.append({"b": b, "segments": b + 1, "sharp_r": str(r),
                        "sharp_support": len(sharp["policy"])})
        if b in (2, 3, 9, 25, 101):
            certificate_examples.append({"b": b, "r": str(r), **sharp})
    example = check(3, F(9, 20))
    assert example["value"] == F(221, 80)
    result = {"job_id": "robust-stopping-research-cd75b220d422", "status": "passed",
              "exact_certificate_cases": total, "alternate_segment_endpoint_checks": alternate_endpoints,
              "previous_optimizer_comparisons": comparisons, "exhaustive_vertex_instances": vertex_cases,
              "feasible_vertices_checked": vertex_count, "families": summary,
              "certificates": certificate_examples,
              "source_sha256": hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest(),
              "limits": "Finite checks only; global tail inequalities, uniqueness and all-b formulas require the analytic proof. This worker is the proposer, not a fresh referee."}
    path = ROOT / "revision/uniform-frontier-verification.json"
    path.write_text(json.dumps(result, default=str, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k not in ("families", "certificates")}, indent=2))


if __name__ == "__main__":
    main()
