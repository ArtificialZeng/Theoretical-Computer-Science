"""Fresh exact checks, independent of the proposer's search implementation.

Pullbacks are reconstructed by Boolean-grid interpolation, rather than
symbolic substitution. Finite checks supplement the universal proof review.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from collections import deque
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c021-ccrapumping-referee-d846876ce849'

def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]

def multiply(a, b):
    return [[sum((x*y for x, y in zip(r, c)), Q(0))
             for c in zip(*b)] for r in a]

def subtract(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]

def power(a, n):
    result = identity(len(a))
    while n:
        if n & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        n //= 2
    return result

def rank(rows):
    basis = {}
    for row in rows:
        row = list(map(Q, row))
        for pivot, old in sorted(basis.items()):
            c = row[pivot]
            if c:
                row = [x-c*y for x, y in zip(row, old)]
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is not None:
            c = row[pivot]
            basis[pivot] = [x/c for x in row]
    return len(basis)

def transpose(a):
    return list(map(list, zip(*a)))

def zero(a):
    return all(x == 0 for row in a for x in row)

def monomials(point):
    result = []
    for mask in range(1 << len(point)):
        value = Q(1)
        for i, x in enumerate(point):
            if mask & (1 << i):
                value *= x
        result.append(value)
    return result

def interpolate(values, n):
    coefficients = list(map(Q, values))
    for i in range(n):
        for mask in range(1 << n):
            if mask & (1 << i):
                coefficients[mask] -= coefficients[mask ^ (1 << i)]
    return coefficients

def pullback(function, n):
    samples = [monomials(function(tuple(Q(bool(mask & (1 << i)))
                                        for i in range(n))))
               for mask in range(1 << n)]
    return transpose([interpolate(column, n) for column in zip(*samples)])

def closure(initial, operators, row):
    basis, todo = [], list(initial)
    while todo:
        v = todo.pop()
        if rank(basis + [v]) == len(basis):
            continue
        basis.append(v)
        for operator in operators:
            todo.append(multiply([v], operator)[0] if row else
                        transpose(multiply(operator, transpose([v])))[0])
    return basis

def e(p):
    x, y, z, t = p
    return ((x+z)*t+2, 3*y-1, Q(0), Q(1))

def a(p):
    x, y, z, t = p
    return (2*y+1, (x+z)*t+3, Q(0), Q(1))

def b(p):
    x, y, z, t = p
    return (3*(x+z)*t-4, y+2, Q(0), Q(1))

def retract(p):
    x, y, z, t = p
    return ((x+z)*t, y, Q(0), Q(1))

operators = [pullback(p, 4) for p in (e, a, b)]
E, I = pullback(retract, 4), identity(16)
assert multiply(E, E) == E
assert rank(E) == rank(operators[0]) == rank(power(operators[0], 2)) == 4
qB = multiply(power(subtract(operators[0], I), 2),
              power(subtract(operators[0], [[3*x for x in r] for r in I]), 2))
assert E == subtract(I, [[x/9 for x in r] for r in qB])
out = interpolate([(Q(bool(mask & 1))+1)*(Q(bool(mask & 2))+1)
                   for mask in range(16)], 4)
initial = monomials((Q(1), Q(2), Q(1), Q(1, 2)))
W = transpose(closure([out], operators, row=False))
O = closure([initial], operators, row=True)
dimension = rank(multiply(O, W))
assert dimension == 4
assert len(W[0]) == 5  # An actual kernel must be quotiented out.
assert zero(multiply(multiply(O, subtract(E, I)), W))
for B in operators:
    assert rank(multiply(multiply(O, B), W)) == dimension
    assert zero(multiply(multiply(O, subtract(multiply(multiply(E, B), E), B)), W))

# Independent exact pumping and row-convention weighted representation checks.
def f(w):
    return sum(i for i, bit in enumerate(w, 1) if bit == '1')

words = [''.join(w) for n in range(5) for w in product('01', repeat=n)]
pumping_cases = 0
for u, w, v in product(words, repeat=3):
    C = f(u)+f(v)+len(u)*v.count('1')
    A = f(w)+len(u)*w.count('1')+len(w)*v.count('1')
    B = len(w)*w.count('1')
    for n in (0, 1, 2, 5, 8):
        expected = C+A+(A+Q(B, 2))*n+Q(B, 2)*n*n
        assert f(u+w*(n+1)+v) == expected
        pumping_cases += 1

matrix_cases = 0
for n in range(9):
    for bits in product((0, 1), repeat=n):
        row = [[Q(0), Q(0), Q(1)]]
        for bit in bits:
            row = multiply(row, [[1, 0, 0], [bit, 1, 0], [bit, 1, 1]])
        assert row[0][0] == f(''.join(map(str, bits)))
        matrix_cases += 1

# Held-out four-state controls. BFS chooses return paths without assuming loops.
def path(edges, source, target):
    todo, seen = deque([(source, '')]), {source}
    while todo:
        q, word = todo.popleft()
        if q == target:
            return word
        for bit in range(2):
            r = edges[q][bit]
            if r not in seen:
                seen.add(r)
                todo.append((r, word+str(bit)))
    return None

def end(edges, q, word):
    for bit in word:
        q = edges[q][int(bit)]
    return q

dfa_cases = 0
for entries in product(range(4), repeat=8):
    edges = [entries[2*i:2*i+2] for i in range(4)]
    reach = [[path(edges, i, j) is not None for j in range(4)] for i in range(4)]
    q = next(i for i in range(4) if reach[0][i] and
             all(not reach[i][j] or reach[j][i] for j in range(4)))
    component = [i for i in range(4) if reach[q][i]]
    s = len(component)
    u = '0'*s + path(edges, end(edges, q, '0'*s), q)
    v = '1'*s + path(edges, end(edges, q, '1'*s), q)
    assert end(edges, q, u) == end(edges, q, v) == q
    assert len(u) <= 2*s-1 and len(v) <= 2*s-1
    assert 2*u.count('1') < len(u) and 2*v.count('1') > len(v)
    delta = v.count('1')*len(u)-u.count('1')*len(v)
    # The reachability determinant is +/-delta*|u|; observability is
    # +/-delta*c(v). Neither depends on the chosen prefix valuation.
    assert delta*len(u) != 0 and delta*v.count('1') != 0
    dfa_cases += 1

# Unique unipotent-root polynomial, including powers larger than dimension.
root_cases = 0
for d in range(1, 7):
    for seed in range(8):
        M = [[Q(i == j) if i >= j else Q(((i+2)*(j+3)+seed) % 5 - 2)
              for j in range(d)] for i in range(d)]
        for exponent in (1, 2, 6, 24):
            H = subtract(power(M, exponent), identity(d))
            result = identity(d)
            term, coefficient = identity(d), Q(1)
            for j in range(1, d):
                term = multiply(term, H)
                coefficient *= (Q(1, exponent)-j+1)/j
                result = [[x+coefficient*y for x, y in zip(r, s)]
                          for r, s in zip(result, term)]
            assert result == M
            root_cases += 1

result = {
    'job_id': JOB,
    'status': 'passed',
    'arithmetic': 'exact integers and fractions',
    'method': 'Independent Boolean-grid interpolation of multiaffine pullbacks; no proposer code imported or executed.',
    'source_sha256': hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'singular_subquotient': {
        'maps': ['((x+z)t+2,3y-1,0,1)', '(2y+1,(x+z)t+3,0,1)', '(3(x+z)t-4,y+2,0,1)'],
        'Q': '((x+z)t,y,0,1)',
        'initial': ['1','2','1','1/2'],
        'output': '(x+1)(y+1)',
        'global_minimum': 'All nonempty products map onto L={z=0,t=1}; restrictions to L are affine coordinate permutations.',
        'ambient_dimension': 16,
        'physical_pullback_rank': 4,
        'reachable_polynomial_dimension': len(W[0]),
        'observable_row_dimension': len(O),
        'minimal_quotient_dimension': dimension,
        'projection_polynomial': '1-(T-1)^2(T-3)^2/9',
        'checked': ['E^2=E', 'E=p(B_e)', 'E acts identically on W/N', 'all minimal letters invertible', 'compressed letters agree on W/N']
    },
    'pumping': {'word_length_bound_each': 4, 'n_values': [0,1,2,5,8], 'cases': pumping_cases},
    'weighted_realization': {'word_length_bound': 8, 'cases': matrix_cases},
    'finite_control': {'states': 4, 'complete_binary_DFAs': dfa_cases},
    'unipotent_root': {'dimension_range': [1,6], 'powers': [1,2,6,24], 'cases': root_cases},
    'limitations': 'Finite checks are diagnostics. Acceptance, if any, rests on the universal mathematical reconstruction in math.md.'
}
(ROOT/'audit/referee-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
