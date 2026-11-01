"""Exact bounded adversarial checks. The general proof is in resolution-proof.md.

No finite enumeration here purports to cover arbitrary-register CCRAs.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'c021-ccrapumping-research-44e54bf7c116'

def add(p, q):
    r = dict(p)
    for m, c in q.items():
        r[m] = r.get(m, F(0)) + c
    return {m: c for m, c in r.items() if c}

def scale(p, c):
    return {m: c*v for m, v in p.items() if c*v}

def mul(p, q):
    r = {}
    for m, c in p.items():
        for n, d in q.items():
            assert not m & n, 'repeated variable in multiplication'
            r[m | n] = r.get(m | n, F(0)) + c*d
    return {m: c for m, c in r.items() if c}

def substitute(p, maps):
    r = {}
    for m, c in p.items():
        t = {0: c}
        for i, q in enumerate(maps):
            if m & (1 << i):
                t = mul(t, q)
        r = add(r, t)
    return r

def compose(p, q):
    return tuple(substitute(t, q) for t in p)

def ident(n):
    return tuple({1 << i: F(1)} for i in range(n))

def active(p):
    return sum(any(m for m in t) for t in p)

def copyless(p):
    used = 0
    for t in p:
        support = 0
        for m in t:
            support |= m
        assert not support & used
        used |= support

def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]

def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)]
            for row in a]

def minus(a, b):
    return [[x-y for x, y in zip(r, s)] for r, s in zip(a, b)]

def transpose(a):
    return list(map(list, zip(*a)))

def rank(a):
    a = [list(row) for row in a]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        j = next((j for j in range(r, len(a)) if a[j][c]), None)
        if j is None:
            continue
        a[r], a[j] = a[j], a[r]
        d = a[r][c]
        a[r] = [v/d for v in a[r]]
        for j in range(len(a)):
            if j != r and a[j][c]:
                d = a[j][c]
                a[j] = [v-d*w for v, w in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r

def pullback(p):
    n = len(p)
    cols = [substitute({m: F(1)}, p) for m in range(1 << n)]
    return [[c.get(m, F(0)) for c in cols] for m in range(1 << n)]

def mpow(a, n):
    r = eye(len(a))
    for _ in range(n):
        r = mm(r, a)
    return r

def zero(a):
    return all(not v for row in a for v in row)

def span_closure(vectors, maps, row=False):
    basis = []
    todo = list(vectors)
    while todo:
        v = todo.pop()
        if rank(basis + [v]) == len(basis):
            continue
        basis.append(v)
        for a in maps:
            todo.append(mm([v], a)[0] if row
                        else [r[0] for r in mm(a, [[x] for x in v])])
    return basis

ONE = {0: F(1)}
x, y, z, t = ident(4)
L = (x, y, {}, ONE)
e = (add(add(scale(x, F(2)), z), ONE),
     add(scale(mul(y, t), F(3)), scale(ONE, F(-2))), {}, ONE)
a = (add(add(x, z), scale(ONE, F(5))), add(y, t), {}, ONE)
b = (add(y, z), add(scale(mul(x, t), F(2)), scale(ONE, F(-1))), {}, ONE)
gens = (e, a, b)
Q = (add(x, scale(z, F(1, 2))), mul(y, t), {}, ONE)
for p in gens + (Q,):
    copyless(p)
assert compose(Q, Q) == Q
assert compose(Q, L) == L
assert compose(e, Q) == e
assert compose(Q, e) == e
Bs = [pullback(p) for p in gens]
E = pullback(Q)
I = eye(16)
assert mm(E, E) == E
assert rank(E) == rank(Bs[0]) == rank(mm(Bs[0], Bs[0])) == 4
assert mm(E, Bs[0]) == mm(Bs[0], E) == Bs[0]
# Nonzero spectral factor q(T)=(T-1)(T-2)(T-3)(T-6), q(0)=36.
qB = I
for eigenvalue in (1, 2, 3, 6):
    qB = mm(qB, minus(Bs[0], [[eigenvalue*v for v in row] for row in I]))
assert E == minus(I, [[v/36 for v in row] for row in qB])

word_count = 0
for length in range(4):
    for indices in product(range(3), repeat=length):
        p = ident(4)
        for index in indices:
            p = compose(gens[index], p)
        copyless(p)
        assert active(p) == (4 if not length else 2)
        assert rank(pullback(p)) == 2**active(p)
        word_count += 1

# Restriction J^-1 and extension J are computed independently of E B_a E.
xx, yy = ident(2)
restricted = tuple({m: c for m, c in substitute(h, (xx, yy, {}, ONE)).items()}
                   for h in ident(4))
res = [[substitute({m: F(1)}, restricted).get(j, F(0))
        for m in range(16)] for j in range(4)]
J = [[substitute({m: F(1)}, Q[:2]).get(j, F(0))
      for m in range(4)] for j in range(16)]
assert mm(res, J) == eye(4)
assert mm(J, res) == E
for P, B in zip(gens, Bs):
    R = compose(Q, compose(P, L))[:2]
    R = tuple(substitute(h, (xx, yy, {}, ONE)) for h in R)
    assert active(R) == 2
    assert mm(mm(mm(E, B), E), J) == mm(J, pullback(R))
    assert rank(pullback(R)) == 4

# An actual singular physical representation with invertible minimal quotient.
output = add(x, y)
outcol = [output.get(m, F(0)) for m in range(16)]
initial = [F(1) if not (m & 7) else F(0) for m in range(16)]  # (0,0,0,1)
W = transpose(span_closure([outcol], Bs))
O = span_closure([initial], Bs, row=True)
minimal_dimension = rank(mm(O, W))
assert minimal_dimension == 3
assert zero(mm(mm(O, minus(E, I)), W))
for B in Bs:
    C = mm(mm(E, B), E)
    assert zero(mm(mm(O, minus(C, B)), W))

# Held-out singular normalizations: a nonsemisimple nonzero spectrum, and
# a rational operator with irreducible nonzero spectral factor T^2-2.
e_unip = (add(add(x, z), ONE), add(mul(y, t), ONE), {}, ONE)
Q_unip = (add(x, z), mul(y, t), {}, ONE)
BU, EU = pullback(e_unip), pullback(Q_unip)
assert rank(BU) == rank(mm(BU, BU)) == 4
assert EU == [[v+w for v, w in zip(r, s)]
              for r, s in zip(I, mpow(minus(BU, I), 3))]
assert mm(EU, EU) == EU
unip_maps = [BU, Bs[1]]
unip_output = mul(x, y)
unip_W = transpose(span_closure([[unip_output.get(m, F(0)) for m in range(16)]],
                               unip_maps))
unip_O = span_closure([initial], unip_maps, row=True)
assert rank(mm(unip_O, unip_W)) == 4
assert zero(mm(mm(unip_O, minus(EU, I)), unip_W))
assert zero(mm(mm(unip_O, minus(mm(BU, Bs[1]), mm(Bs[1], BU))), unip_W))
for B in unip_maps:
    assert zero(mm(mm(unip_O, mpow(minus(B, I), 4)), unip_W))
e_swap = (add(add(y, z), ONE), add(scale(mul(x, t), F(2)), scale(ONE, F(-1))),
          {}, ONE)
Q_swap = (mul(x, t), add(y, z), {}, ONE)
BT, ET = pullback(e_swap), pullback(Q_swap)
qBT = mm(mm(minus(BT, I), minus(BT, [[2*v for v in row] for row in I])),
         minus(mm(BT, BT), [[2*v for v in row] for row in I]))
assert ET == [[v+w/4 for v, w in zip(r, s)] for r, s in zip(I, qBT)]
assert mm(ET, ET) == ET and rank(BT) == rank(mm(BT, BT)) == 4
for P, QQ in ((e_unip, Q_unip), (e_swap, Q_swap)):
    copyless(P)
    copyless(QQ)
    assert compose(QQ, QQ) == QQ
    assert compose(P, QQ) == compose(QQ, P) == P

# Jordan decomposition of all 288 two-coordinate affine permutations below.
jordan_count = 0
unipotent_parts = []
for perm in ((0, 1), (1, 0)):
    for alphas in product((-2, -1, 1, 2), repeat=2):
        for betas in product((-1, 0, 1), repeat=2):
            R = tuple(add(scale(ident(2)[perm[i]], F(alphas[i])),
                          scale(ONE, F(betas[i]))) for i in range(2))
            R2 = compose(R, R)
            assert all(not any(m not in (0, 1 << i) for m in R2[i])
                       for i in range(2))
            S, U, shift, invshift, diagonal = [], [], [], [], []
            for i in range(2):
                var = ident(2)[i]
                alpha, beta = R2[i].get(1 << i, F(0)), R2[i].get(0, F(0))
                S.append(var if alpha == 1 else R2[i])
                U.append(add(var, scale(ONE, beta)) if alpha == 1 else var)
                c = beta/(alpha-1) if alpha != 1 else F(0)
                shift.append(add(var, scale(ONE, c)))
                invshift.append(add(var, scale(ONE, -c)))
                diagonal.append(scale(var, alpha))
            S, U = tuple(S), tuple(U)
            assert compose(S, U) == compose(U, S) == R2
            assert compose(tuple(shift), compose(S, tuple(invshift))) == tuple(diagonal)
            US, SS, T = pullback(U), pullback(S), pullback(R2)
            assert mm(US, SS) == mm(SS, US) == T
            assert zero(mpow(minus(US, eye(4)), 4))
            unipotent_parts.append(US)
            jordan_count += 1
for U in unipotent_parts:
    for V in unipotent_parts:
        assert mm(U, V) == mm(V, U)

def shortest_path(edges, start, target):
    todo = [(start, '')]
    seen = {start}
    for q, w in todo:
        if q == target:
            return w
        for bit in (0, 1):
            nxt = edges[q][bit]
            if nxt not in seen:
                seen.add(nxt)
                todo.append((nxt, w+str(bit)))
    return None

def run(edges, q, w):
    for bit in w:
        q = edges[q][int(bit)]
    return q

def f(w):
    return sum(i for i, bit in enumerate(w, 1) if bit == '1')

dfa_count = 0
for n in (1, 2, 3):
    for transitions in product(range(n), repeat=2*n):
        edges = [transitions[2*i:2*i+2] for i in range(n)]
        reach = [[shortest_path(edges, i, j) is not None for j in range(n)]
                 for i in range(n)]
        q = next(q for q in range(n) if reach[0][q] and
                 all(not reach[q][j] or reach[j][q] for j in range(n)))
        prefix = shortest_path(edges, 0, q)
        u = '0'*n + shortest_path(edges, run(edges, q, '0'*n), q)
        v = '1'*n + shortest_path(edges, run(edges, q, '1'*n), q)
        assert run(edges, q, u) == run(edges, q, v) == q
        assert n <= len(u) <= 2*n-1 and n <= len(v) <= 2*n-1
        assert 2*u.count('1') < len(u) and 2*v.count('1') > len(v)
        def mat(w):
            return [[F(1), F(w.count('1')), F(f(w))],
                    [F(0), F(1), F(len(w))], [F(0), F(0), F(1)]]
        U, V = mat(u), mat(v)
        D = minus(mm(V, U), mm(U, V))
        assert D[0][2] != 0
        z0 = [[F(f(prefix))], [F(len(prefix))], [F(1)]]
        reachable = [z0, mm(D, z0), mm(minus(U, eye(3)), z0)]
        assert rank(transpose([[r[0] for r in c] for c in reachable])) == 3
        assert rank([[F(1), F(0), F(0)], D[0], minus(V, eye(3))[0]]) == 3
        dfa_count += 1

result = {
    'job_id': JOB,
    'arithmetic': 'exact integers and fractions; no numerical tolerance',
    'source_sha256': hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
    'singular_family': {
        'registers': 4, 'generators': 3, 'word_length_bound': 3,
        'word_cases': word_count, 'nonempty_physical_pullback_rank': 4,
        'ambient_dimension': 16, 'minimum_active_count': 2,
        'global_minimum_justification': 'Each letter maps onto the same L, and restricts to an affine coordinate permutation on L; every nonempty product maps onto L.',
        'normalized_Q': ['x+z/2', 'y*t', '0', '1'],
        'spectral_polynomial': '1-(T-1)(T-2)(T-3)(T-6)/36',
        'W_dimension': len(W[0]), 'observable_row_dimension': len(O),
        'minimal_quotient_dimension': minimal_dimension,
        'checks': ['E squared = E', 'E=p(B_e)', 'image and kernel rank stability',
                   'restriction-extension identity', 'E B_a E intertwines R_a pullback',
                   'E acts as identity on actual observable subquotient',
                   'compressed and original letters agree on that quotient']},
    'jordan_check': {'affine_permutations': jordan_count, 'coordinates': 2,
                     'power': 2, 'translation_pair_cases': jordan_count**2,
                     'checks': ['explicit semisimple conjugacy to diagonal',
                                'unipotent translation factor', 'all translation factors commute']},
    'held_out_singular_checks': {
        'nonzero_nonsemisimple_factor': '(T-1)^3',
        'projection_polynomial': '1+(T-1)^3',
        'unipotent_minimal_quotient_dimension': 4,
        'unipotent_quotient_letters_commute': True,
        'irreducible_spectral_factor': '(T-1)(T-2)(T^2-2)',
        'second_projection_polynomial': '1+(T-1)(T-2)(T^2-2)/4',
        'physical_ambient_dimension': 16, 'physical_rank': 4},
    'finite_control_check': {'complete_binary_DFAs': dfa_count,
                             'state_range': [1, 3], 'checks': ['reachable bottom SCC',
                             'return words of opposite densities', '3D reachability and observability']},
    'status': 'passed',
    'limitations': ['Finite tests do not prove the arbitrary-register theorem.',
                    'General proofs and scope are in evidence/resolution-proof.md.',
                    'No independent referee acceptance is represented by these checks.']}
(ROOT/'evidence/research-checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
