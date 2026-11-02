#!/usr/bin/env python3
"""Exact diagnostics for an UNACCEPTED same-project algorithmic extension.

This checks the commutativity algorithm and its YES synthesis, not the theorem
excluding all finite-state CCRAs on NO.  It does not modify frozen evidence.
"""
from collections import deque
from fractions import Fraction as F
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import random


def words(alphabet, bound):
    return [''.join(w) for n in range(bound + 1)
            for w in product(alphabet, repeat=n)]


def count(w, p):
    d = [1] + [0] * len(p)
    for a in w:
        for i in range(len(p) - 1, -1, -1):
            if p[i] == a:
                d[i + 1] += d[i]
    return d[-1]


def direct(terms, w):
    return sum((c * count(w, p) for p, c in terms), F(0))


class PatternWA:
    def __init__(self, terms, alphabet):
        self.terms, self.alphabet = terms, alphabet
        self.edges = {a: [] for a in alphabet}
        self.initial, self.final = [], []
        for p, c in terms:
            k = len(self.initial)
            self.initial += [F(c)] + [F(0)] * len(p)
            self.final += [F(0)] * len(p) + [F(1)]
            for i, a in enumerate(p):
                self.edges[a].append((k + i, k + i + 1))
        self.dim = len(self.initial)

    def row_step(self, v, a):
        z = v.copy()
        for i, j in self.edges[a]:
            z[j] += v[i]
        return z

    def col_step(self, v, a):
        z = v.copy()
        for i, j in self.edges[a]:
            z[i] += v[j]
        return z

    def value(self, w):
        v = self.initial.copy()
        for a in w:
            v = self.row_step(v, a)
        return dot(v, self.final)


def dot(u, v):
    return sum((x * y for x, y in zip(u, v)), F(0))


def invariant_basis(wa, column=False):
    """Retain actual original word vectors; echelon vectors only test rank."""
    start = wa.final if column else wa.initial
    step = wa.col_step if column else wa.row_step
    pending = deque([('', start.copy())])
    pivots, originals = {}, []
    while pending:
        w, v = pending.popleft()
        z = v.copy()
        for pivot in sorted(pivots):
            if z[pivot]:
                c = z[pivot]
                z = [x - c * y for x, y in zip(z, pivots[pivot])]
        p = next((i for i, x in enumerate(z) if x), None)
        if p is None:
            continue
        c = z[p]
        pivots[p] = [x / c for x in z]
        originals.append((w, v))
        assert len(w) <= wa.dim - 1
        for a in wa.alphabet:
            pending.append(((a + w) if column else (w + a), step(v, a)))
    return originals


def decide(wa):
    rows, cols = invariant_basis(wa), invariant_basis(wa, True)
    for u, r in rows:
        for a, b in combinations(wa.alphabet, 2):
            rab = wa.row_step(wa.row_step(r, a), b)
            rba = wa.row_step(wa.row_step(r, b), a)
            delta = [x - y for x, y in zip(rab, rba)]
            for v, c in cols:
                if dot(delta, c):
                    x, y = u + a + b + v, u + b + a + v
                    assert len(x) <= 2 * wa.dim
                    return False, (x, y), (len(rows), len(cols))
    return True, None, (len(rows), len(cols))


def synthesize(terms):
    """Explicit disjoint counter offsets, with each old register used once."""
    slots, outputs = [], []
    for p, c in terms:
        if list(p) != sorted(p):
            continue
        ids, denominator = [], 1
        for a in sorted(set(p)):
            m = p.count(a)
            denominator *= math.factorial(m)
            for j in range(m):
                ids.append(len(slots))
                slots.append((a, -j))
        outputs.append((c / denominator, ids))
    flat = [i for _, ids in outputs for i in ids]
    assert sorted(flat) == list(range(len(slots)))
    assert len(slots) <= sum(len(p) for p, _ in terms)
    return slots, outputs


def evaluate_ccra(compiled, w):
    slots, outputs = compiled
    registers = [F(initial) for _, initial in slots]
    for a in w:
        # Register i alone is consumed by update i, even if counters agree.
        registers = [x + int(letter == a)
                     for x, (letter, _) in zip(registers, slots)]
    return sum((c * math.prod(registers[i] for i in ids)
                for c, ids in outputs), F(0))


def main():
    rng = random.Random(20261102)
    cases = []
    patterns = words('01', 3)
    cases.extend(([(p, F(1))], '01') for p in patterns)
    for p, q in combinations(patterns, 2):
        for cp, cq in [(F(1), F(1)), (F(1), F(-1)), (F(1, 2), F(3, 2))]:
            cases.append(([(p, cp), (q, cq)], '01'))
    # Repetitions, rational cancellation and many noncommutative summands.
    for alphabet in ['01', 'abc']:
        for n in range(1, 6):
            for _ in range(4):
                multiset = ''.join(rng.choice(alphabet) for _ in range(n))
                terms = [(p, F(1)) for p in sorted(set(map(''.join, permutations(multiset))))]
                cases.append((terms, alphabet))
        for _ in range(50):
            terms = [(''.join(rng.choice(alphabet) for _ in range(rng.randrange(5))),
                      F(rng.randrange(-3, 4), rng.randrange(1, 4)))
                     for _ in range(rng.randrange(1, 5))]
            cases.append((terms, alphabet))
    cases.extend([
        ([('1', F(1)), ('01', F(1)), ('11', F(1))], '01'),
        ([('01', F(1)), ('10', F(1))], '01'),
        ([('abc', F(2)), ('abc', F(-2))], 'abc'),
        ([], '01'),
    ])
    report = dict(scope='Exact finite diagnostics only; finite-state CCRA exclusion theorem is unaccepted.',
                  seed=20261102, cases=len(cases), yes=0, no=0,
                  wa_value_checks=0, yes_copyless_synthesis_checks=0,
                  no_certificates_checked=0, max_dimension=0, max_witness_length=0,
                  mismatches=[])
    for terms, alphabet in cases:
        wa = PatternWA(terms, alphabet)
        report['max_dimension'] = max(report['max_dimension'], wa.dim)
        yes, witness, ranks = decide(wa)
        report['yes' if yes else 'no'] += 1
        compiled = synthesize(terms) if yes else None
        if not yes:
            x, y = witness
            assert sorted(x) == sorted(y)
            assert direct(terms, x) != direct(terms, y)
            report['no_certificates_checked'] += 1
            report['max_witness_length'] = max(report['max_witness_length'], len(x))
        for w in words(alphabet, 5 if alphabet == '01' else 4):
            d = direct(terms, w)
            assert wa.value(w) == d, (terms, w, 'WA')
            report['wa_value_checks'] += 1
            if yes:
                assert evaluate_ccra(compiled, w) == d, (terms, w, 'synthesis')
                assert direct(terms, ''.join(sorted(w))) == d
                report['yes_copyless_synthesis_checks'] += 1
        assert all(k <= wa.dim for k in ranks)
    report['all_passed'] = True
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
