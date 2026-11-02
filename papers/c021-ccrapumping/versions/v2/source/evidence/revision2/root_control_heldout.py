#!/usr/bin/env python3
"""Held-out ternary-control/UT4 diagnostics, not a fresh theorem audit."""
from collections import deque
from fractions import Fraction as F
from itertools import combinations, product
import json
from math import factorial
from pathlib import Path
import random
from root_scattered_check import invariant_basis


def eye(d):
    return [[F(int(i == j)) for j in range(d)] for i in range(d)]


def mul(a, b):
    return [[sum((x * y for x, y in zip(r, c)), F(0))
             for c in zip(*b)] for r in a]


def power(a, n):
    r = eye(len(a))
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r


def root(a, exponent):
    d = len(a)
    z = [[x - y for x, y in zip(r, s)] for r, s in zip(a, eye(d))]
    assert power(z, d) == [[0] * d for _ in range(d)]
    ans, term, c = eye(d), eye(d), F(1)
    for j in range(1, d):
        term = mul(term, z)
        c *= (exponent - j + 1) / j
        ans = [[x + c * y for x, y in zip(r, s)] for r, s in zip(ans, term)]
    return ans


def compose(a, b):
    # Read transformation a, then b.
    return tuple(b[x] for x in a)


def reach(start, transitions):
    seen, pending = {start: ()}, deque([start])
    while pending:
        q = pending.popleft()
        for a, t in enumerate(transitions):
            if t[q] not in seen:
                seen[t[q]] = seen[q] + (a,)
                pending.append(t[q])
    return seen


M = [eye(4) for _ in range(3)]
for a in range(3):
    M[a][a][a+1] = F(1)


def word_matrix(w):
    ans = eye(4)
    for a in w:
        ans = mul(ans, M[a])
    return ans


class BlockWA:
    def __init__(self, matrices, prefix):
        self.dim, self.alphabet, self.matrices = 4, tuple(map(str, range(len(matrices)))), matrices
        self.initial, self.final = word_matrix(prefix)[0], [F(0), F(0), F(0), F(1)]

    def row_step(self, row, a):
        return mul([row], self.matrices[int(a)])[0]

    def col_step(self, col, a):
        return [r[0] for r in mul(self.matrices[int(a)], [[x] for x in col])]


def verify(transitions):
    n = len(transitions[0])
    paths = [reach(q, transitions) for q in range(n)]
    components = {frozenset(v for v in range(n) if v in paths[q] and q in paths[v])
                  for q in range(n)}
    C = min((c for c in components if c <= paths[0].keys()
             and all(t[q] in c for t in transitions for q in c)), key=lambda c: tuple(sorted(c)))
    states = sorted(C)
    rename = {q: i for i, q in enumerate(states)}
    ts = [tuple(rename[t[q]] for q in states) for t in transitions]
    s = len(states)
    identity = tuple(range(s))
    semigroup, pending = {identity: ()}, deque([identity])
    while pending:
        f = pending.popleft()
        for a, t in enumerate(ts):
            g = compose(f, t)
            if g not in semigroup:
                semigroup[g] = semigroup[f] + (a,)
                pending.append(g)
    t = min(semigroup, key=lambda z: (len(set(z)), len(semigroup[z]), semigroup[z]))
    r, eword = len(set(t)), semigroup[t]
    N = factorial(r)
    E = identity
    for _ in range(N):
        E = compose(E, t)
    R = set(E)
    assert len(R) == r and all(E[q] == q for q in R)
    base = power(word_matrix(eword), N)
    inverse = root(base, F(-1))
    blocks = [base]
    for a, generator in enumerate(ts):
        T = compose(compose(E, generator), E)
        assert set(T) == R and {T[q] for q in R} == R
        returning = identity
        for _ in range(N):
            returning = compose(returning, T)
        assert all(returning[q] == q for q in R)
        U = mul(mul(base, M[a]), base)
        B = power(U, N)
        recovered = root(B, F(1, N))
        assert recovered == U
        assert mul(mul(inverse, recovered), inverse) == M[a]
        blocks.append(B)
    q = states[min(R)]
    prefix = paths[0][q]
    wa = BlockWA(blocks, prefix)
    assert len(invariant_basis(wa)) == len(invariant_basis(wa, True)) == 4
    assert any(mul(a, b) != mul(b, a) for a, b in combinations(blocks, 2))
    return s, r, len(semigroup)


def main():
    rng = random.Random(20261103)
    controls = []
    for n in (1, 2):
        for flat in product(range(n), repeat=3*n):
            controls.append(([flat[a*n:(a+1)*n] for a in range(3)], 'exhaustive_ternary_n_le2'))
    for n in (3, 4, 5):
        for _ in range(24):
            controls.append(([tuple(rng.randrange(n) for _ in range(n)) for a in range(3)], 'seeded_ternary_n3to5'))
        # Permutation groups exercise nontrivial minimum control ranks.
        for _ in range(8):
            rows = []
            for a in range(3):
                row = list(range(n))
                rng.shuffle(row)
                rows.append(tuple(row))
            controls.append((rows, 'seeded_permutation_controls'))
    report = dict(scope='Held-out exact diagnostics for the unaccepted finite-control theorem; not a fresh referee verdict.',
                  seed=20261103, controls=len(controls), families={}, ranks={},
                  max_control_semigroup=0, full_block_minimal_dimension=4,
                  weighted_letters='I4+E12,I4+E23,I4+E34 (row convention)', mismatches=[])
    for ts, family in controls:
        s, r, size = verify(ts)
        report['families'][family] = report['families'].get(family, 0) + 1
        key = str((s, r))
        report['ranks'][key] = report['ranks'].get(key, 0) + 1
        report['max_control_semigroup'] = max(report['max_control_semigroup'], size)
    report['all_passed'] = True
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
