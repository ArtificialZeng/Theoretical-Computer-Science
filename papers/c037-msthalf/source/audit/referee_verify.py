"""Fresh referee checks. Reads frozen inputs; writes only its own audit result.

Finite checks supplement the independently reconstructed written proof.
They do not establish its unbounded quantifiers or novelty.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json

PROJECT = Path(__file__).resolve().parents[1]
JOB = "c037-msthalf-referee-9071a36d85a3"


def verify_snapshot():
    snapshot = json.loads((PROJECT / "audit/snapshot.json").read_text())
    for name, digest in snapshot["files"].items():
        assert hashlib.sha256((PROJECT / name).read_bytes()).hexdigest() == digest, name
    digest = hashlib.sha256(json.dumps(snapshot["files"], sort_keys=True,
                                      separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    assert digest == snapshot["digest"]
    return snapshot


def metric_checks():
    saved = json.loads((PROJECT / "evidence/interval-packing-check.json").read_text())
    rectangles = costly_edges = peak_seen = triangles = 0
    for record in saved["records"]:
        d, w, r = record["d"], record["weights"], record["r"]
        n = len(d)
        assert len(w) == n - 1 and min(w) >= 0
        for i in range(n):
            assert d[i][i] == 0
            for j in range(n):
                assert d[i][j] == d[j][i]
                assert i == j or d[i][j] > 0
                for k in range(n):
                    assert d[i][j] <= d[i][k] + d[k][j]
                    triangles += 1
        positions = [sum(w[:i]) for i in range(n)]
        good = {(i, j) for i in range(n) for j in range(n)
                if i != j and d[i][j] <= abs(positions[i] - positions[j])}
        least = r * r
        for a in combinations(range(n), r):
            outside = tuple(v for v in range(n) if v not in a)
            # Fresh direct degree computation and explicit enumeration of B.
            counts = {v: sum((u, v) in good for u in a) for v in outside}
            for b in combinations(outside, r):
                least = min(least, sum(counts[v] for v in b))
                rectangles += 1
        assert least == record["minimum"] >= record["required"] > 0
        eta = Fraction(least, r * r)
        lengths = [d[i][i + 1] for i in range(n - 1)]
        intervals = [(Fraction(positions[i]) - Fraction(v, 64),
                      Fraction(positions[i]) + Fraction(v, 64))
                     for i, v in enumerate(lengths) if v > 64 * w[i]]
        ends = sorted({x for interval in intervals for x in interval})
        peak = max((sum(left <= x <= right for left, right in intervals)
                    for x in ends), default=0)
        integral = sum((b - a) * sum(left <= (a+b)/2 <= right
                                     for left, right in intervals)
                       for a, b in zip(ends, ends[1:]))
        assert integral == sum(right-left for left, right in intervals)
        ell = (2 * r * eta.denominator + eta.numerator - 1) // eta.numerator
        assert peak < 2 * (ell + r)
        assert peak <= Fraction(8 * r, 1) / eta
        # Kruskal, independently of the saved verifier's Prim implementation.
        parent = list(range(n))
        def find(v):
            while parent[v] != v:
                v = parent[v]
            return v
        mst = 0
        for length, i, j in sorted((d[i][j], i, j) for i in range(n) for j in range(i)):
            x, y = find(i), find(j)
            if x != y:
                parent[x] = y
                mst += length
        assert max(lengths) <= mst
        assert sum(lengths) <= Fraction(320*r, 1)/eta*sum(w) + Fraction(8*r, 1)/eta*mst
        costly_edges += len(intervals)
        peak_seen = max(peak_seen, peak)
    return dict(metric_witnesses=len(saved["records"]), metric_triangle_checks=triangles,
                disjoint_r_by_r_rectangles=rectangles,
                expensive_edges=costly_edges, largest_interval_overlap=peak_seen)


def repair_checks():
    # Use sets of marked pairs, explicit candidate order and line coordinates.
    # Unlike the frozen generator, directly sum two distances for each repair.
    total_masks = total_parameter_checks = 0
    probabilities = [Fraction(0), Fraction(1, 3), Fraction(2, 5), Fraction(49, 100)]
    records = []
    saved = json.loads((PROJECT / "evidence/interval-packing-check.json").read_text())
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        weights = [1, 100, 2, 10000, 3][:n-1]
        x = [sum(weights[:i]) for i in range(n)]
        by_count = defaultdict(lambda: [0, 0])
        for mask in range(1 << len(pairs)):
            marked = {pair for k, pair in enumerate(pairs) if (mask >> k) & 1}
            cost = 0
            success = True
            for i in range(n-1):
                if (i, i+1) not in marked:
                    cost += weights[i]
                    continue
                candidates = [v for v in range(n) if v not in (i, i+1)
                              and tuple(sorted((i, v))) not in marked
                              and tuple(sorted((i+1, v))) not in marked]
                if not candidates:
                    success = False
                    break
                v = sorted(candidates, key=lambda v: (min(abs(v-i), abs(v-i-1)), v))[0]
                cost += abs(x[v]-x[i]) + abs(x[v]-x[i+1])
            bucket = by_count[len(marked)]
            if success:
                bucket[1] += cost
            else:
                bucket[0] += 1
            total_masks += 1
        checks = []
        for p in probabilities:
            failure = sum(fail*p**k*(1-p)**(len(pairs)-k)
                          for k, (fail, cost) in by_count.items())
            expected = sum(cost*p**k*(1-p)**(len(pairs)-k)
                           for k, (fail, cost) in by_count.items())
            alpha = (1-p)**2
            assert failure <= (n-1)*(1-alpha)**(n-2)
            assert expected <= (1+4/alpha)*sum(weights)
            old = saved["repair_masks"][n-2]["checks"][probabilities.index(p)]
            assert failure == Fraction(old["failure"])
            assert expected == Fraction(old["expected_walk_cost_on_F"])
            total_parameter_checks += 1
            checks.append(dict(p=str(p), failure=str(failure), expected_walk_cost_on_F=str(expected)))
        records.append(dict(n=n, masks=1 << len(pairs), checks=checks))
    return dict(masks=total_masks, parameter_checks=total_parameter_checks, results=records)


def arithmetic_checks():
    # Exact boundary checks complement the analytic inequalities in math.md.
    count = 0
    for r in range(1, 31):
        for eta in [Fraction(1), Fraction(3, 4), Fraction(1, 2), Fraction(1, 7), Fraction(1, 1000)]:
            ell = (2*r*eta.denominator + eta.numerator-1)//eta.numerator
            assert eta*(2*ell-1) >= r
            assert 2*(ell+r) <= 8*r/eta
            assert 64 + 256*r/eta <= 320*r/eta
            count += 1
    return dict(exact_constant_checks=count)


if __name__ == "__main__":
    snapshot = verify_snapshot()
    result = dict(job_id=JOB, snapshot_digest=snapshot["digest"],
                  arithmetic="exact integers and rational numbers",
                  saved_metrics=metric_checks(), repair=repair_checks(),
                  constants=arithmetic_checks(),
                  limitations=["Saved metric families are finite samples, not exhaustive.",
                               "Repair masks are exhaustive only for n=2,...,6 at four rational p values.",
                               "The universal theorem is assessed by its written proof, not these tests."])
    verify_snapshot()
    (PROJECT / "audit/referee-verification.json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({k: v for k, v in result.items() if k != "repair"} | {
        "repair_masks": result["repair"]["masks"],
        "repair_parameter_checks": result["repair"]["parameter_checks"]}))
