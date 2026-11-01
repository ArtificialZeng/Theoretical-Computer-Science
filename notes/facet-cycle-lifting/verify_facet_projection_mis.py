"""Literal verification of the saved P19 counting certificate."""
import itertools
import json
from pathlib import Path

path = Path(__file__).with_name("facet-projection-MIS-obstruction.json")
data = json.loads(path.read_text())
n = 19
maximal = []
for mask in range(1 << n):
    chosen = {v for v in range(n) if mask & (1 << v)}
    if any(v + 1 in chosen for v in chosen):
        continue
    # A maximal independent set is exactly an independent dominating set.
    if all(v in chosen or v - 1 in chosen or v + 1 in chosen for v in range(n)):
        maximal.append(mask)
assert maximal == data["maximal_independent_sets"]
counts = [1, 1, 2]
for k in range(3, 41):
    counts.append(counts[k - 2] + counts[k - 3])
assert counts == data["recurrence_counts_n0_to40"]
assert counts[n] == len(maximal) == 200 > data["proper_connected_tubes"] == 189
assert all((a | b) & ((a | b) << 1) for a, b in itertools.combinations(maximal, 2))
print("Verified all 524288 masks by a separate set predicate, recurrence and all19900 incompatible pairs; original conjecture unresolved.")
