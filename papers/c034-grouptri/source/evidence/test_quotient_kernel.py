"""Exact semantic tests of the complete lifting reduction; no fast runtime claim.

The capped detector and prime leaf solver are deliberately brute force.
All computations use exact integer residues. Selected/seeded tests are not
exhaustive claims outside the explicitly enumerated binary quotient domain.
"""
import hashlib
import itertools as it
import json
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path

JOB = 'c034-grouptri-research-d92d3d43a90d'
COUNTS = Counter()


def add(x, y, m):
    return tuple((a + b) % m for a, b in zip(x, y))


def sub(x, y, m):
    return tuple((a - b) % m for a, b in zip(x, y))


def prime_divisor(m):
    return next(p for p in range(2, m + 1) if m % p == 0)


def triples(sizes):
    return it.product(*(range(n) for n in sizes))


def truth(A, B, C, m, sizes):
    return {(i, k, j) for i, k, j in triples(sizes)
            if add(A[i, k], B[k, j], m) == C[i, j]}


def capped(relation, sizes, cap, reverse=False):
    n = max(1, *sizes)
    N = 1 << (n - 1).bit_length()
    lists = {(i, j): [] for i in range(sizes[0]) for j in range(sizes[2])}

    def active(i, k, j):
        return ((i, k, j) in relation and len(lists[i, j]) < cap)

    def visit(I, K, J):
        if not any(active(i, k, j) for i in I for k in K for j in J):
            return
        if len(I) <= 2:
            for i in I:
                for k in K:
                    for j in J:
                        if active(i, k, j):
                            lists[i, j].append(k)
            return
        t = len(I) // 2
        children = list(it.product((I[:t], I[t:]), (K[:t], K[t:]),
                                   (J[:t], J[t:])))
        if reverse:
            children.reverse()
        for child in children:
            visit(*child)

    visit(tuple(range(N)), tuple(range(N)), tuple(range(N)))
    for (i, j), ks in lists.items():
        assert len(ks) == len(set(ks))
        assert len(ks) == min(cap, sum(t[0] == i and t[2] == j for t in relation))
    return lists


def decompose(A, B, C, p, sizes, s, reverse=False):
    n = max(1, *sizes)
    relation = truth(A, B, C, p, sizes)
    cap, r = n // s + 1, s * s
    lists = capped(relation, sizes, cap, reverse)
    light = {(i, k, j) for (i, j), ks in lists.items() if len(ks) < cap for k in ks}
    remaining = {ij: set(ks) for ij, ks in lists.items() if len(ks) == cap}
    pivot, H = {}, []
    while remaining:
        h = max(range(sizes[1]), key=lambda k: (sum(k in ks for ks in remaining.values()), -k))
        H.append(h)
        hit = [ij for ij, ks in remaining.items() if h in ks]
        assert hit
        for ij in hit:
            pivot[ij] = h
            del remaining[ij]
    low, pieces = set(), []
    dimension = len(next(iter(A.values()), next(iter(B.values()), ())))
    zero = (0,) * dimension
    for h in H:
        freq, slots = {}, {}
        for k in range(sizes[1]):
            freq[k] = Counter(sub(B[h, j], B[k, j], p) for j in range(sizes[2]))
            slots[k] = sorted(v for v, count in freq[k].items() if count * r > n)
            assert len(slots[k]) <= r
        for i in range(sizes[0]):
            for k in range(sizes[1]):
                v = sub(A[i, k], A[i, h], p)
                if v not in slots[k]:
                    assert freq[k][v] * r <= n
                    for j in range(sizes[2]):
                        if sub(B[h, j], B[k, j], p) == v and pivot.get((i, j)) == h:
                            assert (i, k, j) not in low
                            low.add((i, k, j))
        for l in range(r):
            tau = {k: slots[k][l] if l < len(slots[k]) else zero for k in range(sizes[1])}
            E1 = {(i, k) for i in range(sizes[0]) for k in range(sizes[1])
                  if l < len(slots[k]) and sub(A[i, k], A[i, h], p) == tau[k]}
            E2 = {(k, j) for k in range(sizes[1]) for j in range(sizes[2])
                  if l < len(slots[k]) and sub(B[h, j], B[k, j], p) == tau[k]}
            E3 = {ij for ij, selected in pivot.items() if selected == h}
            for i, k in E1:
                assert A[i, k] == add(A[i, h], tau[k], p)
            for k, j in E2:
                assert B[k, j] == sub(B[h, j], tau[k], p)
            for i, j in E3:
                assert C[i, j] == add(A[i, h], B[h, j], p)
            present = {(i, k, j) for i, k, j in triples(sizes)
                       if (i, k) in E1 and (k, j) in E2 and (i, j) in E3}
            pieces.append((h, tau, E1, E2, E3, present))
    multiplicity = Counter(light) + Counter(low)
    for piece in pieces:
        multiplicity.update(piece[-1])
    assert set(multiplicity) == relation
    assert all(v == 1 for v in multiplicity.values())
    assert len(pieces) == len(H) * r
    COUNTS['decompositions'] += 1
    COUNTS['few_exception_triangles'] += len(light)
    COUNTS['low_exception_triangles'] += len(low)
    COUNTS['nonempty_high_pieces'] += sum(bool(t[-1]) for t in pieces)
    COUNTS['all_materialized_pieces'] += len(pieces)
    return light | low, pieces


