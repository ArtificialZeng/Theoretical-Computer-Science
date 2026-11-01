"""Exact finite controls, not an asymptotic tightness certificate.

Run from project root: python3 evidence/check_clock_baseline.py
No truncation: all reachable subset transitions are explored to closure.
"""
from collections import Counter, deque
from math import lcm
from pathlib import Path
import json

JOB = "c015-imagebound-triage-104fc05d5d7d"


def image(mask, rows):
    result = 0
    for q, row in enumerate(rows):
        if mask & (1 << q):
            result |= row
    return result


def closure(seeds, letters):
    distance = {s: 0 for s in seeds}
    parent = {}
    queue = deque(distance)
    while queue:
        s = queue.popleft()
        for letter, rows in letters.items():
            t = image(s, rows)
            if t not in distance:
                distance[t] = distance[s] + 1
                parent[t] = (s, letter)
                queue.append(t)
    assert all(image(s, rows) in distance for s in distance
               for rows in letters.values())
    return distance, parent


def check(lengths):
    n = sum(lengths)
    starts, offset = [], 0
    for m in lengths:
        starts.append(offset)
        offset += m
    reset = sum(1 << s for s in starts)
    a, b = [], []
    for s, m in zip(starts, lengths):
        for j in range(m):
            a.append(1 << (s + (j + 1) % m))
            b.append(0 if j == m - 1 else reset)
    letters = {"a": a, "b": b}
    row_domain, _ = closure([1 << q for q in range(n)], letters)
    assert max(s.bit_count() for s in row_domain) <= len(lengths)
    distance, parent = closure([(1 << n) - 1], letters)
    assert 0 in distance
    word, s = [], 0
    while s in parent:
        s, letter = parent[s]
        word.append(letter)
    word = "".join(reversed(word))
    expected = "b" + "a" * (lcm(*lengths) - 1) + "b"
    assert distance[0] == lcm(*lengths) + 1
    s = (1 << n) - 1
    for letter in expected:
        s = image(s, letters[letter])
    assert s == 0
    return {
        "lengths": lengths, "n": n, "k": len(lengths),
        "transition_row_masks": letters,
        "all_word_row_domain_masks": sorted(row_domain),
        "row_closure_states": len(row_domain),
        "row_max_size": max(s.bit_count() for s in row_domain),
        "row_closure_edges_checked": len(row_domain) * len(letters),
        "global_subset_distances": {str(s): d for s, d in sorted(distance.items())},
        "global_closure_states": len(distance),
        "global_closure_edges_checked": len(distance) * len(letters),
        "global_distance_histogram": dict(sorted(Counter(distance.values()).items())),
        "shortest_mortal_length": distance[0], "bfs_witness": word,
        "formula_witness": expected, "complete": True,
    }


if __name__ == "__main__":
    results = [check(x) for x in [(3, 5), (2, 3, 5), (3, 4, 5), (5,)]]
    output = {"job_id": JOB, "scope": "Four explicit automata only", "results": results}
    Path("evidence/clock-baseline-results.json").write_text(json.dumps(output, indent=2) + "\n")
    for r in results:
        print({key: r[key] for key in ("lengths", "n", "row_max_size",
               "row_closure_states", "global_closure_states", "shortest_mortal_length")})
