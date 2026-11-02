#!/usr/bin/env python3
"""Bounded exact adversarial diagnostics; not a universal theorem or review.

Standalone rational matrix/control code, independent of the supervisor's
matrix helpers. All outputs stay in this project. No external processes.
"""
from collections import deque, Counter
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json
import random


def eye(d):
    return [[F(i == j) for j in range(d)] for i in range(d)]


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def lin(a, b, c=F(1)):
    return [[x+c*y for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def power(a, n):
    value = eye(len(a))
    while n:
        if n % 2:
            value = mul(value, a)
        a = mul(a, a)
        n //= 2
    return value


def inverse(a):
    d = len(a)
    z = [row.copy()+other for row, other in zip(a, eye(d))]
    for j in range(d):
        i = next(i for i in range(j, d) if z[i][j])
        z[j], z[i] = z[i], z[j]
        c = z[j][j]
        z[j] = [v/c for v in z[j]]
        for i in range(d):
            if i != j:
                c = z[i][j]
                z[i] = [x-c*y for x, y in zip(z[i], z[j])]
    return [row[d:] for row in z]


def root(a, exponent):
    d = len(a)
    z = lin(a, eye(d), F(-1))
    assert power(z, d) == [[0]*d for _ in range(d)]
    result, term, c = eye(d), eye(d), F(1)
    for j in range(1, d):
        term = mul(term, z)
        c *= (exponent-j+1)/j
        result = lin(result, term, c)
    return result


def basis_closure(start, steps):
    """Keep original vectors and words, using an independent echelon test."""
    pending = deque([((), start)])
    pivots, originals = {}, []
    while pending:
        word, original = pending.popleft()
        v = original.copy()
        for j in sorted(pivots):
            if v[j]:
                c = v[j]
                v = [x-c*y for x, y in zip(v, pivots[j])]
        j = next((j for j, x in enumerate(v) if x), None)
        if j is None:
            continue
        c = v[j]
        pivots[j] = [x/c for x in v]
        originals.append((word, original))
        for a, step in enumerate(steps):
            pending.append((word+(a,), step(original)))
    return originals


def graph_paths(q, controls):
    paths, pending = {q: ()}, deque([q])
    while pending:
        q = pending.popleft()
        for a, t in enumerate(controls):
            if t[q] not in paths:
                paths[t[q]] = paths[q]+(a,)
                pending.append(t[q])
    return paths


def compose(t, u):
    return tuple(u[q] for q in t)  # read t followed by u


def control_blocks(controls):
    n = len(controls[0])
    paths = [graph_paths(q, controls) for q in range(n)]
    components = {frozenset(v for v in range(n)
                            if v in paths[q] and q in paths[v])
                  for q in range(n)}
    c = min((c for c in components if c <= paths[0].keys()
             and all(t[q] in c for q in c for t in controls)),
            key=lambda c: tuple(sorted(c)))
    states = sorted(c)
    renaming = {q: i for i, q in enumerate(states)}
    ts = [tuple(renaming[t[q]] for q in states) for t in controls]
    identity = tuple(range(len(states)))
    monoid, pending = {identity: ()}, deque([identity])
    while pending:
        t = pending.popleft()
        for a, u in enumerate(ts):
            v = compose(t, u)
            if v not in monoid:
                monoid[v] = monoid[t]+(a,)
                pending.append(v)
    t = min(monoid, key=lambda t: (len(set(t)), len(monoid[t]), monoid[t]))
    r = len(set(t))
    big_n = factorial(r)
    e = monoid[t]*big_n

    def act(word):
        t = identity
        for a in word:
            t = compose(t, ts[a])
        return t

    idem = act(e)
    image = set(idem)
    assert len(image) == r and all(idem[q] == q for q in image)
    blocks = [e]
    for a in range(len(controls)):
        raw = e+(a,)+e
        t = act(raw)
        assert set(t) == image == {t[q] for q in image}
        w = raw*big_n
        assert all(act(w)[q] == q for q in image)
        blocks.append(w)
    q = states[min(image)]
    prefix = paths[0][q]
    assert q in c and graph_paths(0, controls)[q] == prefix
    return blocks, prefix, r, len(monoid)


def dense_model(k):
    d = k+1
    s = [[F(i+1, d+1)**j for j in range(d)] for i in range(d)]
    si = inverse(s)
    assert mul(s, si) == eye(d)
    letters = []
    for a in range(k):
        u = eye(d)
        u[a][a+1] = F((-1)**a*(a+2), a+1)
        letters.append(mul(mul(si, u), s))
    # Row representation conjugated from scattered pattern 012...(k-1).
    return letters, s[0], [[row[-1]] for row in si]


def transfer_check(controls, model):
    letters, initial, final = model
    d = len(initial)

    def wm(word):
        result = eye(d)
        for a in word:
            result = mul(result, letters[a])
        return result

    words, prefix, r, size = control_blocks(controls)
    blocks = [wm(w) for w in words]
    e = blocks[0]
    ei = root(e, F(-1))
    assert mul(e, ei) == eye(d)
    for a, block in enumerate(blocks[1:]):
        recovered = root(block, F(1, factorial(r)))
        assert recovered == mul(mul(e, letters[a]), e)
        assert mul(mul(ei, recovered), ei) == letters[a]
    ip = mul([initial], wm(prefix))[0]
    rows = basis_closure(ip, [lambda v, m=m: mul([v], m)[0] for m in blocks])
    cols = basis_closure([v[0] for v in final],
                         [lambda v, m=m: [row[0] for row in mul(m, [[x] for x in v])]
                          for m in blocks])
    assert len(rows) == len(cols) == d
    assert any(mul(a, b) != mul(b, a) for a in blocks for b in blocks)
    return r, size, len(prefix), max(map(len, words))


def trace_test(letters):
    d = len(letters[0])
    initial = [x for row in eye(d) for x in row]+[F(1)]

    def step(v, m):
        x = [v[i*d:(i+1)*d] for i in range(d)]
        return [t for row in mul(x, m) for t in row]+[v[-1]]

    basis = basis_closure(initial, [lambda v, m=m: step(v, m) for m in letters])
    for w, v in basis:
        assert len(w) <= d*d
        if sum(v[i*d+i] for i in range(d)) != d*v[-1]:
            return False, w
    return True, None


def main():
    rng = random.Random(20261104)
    report = dict(job_id='c021-ccrapumping-research-b9b720512ca2',
                  scope='Exact finite diagnostics, not universal proof or independent review.',
                  seed=20261104, controls=0, control_ranks={}, max_control_monoid=0,
                  max_return_word_length=0, max_actual_prefix_length=0,
                  exact_matrix_model='Dense rational conjugates of scaled UT4 and UT5 pattern models',
                  original_scope_checks=['Singular physical-map obstruction is proved symbolically in the proof dossier, not certified by these tests.'])
    models = {k: dense_model(k) for k in (3, 4)}
    cases = []
    for n in (1, 2):
        for flat in product(range(n), repeat=3*n):
            cases.append([tuple(flat[a*n:(a+1)*n]) for a in range(3)])
    for n in (3, 4):
        for _ in range(8):
            cases.append([tuple(rng.randrange(n) for _ in range(n)) for a in range(4)])
        for _ in range(4):
            ts = []
            for a in range(4):
                t = list(range(n)); rng.shuffle(t); ts.append(tuple(t))
            cases.append(ts)
    for controls in cases:
        r, size, lp, lb = transfer_check(controls, models[len(controls)])
        report['controls'] += 1
        key = str(r)
        report['control_ranks'][key] = report['control_ranks'].get(key, 0)+1
        report['max_control_monoid'] = max(report['max_control_monoid'], size)
        report['max_return_word_length'] = max(report['max_return_word_length'], lb)
        report['max_actual_prefix_length'] = max(report['max_actual_prefix_length'], lp)
    report['families'] = dict(exhaustive_ternary_controls_n_le2=65,
                             seeded_quaternary_controls_n3_n4=16,
                             permutation_controls_n3_n4=8)
    trace_cases = [(models[k][0], True) for k in (3, 4)]
    trace_cases += [([[[F(1)]]], True), ([[[F(-1)]]], False),
                    ([eye(2), [[F(1), F(1)], [F(0), F(1)]]], True),
                    ([[[F(1), F(1)], [F(0), F(1)]],
                      [[F(1), F(0)], [F(1), F(1)]]], False),
                    ([[[F(1), F(0)], [F(0), F(2)]]], False)]
    report['trace_cases'] = []
    for letters, expected in trace_cases:
        yes, word = trace_test(letters)
        assert yes == expected
        report['trace_cases'].append(dict(d=len(letters[0]), expected=expected,
                                          result=yes, negative_word=word))
    # The last trace case represents constant 1 with an unreachable hidden
    # eigenvalue 2: minimizing removes the hidden block, yielding M_a=[1].
    assert trace_test([[[F(1)]]])[0]
    report['hidden_block_control'] = 'Raw diag(1,2) rejects; minimal [1] accepts for lambda=(1,0), gamma=(1,0)^T.'
    report['all_passed'] = True
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
