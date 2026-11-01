#!/usr/bin/env python3
"""Exact finite checks for a known n=2 obstruction; standard library only."""
import hashlib
import itertools
import json
from pathlib import Path


def optimum(edges):
    return max(
        len(es)
        for k in range(len(edges) + 1)
        for es in itertools.combinations(edges, k)
        if len({e[0] for e in es}) == len(es)
        and len({e[1] for e in es}) == len(es)
    )


def maximum_degree(edges):
    return max(sum(z in e for e in edges) for z in ("a", "b", "x", "y"))


def best_completion(first, second_neighbor):
    used = set() if first is None else {first}
    return int(first is not None) + int(second_neighbor not in used)


def main():
    graphs = {
        "good": [("a", "x"), ("b", "x"), ("b", "y")],
        "bad": [("a", "x"), ("b", "x"), ("a", "y")],
    }
    advice = {("a", "x"), ("b", "y")}
    checked = {}
    for name, edges in graphs.items():
        checked[name] = {
            "maximum_degree_both_sides": maximum_degree(edges),
            "optimum": optimum(edges),
            "advice_contained_in_graph": advice <= set(edges),
        }
        assert maximum_degree(edges) == 2 and optimum(edges) == 2
    rows = []
    for first in ("a", "b", None):
        good = best_completion(first, "b")
        bad = best_completion(first, "a")
        assert good + bad <= 3
        rows.append({"first_action": first, "best_good": good,
                     "best_bad": bad, "sum": good + bad})
    root = Path(__file__).resolve().parents[1]
    actual_hash = hashlib.sha256((root / "source.md").read_bytes()).hexdigest()
    assert actual_hash == "3ec230456a31ba9b004000be9e79c74a77636a28a31e9b4eec31918f5ab305ed"
    print(json.dumps({
        "job_id": "advice-matching-triage-5cc2f73291d9",
        "scope": "n=2 graph checks and three deterministic first-action continuation bounds",
        "graphs": checked, "first_action_rows": rows,
        "randomized_extension": "Affine inequality holds for every convex combination; see known-obstruction.md",
        "source_sha256": actual_hash,
        "novel_contribution": False,
    }, indent=2))


if __name__ == "__main__":
    main()