def lift(A, B, C, m, p, sizes, piece):
    q = m // p
    h, tau, E1, E2, E3, present = piece
    dimension = len(next(iter(A.values())))
    zero = (0,) * dimension
    QA = {e: tuple(x % p for x in w) for e, w in A.items()}
    QB = {e: tuple(x % p for x in w) for e, w in B.items()}

    def encode(value, present_edge, kind):
        if present_edge:
            assert all(x % p == 0 for x in value)
            return tuple(x // p for x in value) + (0, 0, 0)
        return zero + tuple(int(t == kind) for t in range(3))

    U, V, D = {}, {}, {}
    for i, k in A:
        shifted = sub(sub(A[i, k], QA[i, h], m), tau[k], m)
        U[i, k] = encode(shifted, (i, k) in E1, 0)
    for k, j in B:
        shifted = add(sub(B[k, j], QB[h, j], m), tau[k], m)
        V[k, j] = encode(shifted, (k, j) in E2, 1)
    for i, j in C:
        shifted = sub(sub(C[i, j], QA[i, h], m), QB[h, j], m)
        # C stores minus the actual third edge; marker on actual edge is +1.
        plus_weight = tuple(-x % m for x in shifted)
        third_plus = encode(plus_weight, (i, j) in E3, 2)
        D[i, j] = tuple(-x % q for x in third_plus)
    encoded_truth = truth(U, V, D, q, sizes)
    expected = truth(A, B, C, m, sizes) & present
    assert encoded_truth == expected
    COUNTS['kernel_instances_checked'] += 1
    COUNTS['kernel_triangle_checks'] += sizes[0] * sizes[1] * sizes[2]
    return U, V, D


def check(A, B, C, m, sizes, s, reverse=False, recurse=False):
    if not all(sizes):
        assert not truth(A, B, C, m, sizes)
        COUNTS['empty_part_tests'] += 1
        return False
    p = prime_divisor(m)
    if p == m:
        COUNTS['prime_brute_leaves'] += 1
        return bool(truth(A, B, C, m, sizes))
    quotient = [{e: tuple(x % p for x in w) for e, w in T.items()} for T in (A, B, C)]
    exceptions, pieces = decompose(*quotient, p, sizes, s, reverse)
    original = truth(A, B, C, m, sizes)
    answers = [bool(original & exceptions)]
    for piece in pieces:
        U, V, D = lift(A, B, C, m, p, sizes, piece)
        if recurse:
            answers.append(check(U, V, D, m // p, sizes, s, not reverse, True))
        else:
            answers.append(bool(truth(U, V, D, m // p, sizes)))
    assert any(answers) == bool(original)
    return any(answers)


def tables(sizes, dimension, m, rng, mode=0):
    U, X, V = sizes
    rand = lambda: tuple(rng.randrange(m) for _ in range(dimension))
    A = {(i, k): rand() for i in range(U) for k in range(X)}
    B = {(k, j): rand() for k in range(X) for j in range(V)}
    C = {(i, j): rand() for i in range(U) for j in range(V)}
    if mode in (1, 2, 3):
        p = prime_divisor(m)
        a, b, t = [tuple(rng.randrange(p) for _ in range(dimension)) for _ in range(U)], [tuple(rng.randrange(p) for _ in range(dimension)) for _ in range(V)], [tuple(rng.randrange(p) for _ in range(dimension)) for _ in range(X)]
        for T, potentials in ((A, {(i, k): add(a[i], t[k], p) for i, k in A}),
                              (B, {(k, j): sub(b[j], t[k], p) for k, j in B}),
                              (C, {(i, j): add(a[i], b[j], p) for i, j in C})):
            for e, residue in potentials.items():
                T[e] = tuple(x + p * rng.randrange(m // p) for x in residue)
        if mode == 2:
            # Planted exact all-zero-sum gauge, including nonzero kernel data.
            aa, bb, tt = [rand() for _ in range(U)], [rand() for _ in range(V)], [rand() for _ in range(X)]
            A = {(i, k): add(aa[i], tt[k], m) for i, k in A}
            B = {(k, j): sub(bb[j], tt[k], m) for k, j in B}
            C = {(i, j): add(aa[i], bb[j], m) for i, j in C}
        if mode == 3:
            # Dense quotient-zero, no original-zero: kernel obstruction.
            A = {e: (0,) * dimension for e in A}
            B = {e: (0,) * dimension for e in B}
            C = {e: (p,) + (0,) * (dimension - 1) for e in C}
    return A, B, C


def delta(m):
    p = prime_divisor(m)
    return Fraction(1, 1000) if p == m else Fraction(1, 144000) * delta(m // p)


def run():
    rng = random.Random(340034)
    # Exhaust every label assignment in the 12-edge binary quotient at n=2.
    edges = [(kind, x, y) for kind in range(3) for x in range(2) for y in range(2)]
    for bits in range(1 << 12):
        T = [{}, {}, {}]
        for z, (kind, x, y) in enumerate(edges):
            residue = bits >> z & 1
            # Fixed varying kernel digits, selected rather than exhaustive.
            T[kind][x, y] = (residue + 2 * ((bits + z * z + x * y) & 1),)
        for s in (1, 2):
            check(*T, 4, (2, 2, 2), s, bool(bits & 1))
            COUNTS['exhaustive_binary_quotient_tests'] += 1
    # Unequal, empty, padded, low-frequency, pure-gauge and negative dense cases.
    for m in (4, 6, 8, 9, 10, 12, 16, 18, 24, 25, 27, 36):
        for sizes in ((0, 2, 3), (1, 1, 1), (2, 3, 4), (4, 4, 4), (5, 6, 7), (8, 8, 8)):
            for dimension in (1, 2):
                for mode in range(4):
                    T = tables(sizes, dimension, m, rng, mode)
                    for s in sorted({1, 2, min(3, max(sizes))}):
                        check(*T, m, sizes, s, bool(mode & 1))
                        COUNTS['selected_structured_tests'] += 1
    # Full repeated lifting through composite kernels with carried marker blocks.
    for m in (8, 12, 16, 18, 24, 27, 32, 36, 48, 72):
        for mode in range(4):
            T = tables((3, 3, 3), 2, m, rng, mode)
            check(*T, m, (3, 3, 3), 2, recurse=True)
            COUNTS['full_recursive_tests'] += 1
    # Exact exponent ledger checks (finite arithmetic sanity, not induction proof).
    for m in range(2, 257):
        p = prime_divisor(m)
        assert 0 < delta(m) <= Fraction(1, 1000)
        if p != m:
            dq = delta(m // p)
            theta = dq / 12
            raw = Fraction(1, 1000) * theta / 6
            assert delta(m) == raw / 2
            assert all(gain >= raw for gain in (theta, 1-theta, 1-3*theta, dq-3*theta))
        COUNTS['exact_exponent_checks'] += 1
    return {
        'job_id': JOB, 'status': 'passed', 'counts': dict(COUNTS),
        'exhaustive_scope': 'All 4096 F_2 assignments to the 12 edges of side-2 complete tripartite graphs, at s=1 and s=2; selected deterministic Z_4 kernel digits, not all Z_4 labels.',
        'selected_scope': 'Listed moduli 4,6,8,9,10,12,16,18,24,25,27,36; six listed unequal/empty/padded size triples through side 8; dimensions 1/2; seeded random, dense quotient, exact gauge, dense negative kernel patterns; s=1/2/3 as listed.',
        'recursive_scope': '40 complete recursive semantic runs, dimension 2, side 3, moduli 8,12,16,18,24,27,32,36,48,72, four modes each.',
        'seed': 340034,
        'limits': 'The capped detector and prime solver are brute force. These are exact finite semantic/cost-ledger checks, not fast implementation benchmarks, exhaustive arbitrary-group tests, or independent proof audits.',
        'delta_4': str(delta(4)), 'delta_8': str(delta(8)),
        'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }


if __name__ == '__main__':
    result = run()
    Path('evidence/quotient-kernel-tests.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
