"""Exact, dependency-free checks for the marked-palindrome manuscript.

Run from stoc2: python3 research/code/verify.py
All reported counts are measured; no simulated compiler benchmark results.
"""
import csv
import itertools
import json
import pathlib
import random
import time
from functools import lru_cache

ROOT = pathlib.Path(__file__).resolve().parents[2]


def words(alphabet, maximum):
    for n in range(maximum + 1):
        for w in itertools.product(alphabet, repeat=n):
            yield ''.join(w)


def ed(a, b):
    row = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        nxt = [i]
        for j, y in enumerate(b, 1):
            nxt.append(min(nxt[-1]+1, row[j]+1, row[j-1]+(x != y)))
        row = nxt
    return row[-1]


def interval(s, alphabet='ab', witness=False):
    """Quadratic interval oracle, retaining a shortest repaired word."""
    @lru_cache(None)
    def go(i, j):
        if i == j:
            return 1, '#'
        if i + 1 == j:
            return int(s[i] != '#'), '#'
        candidates = []
        c, w = go(i+1, j)
        candidates.append((1+c, w))
        c, w = go(i, j-1)
        candidates.append((1+c, w))
        c, w = go(i+1, j-1)
        for a in alphabet:
            candidates.append((c+(s[i] != a)+(s[j-1] != a), a+w+a))
        return min(candidates)
    value = go(0, len(s))
    return value if witness else value[0]


def frontier(s, k, alphabet='ab'):
    """Landau--Vishkin frontier. Direct scans stand in for an LCE oracle.

    Number of extensions is quadratic in k. Scan time is NOT used to claim
    a near-linear implementation; the proof uses a suffix index.
    """
    n = len(s)
    levels = []
    queries = 0
    def extend(i, j):
        nonlocal queries
        queries += 1
        while i+j+1 < n and s[i] == s[n-1-j] and s[i] in alphabet:
            i += 1
            j += 1
        return i
    def finish(i, j):
        remaining = n-i-j
        if remaining == 0:
            return 1
        if remaining == 1:
            return int(s[i] != '#')
        return None
    for budget in range(k+1):
        layer = {}
        for delta in range(-budget, budget+1):
            candidates = []
            if budget == 0 and delta == 0:
                candidates.append(0)
            if budget:
                previous = levels[budget-1]
                if delta in previous:
                    candidates.append(previous[delta])
                # Delete left: predecessor diagonal delta-1.
                if delta-1 in previous:
                    i = previous[delta-1]
                    j = i-(delta-1)
                    if i+j < n:
                        candidates.append(i+1)
                # Delete right: predecessor diagonal delta+1.
                if delta+1 in previous:
                    i = previous[delta+1]
                    j = i-(delta+1)
                    if i+j < n:
                        candidates.append(i)
            for cost in (1, 2):
                if budget < cost or delta not in levels[budget-cost]:
                    continue
                i = levels[budget-cost][delta]
                j = i-delta
                if i+j+1 < n:
                    pair = min((s[i] != a)+(s[n-1-j] != a) for a in alphabet)
                    if pair <= cost:
                        candidates.append(i+1)
            candidates = [i for i in candidates if 0 <= i <= n and 0 <= i-delta and 2*i-delta <= n]
            if candidates:
                i = extend(max(candidates), max(candidates)-delta)
                layer[delta] = i
                final = finish(i, i-delta)
                if final is not None and budget+final <= k:
                    # Return a feasible upper bound; stop only at this budget
                    # when center is free. Paid centers may be improved later.
                    pass
        levels.append(layer)
    best = min((e+f for e, layer in enumerate(levels)
                for d, i in layer.items()
                for f in [finish(i, i-d)] if f is not None), default=k+1)
    return (best if best <= k else k+1), queries


def brute_language(s, alphabet='ab'):
    """Independent finite-language oracle. An incumbent cost <= len(s)
    bounds candidate length, so no longer candidate can improve it."""
    incumbent = ed(s, '#')
    result = incumbent
    max_half = (len(s)+incumbent-1)//2
    for half in words(alphabet, max_half):
        result = min(result, ed(s, half+'#'+half[::-1]))
    return result


def main():
    started = time.perf_counter()
    counts = {'interval_vs_language': 0, 'frontier_thresholds': 0,
              'guarded_reduction': 0, 'random_frontier_thresholds': 0}
    for s in words('ab#', 6):
        assert interval(s) == brute_language(s), s
        counts['interval_vs_language'] += 1
    for s in words('ab#', 9):
        truth = interval(s)
        for k in range(min(len(s)+1, 5)+1):
            answer, _ = frontier(s, k)
            assert answer == min(truth, k+1), (s, k, truth, answer)
            counts['frontier_thresholds'] += 1
    inputs = list(words('ab', 4))
    for u in inputs:
        for v in inputs:
            m = 4*max(len(u), len(v), 1)+1
            x = u+'c'*m+'#'+'c'*m+v[::-1]
            assert interval(x, 'abc') == ed(u, v), (u, v)
            counts['guarded_reduction'] += 1
    rng = random.Random(20261031)
    for _ in range(500):
        half = ''.join(rng.choice('abc') for _ in range(rng.randrange(5, 60)))
        x = half+'#'+half[::-1]
        for _ in range(rng.randrange(0, 8)):
            pos = rng.randrange(len(x)+1)
            op = rng.randrange(3)
            if op == 0: x = x[:pos]+rng.choice('abc#')+x[pos:]
            elif pos < len(x):
                x = x[:pos]+(rng.choice('abc#') if op == 1 else '')+x[pos+1:]
        truth = interval(x, 'abc')
        for k in (0, 1, 2, 4, 8):
            answer, _ = frontier(x, k, 'abc')
            assert answer == min(truth, k+1), (x, k, truth, answer)
            counts['random_frontier_thresholds'] += 1
    u, v = 'aaabbb', 'bbbaaa'
    x = u+'#'+v[::-1]
    dist, repaired = interval(x, witness=True)
    assert ed(x, repaired) == dist == 5 and ed(u, v) == 6
    result = {'counts': counts, 'counterexample': {'u': u, 'v': v,
              'input': x, 'ed': ed(u, v), 'led': dist, 'repair': repaired},
              'seed': 20261031, 'wall_seconds': time.perf_counter()-started}
    out = ROOT/'research'/'results'/'verification.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
