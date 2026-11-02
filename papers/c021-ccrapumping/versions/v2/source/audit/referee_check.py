"""Fresh bounded diagnostics. No imports from submitted research programs.

These finite checks support the written referee reconstruction; they do not
prove its universal assertions. Run from this project with Python 3.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from collections import defaultdict, deque, Counter
from math import factorial, comb
from pathlib import Path
import hashlib
import json
import random

JOB = 'c021-ccrapumping-referee-a7ba97c08c76'


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    cols = list(zip(*b))
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in cols] for row in a]


def plus(a, b, scale=1):
    return [[x+scale*y for x, y in zip(row, other)]
            for row, other in zip(a, b)]


def power(a, k):
    v = identity(len(a))
    while k:
        if k & 1:
            v = matmul(v, a)
        a = matmul(a, a)
        k //= 2
    return v


def rank(rows):
    if not rows:
        return 0
    a = [list(map(Q, row)) for row in rows]
    k = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(k, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        v = a[k][j]
        a[k] = [x/v for x in a[k]]
        for i in range(k+1, len(a)):
            v = a[i][j]
            a[i] = [x-v*y for x, y in zip(a[i], a[k])]
        k += 1
        if k == len(a):
            break
    return k


def transpose(a):
    return [list(row) for row in zip(*a)]


def span(seed, maps, rows=True):
    basis, todo = [], deque([seed])
    while todo:
        v = todo.popleft()
        if rank(basis+[v]) == len(basis):
            continue
        basis.append(v)
        for m in maps:
            todo.append(matmul([v], m)[0] if rows else
                        [row[0] for row in matmul(m, transpose([v]))])
    return basis


def pullback_by_values(fn, n):
    # Boolean-grid evaluations followed by Mobius inversion recover
    # multiaffine coefficients, independently of symbolic substitution.
    count = 1 << n
    columns = []
    for mask in range(count):
        values = []
        for bits in range(count):
            y = fn(tuple(Q(bool(bits & (1 << i))) for i in range(n)))
            value = Q(1)
            for i in range(n):
                if mask & (1 << i):
                    value *= y[i]
            values.append(value)
        for i in range(n):
            for bits in range(count):
                if bits & (1 << i):
                    values[bits] -= values[bits ^ (1 << i)]
        columns.append(values)
    return transpose(columns)


def singular_check():
    def retract(v):
        x, y, z, t, u = v
        return x+t, y*u, z, Q(0), Q(1)

    def e(v):
        x, y, z, t, u = retract(v)
        return 2*x+3, y-4, z+5, t, u

    def a(v):
        x, y, z, t, u = retract(v)
        return y, -x+7, z+1, t, u

    def b(v):
        x, y, z, t, u = retract(v)
        return x+2, y+3, -z+4, t, u

    E = pullback_by_values(retract, 5)
    matrices = [pullback_by_values(fn, 5) for fn in (e, a, b)]
    I = identity(32)
    assert matmul(E, E) == E
    assert rank(E) == 8
    T = matrices[0]
    qT = matmul(power(plus(T, I, -1), 3),
               power(plus(T, I, -2), 3))
    assert E == plus(I, qT, -Q(1, 8))
    assert rank(T) == rank(matmul(T, T)) == 8
    # Output (x+t)(yu)z is syntactically copyless and equals J(xyz).
    output = [Q(mask in (0b10111, 0b11110)) for mask in range(32)]
    # x*y*z*u and t*y*z*u use masks 23 and 30 after expansion.
    valuation = (Q(1), Q(2), Q(3), Q(4), Q(5))
    initial = []
    for mask in range(32):
        v = Q(1)
        for i in range(5):
            if mask & (1 << i):
                v *= valuation[i]
        initial.append(v)
    W = transpose(span(output, matrices, rows=False))
    O = span(initial, matrices)
    minimal_dimension = rank(matmul(O, W))
    assert minimal_dimension == 8
    zero = [[Q(0) for _ in range(len(W[0]))] for _ in O]
    assert matmul(matmul(O, plus(E, I, -1)), W) == zero
    for T in matrices:
        compressed = matmul(matmul(E, T), E)
        assert matmul(matmul(O, plus(compressed, T, -1)), W) == zero
    return dict(registers=5, physical_dimension=32, physical_rank=8,
                minimal_dimension=minimal_dimension,
                projection='1-(T-1)^3(T-2)^3/8',
                checks=['Boolean-grid pullbacks', 'rank stability',
                        'polynomial retraction', 'observable subquotient identity',
                        'compressed letters preserve observable behavior'])


def binomial_root(T, exponent):
    d = len(T)
    I = identity(d)
    X = plus(T, I, -1)
    assert power(X, d) == [[0]*d for _ in range(d)]
    result, term, coefficient = I, I, Q(1)
    for j in range(1, d):
        term = matmul(term, X)
        coefficient *= (exponent-j+1)/j
        result = plus(result, term, coefficient)
    return result


def control_check():
    I = identity(4)
    A, B = identity(4), identity(4)
    A[0][1] = Q(-2, 3)
    B[1][2], B[2][3] = Q(5, 7), Q(-3, 2)
    letters = (A, B)
    statistics = Counter()
    for n in range(1, 4):
        for flat in product(range(n), repeat=2*n):
            controls = (flat[:n], flat[n:])
            reached, todo = {0}, [0]
            for q in todo:
                for t in controls:
                    if t[q] not in reached:
                        reached.add(t[q]); todo.append(t[q])
            states = sorted(reached)
            id_action = tuple(states)
            monoid = {id_action: ()}
            pending = deque([id_action])
            while pending:
                action = pending.popleft()
                for letter, t in enumerate(controls):
                    following = tuple(t[q] for q in action)
                    if following not in monoid:
                        monoid[following] = monoid[action]+(letter,)
                        pending.append(following)
            smallest = min(monoid, key=lambda t: (len(set(t)), len(monoid[t])))
            r = len(set(smallest)); N = factorial(r)
            e = monoid[smallest]*N

            def action(word, q):
                for letter in word:
                    q = controls[letter][q]
                return q

            image = {action(e, q) for q in states}
            assert len(image) == r and all(action(e, q) == q for q in image)
            q = action(e, 0)  # e is an actual prefix to this image state.
            blocks = [e]+[(e+(letter,)+e)*N for letter in (0, 1)]
            assert all(action(word, q) == q for word in blocks)

            def matrix(word):
                T = I
                for letter in word:
                    T = matmul(T, letters[letter])
                return T

            mats = list(map(matrix, blocks))
            inverse_e = binomial_root(mats[0], Q(-1))
            for letter in (0, 1):
                recovered = matmul(matmul(inverse_e,
                                  binomial_root(mats[letter+1], Q(1, N))), inverse_e)
                assert recovered == letters[letter]
            ip = matmul([[1, 0, 0, 0]], matrix(e))[0]
            assert len(span(ip, mats)) == 4
            assert len(span([0, 0, 0, 1], mats, rows=False)) == 4
            assert any(matmul(X, Y) != matmul(Y, X) for X in mats for Y in mats)
            statistics[r] += 1
    assert sum(statistics.values()) == 746
    return dict(complete_binary_controls=746, states='1 through 3',
                control_minimum_ranks=dict(statistics),
                checks=['idempotent image', 'common return blocks',
                        'polynomial roots recover both original letters',
                        'actual prefix retains full reachability/observability'])


def scattered(word, pattern):
    v = [1]+[0]*len(pattern)
    for a in word:
        for j in range(len(pattern)-1, -1, -1):
            if pattern[j] == a:
                v[j+1] += v[j]
    return v[-1]


def pattern_checks():
    rng = random.Random(811731)
    patterns = [w for n in range(5) for w in product(range(3), repeat=n)]
    words = patterns
    cases = []
    for _ in range(120):
        terms = [(rng.choice(patterns), Q(rng.randint(-3, 3), rng.randint(1, 7)))
                 for _ in range(rng.randrange(10))]
        cases.append(terms)
    for _ in range(40):
        p = rng.choice(patterns)
        c = Q(rng.randint(-5, 5), rng.randint(1, 11))
        cases.append([(u, c) for u in sorted(set(permutations(p)))])
    cases += [[((), Q(2)), ((0,), Q(3)), ((0,), Q(-3))], [],
              [((1,), Q(1)), ((0, 1), Q(1)), ((1, 1), Q(1))]]
    yes = no = values = 0
    for terms in cases:
        coefficients = defaultdict(Q)
        for p, c in terms:
            coefficients[p] += c
        groups = defaultdict(list)
        for p, c in coefficients.items():
            if c:
                groups[tuple(p.count(a) for a in range(3))].append(c)
        oracle = True
        for counts, cs in groups.items():
            size = factorial(sum(counts))
            for m in counts:
                size //= factorial(m)
            oracle &= len(set(cs)) == 1 and len(cs) == size
        value_by_counts = {}
        observed_invariance = True
        for w in words:
            value = sum((c*scattered(w, p) for p, c in terms), Q(0))
            key = tuple(w.count(a) for a in range(3))
            if key in value_by_counts and value_by_counts[key] != value:
                observed_invariance = False
            value_by_counts[key] = value
            if oracle:
                synthesized = Q(0)
                for p, c in terms:
                    if tuple(sorted(p)) == p:
                        term = c
                        for a in range(3):
                            term *= comb(w.count(a), p.count(a))
                        synthesized += term
                assert value == synthesized
            values += 1
        assert oracle == observed_invariance
        yes += bool(oracle); no += not oracle
    return dict(cases=len(cases), alphabet=3, maximum_pattern_length=4,
                evaluated_words_per_case=len(words), yes=yes, no=no,
                exact_evaluations=values,
                checks=['coefficient-class criterion', 'direct subsequence counting',
                        'sorted falling-factorial synthesis', 'cancellation and empty terms'])


def main():
    report = dict(job_id=JOB, arithmetic='exact rational, Python standard library',
                  status='running', limitations=['Finite diagnostics are not a universal proof.'])
    target = Path(__file__).with_suffix('.json')
    for name, fn in [('singular_compression', singular_check),
                     ('finite_control_transfer', control_check),
                     ('explicit_patterns', pattern_checks)]:
        report[name] = fn()
        target.write_text(json.dumps(report, indent=2)+'\n')
    # Individually unipotent generators need not give all-word unipotence.
    A, B = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
    assert sum(matmul(A, B)[i][i] for i in range(2)) == 3
    report['all_word_hypothesis_trap'] = 'I+E12 and I+E21: trace(AB)=3, dimension=2'
    report['status'] = 'passed'
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    target.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))


if __name__ == '__main__':
    main()
