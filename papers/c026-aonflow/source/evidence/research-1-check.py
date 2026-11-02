#!/usr/bin/env python3
"""Exact bounded checks of N and NR's counting/demand algebra, not an AON solver."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json
import random
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SOURCE = "7241936e887e814eebe18f891cfe9d90c883ee0298057dfc8bbdd2344501e29e"


def ceil_q(x):
    return -(-x.numerator // x.denominator)


def normalize(weights):
    total = sum(weights, Q(0))
    support = sum(w > 0 for w in weights)
    assert total > 0
    q = Q(support) / total
    rounded = [ceil_q(q * w) if w else 0 for w in weights]
    assert all(q * w <= b for w, b in zip(weights, rounded))
    assert support <= sum(rounded) <= 2 * support
    assert Q(sum(rounded)) / q <= 2 * total
    assert all(0 <= b <= support + 1 for b in rounded)
    return q, rounded


def normalization_checks():
    # Entire stated finite grid, plus strongly skewed denominators. No graph domain
    # is enumerated, and these tests do not certify the decomposition theorem.
    grid = [Q(0), Q(1), Q(1, 2), Q(1, 3), Q(1, 7), Q(1, 2**80)]
    count = 0
    max_q_bits = 0
    for size in range(1, 6):
        for row in product(grid, repeat=size):
            if not any(row):
                continue
            q, rounded = normalize(row)
            max_q_bits = max(max_q_bits, q.numerator.bit_length(), q.denominator.bit_length())
            # Adding arbitrary zero-weight Steiner vertices does not affect N.
            assert normalize(row + (Q(0),) * 50) == (q, rounded + [0] * 50)
            count += 1
    return {"cases": count, "sizes": [1, 5], "grid": [str(x) for x in grid],
            "max_observed_q_integer_bit_length": max_q_bits,
            "zero_weight_padding_per_case": 50}


def cluster_counting_checks():
    # Synthetic cluster incidence systems, not graph/pseudocenter constructions.
    # Owned endpoint masses are grouped in [1, 3/2), leaving <1 uncovered mass.
    rng = random.Random(20261102)
    count = 0
    min_selected = None
    largest_pair_mass = Q(0)
    for npairs in [4, 8, 16, 32, 64, 96]:
        for case in range(40):
            masses = [rng.choice([Q(1, 2), Q(1, 3), Q(1, 5), Q(1, 7), Q(1, 2**40)])
                      for _ in range(npairs)]
            endpoints = [(i, side) for i in range(npairs) for side in [0, 1]]
            rng.shuffle(endpoints)
            owner, cluster_mass = {}, []
            pending, running = [], Q(0)
            for endpoint in endpoints:
                pending.append(endpoint)
                running += masses[endpoint[0]]
                if running >= 1:
                    cluster = len(cluster_mass)
                    assert 1 <= running < 2
                    cluster_mass.append(running)
                    for u in pending:
                        owner[u] = cluster
                    pending, running = [], Q(0)
            uncovered = running
            assert uncovered < 1
            eligible = [i for i in range(npairs) if (i, 0) in owner and (i, 1) in owner]
            eligible_mass = sum((masses[i] for i in eligible), Q(0))
            pair_total = sum(masses, Q(0))
            assert eligible_mass >= pair_total - uncovered
            order = list(eligible)
            rng.shuffle(order)
            unused = set(range(len(cluster_mass)))
            selected = []
            for i in order:
                cs = {owner[(i, 0)], owner[(i, 1)]}
                if cs <= unused:
                    selected.append(i)
                    unused -= cs
            # Every removed pair is charged to a selected pair's <=2 clusters.
            assert 4 * len(selected) >= eligible_mass
            assert 4 * len(selected) >= pair_total - 1
            count += 1
            min_selected = len(selected) if min_selected is None else min(min_selected, len(selected))
            largest_pair_mass = max(largest_pair_mass, pair_total)
    return {"cases": count, "seed": 20261102, "pair_counts": [4, 8, 16, 32, 64, 96],
            "minimum_selected_observed": min_selected,
            "largest_total_pair_mass_observed": str(largest_pair_mass),
            "limitation": "Only the initial weighted cluster-counting inequality; no tagging or pseudocenter implementation."}


def reservoir_checks():
    rng = random.Random(20261103)
    cases = 0
    diagonal_cases = 0
    for nvertices in [2, 3, 5, 8]:
        for npairs in [1, 2, 4, 8]:
            for _ in range(20):
                vectors = []
                for _ in range(2 * npairs):
                    entries = [rng.randrange(0, 12) for _ in range(nvertices)]
                    if not any(entries):
                        entries[0] = 1
                    total = sum(entries)
                    vectors.append([Q(e, total) for e in entries])
                rho = [sum((vec[v] for vec in vectors), Q(0)) for v in range(nvertices)]
                demand = {}
                for u in range(nvertices):
                    for v in range(u + 1, nvertices):
                        demand[u, v] = sum((vectors[2*i][u] * vectors[2*i+1][v]
                                          + vectors[2*i][v] * vectors[2*i+1][u]
                                          for i in range(npairs)), Q(0))
                for v in range(nvertices):
                    marginal = sum((val for pair, val in demand.items() if v in pair), Q(0))
                    diagonal = sum((vectors[2*i][v] * vectors[2*i+1][v]
                                    for i in range(npairs)), Q(0))
                    assert marginal == rho[v] - 2 * diagonal
                    assert marginal <= rho[v]
                    diagonal_cases += diagonal > 0
                cases += 1
    return {"cases": cases, "seed": 20261103,
            "vertex_counts": [2, 3, 5, 8], "pair_counts": [1, 2, 4, 8],
            "positive_diagonal_vertex_cases": diagonal_cases,
            "limitation": "Checks demand algebra only; assumes spreading distributions already exist."}


def main():
    source_digest = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
    assert source_digest == EXPECTED_SOURCE
    result = {
        "job_id": "c026-aonflow-research-4dc78c591460",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "arithmetic": "fractions.Fraction exact rational arithmetic",
        "normalization": normalization_checks(),
        "weighted_initial_selection": cluster_counting_checks(),
        "reservoir_demand": reservoir_checks(),
        "source_sha256": source_digest,
        "source_unchanged": True,
        "all_checks_passed": True,
        "original_status": "unresolved",
        "limits": ["No exhaustive graph search", "No AON approximation implementation",
                   "No proof of nonuniform pseudocenter/tagging refinement",
                   "Finite checks supplement the algebraic proofs; they do not settle the original question"]
    }
    dest = ROOT / "evidence/research-1-check-results.json"
    dest.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
