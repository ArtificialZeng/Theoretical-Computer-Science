"""Bounded exact sanity checks, not a CCRA nonrecognizability proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json

JOB = 'c021-ccrapumping-triage-d79f905080dc'
ROOT = Path(__file__).resolve().parents[1]

def words(bound):
    return [''.join(t) for k in range(bound + 1)
            for t in product('01', repeat=k)]

def value(w):
    return sum(i for i, a in enumerate(w, 1) if a == '1')

def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]

letters = {b: [[1, int(b), int(b)], [0, 1, 1], [0, 0, 1]]
           for b in '01'}
matrix_cases = 0
for w in words(7):
    a = [[int(i == j) for j in range(3)] for i in range(3)]
    for b in w:
        a = matmul(letters[b], a)  # appending letters, column convention
    assert a == [[1, w.count('1'), value(w)],
                 [0, 1, len(w)], [0, 0, 1]]
    matrix_cases += 1

psf_cases = 0
for u, w, v in product(words(3), repeat=3):
    c = value(u) + value(v) + len(u) * v.count('1')
    a = value(w) + len(u) * w.count('1') + len(w) * v.count('1')
    b = len(w) * w.count('1')
    for n in range(7):
        expected = F(c) + a*n + F(b*n*(n-1), 2)
        assert value(u + w*n + v) == expected
        shifted = F(c) + a*(n+1) + F(b*n*(n+1), 2)
        assert value(u + w*(n+1) + v) == shifted
        psf_cases += 1

# Multiaffine polynomials use bitmask monomials 1,x,y,xy.
def add(a, b):
    c = dict(a)
    for k, v in b.items():
        c[k] = c.get(k, F(0)) + v
    return {k: v for k, v in c.items() if v}

def mul(a, b):
    c = {}
    for i, x in a.items():
        for j, y in b.items():
            assert i & j == 0, 'Not multiaffine; substitution premise failed'
            c[i | j] = c.get(i | j, F(0)) + x*y
    return {k: v for k, v in c.items() if v}

ONE, X, Y = {0: F(1)}, {1: F(1)}, {2: F(1)}

def substitute(poly, p):
    ans = {}
    for mask, coeff in poly.items():
        term = {0: coeff}
        for j in range(2):
            if mask & (1 << j):
                term = mul(term, p[j])
        ans = add(ans, term)
    return ans

def compose(p, q):
    return tuple(substitute(poly, q) for poly in p)

def rank(columns):
    a = [[col.get(i, F(0)) for col in columns] for i in range(4)]
    r = 0
    for c in range(4):
        pivot = next((i for i in range(r, 4) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        z = a[r][c]
        a[r] = [t/z for t in a[r]]
        for i in range(4):
            if i != r:
                z = a[i][c]
                a[i] = [t - z*s for t, s in zip(a[i], a[r])]
        r += 1
    return r

generators = [
    (X, Y),
    (add(X, Y), {}),
    (mul(X, Y), ONE),
    (add(X, ONE), {}),
    (Y, X),
    (add(X, ONE), Y),
    ({1: F(2), 0: F(1)}, {2: F(3), 0: F(-1)}),
    ({}, {}),
]
rank_cases, singular_cases = 0, 0
for k in range(4):
    for indices in product(range(len(generators)), repeat=k):
        p = (X, Y)
        for i in indices:
            p = compose(generators[i], p)
        supports = [set().union(*(set(j for j in range(2) if m & (1 << j))
                                  for m in poly)) if poly else set()
                    for poly in p]
        assert not supports[0].intersection(supports[1])
        active = sum(bool(s) for s in supports)
        actual_rank = rank([ONE, p[0], p[1], mul(p[0], p[1])])
        assert actual_rank == 2**active
        singular_cases += actual_rank < 4
        rank_cases += 1

result = {
    'job_id': JOB,
    'kind': 'exact finite observations and baseline reproduction',
    'source_sha256': hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'matrix_check': {'max_word_length': 7, 'cases': matrix_cases},
    'pumping_check': {'max_u_w_v_length_each': 3, 'n_range': [0, 6],
                      'triples': len(words(3))**3, 'cases': psf_cases,
                      'both_unshifted_and_shifted_checked': True},
    'rank_check': {'registers': 2, 'generator_count': len(generators),
                   'max_composed_word_length': 3, 'cases': rank_cases,
                   'singular_cases': singular_cases,
                   'assertion': 'rank(B_P)=2^(nonconstant output count)'},
    'limitations': [
        'Generator family is explicitly finite, not all two-register updates.',
        'No observable-quotient or finite-control obstruction was certified.',
        'No all-register nonrecognizability theorem or novelty established.',
        'The pumping formula is a known source baseline, not a new result.'
    ],
    'status': 'passed'
}
(ROOT/'evidence/triage-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
