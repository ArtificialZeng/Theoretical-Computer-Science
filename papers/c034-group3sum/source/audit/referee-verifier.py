"""Independent exact, finite referee checks; not an asymptotic proof.

Uses explicit finite groups and literal support matrices.  It imports no proposer
code and writes only its own audit output.
"""
import hashlib
import itertools as it
import json
import math
import random
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

JOB = "c034-group3sum-referee-f77368142a77"
rng = random.Random(77368142)
stats = Counter()

def divisors(m):
    return [d for d in range(2, m + 1) if m % d == 0]

def prime_divisors(m):
    return [p for p in divisors(m) if all(p % z for z in range(2, p))]

def plus(m, *xs):
    return tuple(sum(a) % m for a in zip(*xs))

def neg(m, x):
    return tuple(-a % m for a in x)

def row(m, u, x):
    return sum(a * b for a, b in zip(u, x)) % m

def order(m, x):
    # Determine order by repeated addition, independently of the dot-image formula.
    z = (0,) * len(x)
    a = z
    for d in range(1, m + 1):
        a = plus(m, a, x)
        if a == z:
            return d
    raise AssertionError("missing finite order")

# Exhaustive one-row laws, with output distributions rather than only zero counts.
for m in [2, 3, 4, 6, 8, 9, 10, 12, 18]:
    g = list(it.product(range(m), repeat=2))
    for v in g:
        d = order(m, v)
        hist = Counter(row(m, u, v) for u in g)
        assert set(hist) == set(range(0, m, m // d))
        assert set(hist.values()) == {len(g) // d}
        for p in prime_divisors(m):
            reduced = Counter(row(m, u, v) % (m // p) for u in g)
            image_size = d // math.gcd(d, p)
            assert len(reduced) == image_size
            assert set(reduced.values()) == {len(g) // image_size}
            stats["reduced_row_distributions"] += 1
        stats["full_row_distributions"] += 1

# Full profiles on original lists; enumerate every subinstance and its sum orders.
for m in [4, 6, 8, 12]:
    g = list(it.product(range(m), repeat=2))
    ds = divisors(m)
    for trial in range(8):
        lists = [rng.sample(g, min(len(g), 14)) for _ in range(3)]
        n = max(map(len, lists))
        profiles = []
        for s in lists:
            buckets = defaultdict(list)
            for x in s:
                sizes = [sum(all((a - b) % (m // d) == 0 for a, b in zip(x, y))
                             for y in s) for d in ds]
                buckets[tuple(2 ** (z.bit_length() - 1) for z in sizes)].append(x)
            profiles.append(buckets)
        for entries in it.product(*(b.items() for b in profiles)):
            sizes = {d: min(entries[i][0][j] for i in range(3))
                     for j, d in enumerate(ds)}
            sublists = [a[1] for a in entries]
            counts = Counter(order(m, plus(m, *t)) for t in it.product(*sublists))
            for d in ds:
                total = sum(v for f, v in counts.items() if d % f == 0)
                assert total < 2 * sizes[d] * n * n
                for i, s in enumerate(sublists):
                    cosets = {tuple(a % (m // d) for a in x) for x in s}
                    assert len(cosets) * entries[i][0][ds.index(d)] <= n
            R, sigma = 8, 2  # diagnostic scale, explicitly not an asymptotic test
            ell = 0
            while any(d ** ell * sigma < sizes[d] * R for d in ds):
                ell += 1
            e = next(d for d in ds if d ** (ell - 1) * sigma < sizes[d] * R)
            p = prime_divisors(e)[0]
            q = 0
            while p ** (q + 1) <= R:
                q += 1
            D = p ** q
            assert e ** ell < e * sizes[e] * Fraction(R, sigma)
            EF = sum(Fraction(v, d ** ell) for d, v in counts.items()
                     if d > 1 and e % d == 0)
            EZ = sum(Fraction(v * math.gcd(d, p) ** q, d ** ell)
                     for d, v in counts.items() if d > 1 and e % d == 0)
            assert EF <= Fraction(2 * len(ds) * sigma * n * n, R)
            assert EZ <= D * EF <= 2 * len(ds) * sigma * n * n
            stats["profile_subinstances"] += 1

# Literal 0/1 matrices, all their entries, all probes, and failed-scan charging.
for m in [2, 4, 6, 8, 9, 12]:
    g = list(it.product(range(m), repeat=2))
    zero = (0, 0)
    for trial in range(24):
        e = rng.choice(divisors(m))
        p = rng.choice(prime_divisors(e))
        q = 1 + trial % 2
        k = trial % 3
        ell = k + q
        rows = [rng.choice(g) for _ in range(ell)]
        def K(x):
            return tuple(a % (m // e) for a in x) + tuple(row(m, u, x) for u in rows)
        def pi(x):
            return (tuple(a % (m // e) for a in x)
                    + tuple(row(m, u, x) for u in rows[:k])
                    + tuple(row(m, u, x) % (m // p) for u in rows[k:]))
        def bvalue(x):
            v = K(x)
            assert not any(v[:2 + k])
            assert all(a % (m // p) == 0 for a in v[2 + k:])
            return tuple(a // (m // p) for a in v[2 + k:])
        assert all((pi(x) != pi(zero)) or len(bvalue(x)) == q for x in g)
        lists = [rng.sample(g, min(len(g), 10)) for _ in range(3)]
        sigma = 1 + trial % 3
        blocks = []
        classes = []
        for s in lists[1:]:
            cc = defaultdict(list)
            for x in s:
                cc[pi(x)].append(x)
            classes.append(cc)
            blocks.append([a[j:j + sigma] for a in cc.values()
                           for j in range(0, len(a), sigma)])
        cut = (q + 1) // 2
        B = list(it.product(range(p), repeat=q))
        B1 = list(it.product(range(p), repeat=cut))
        B2 = list(it.product(range(p), repeat=q - cut))
        left = [(i, u) for i in range(len(blocks[0])) for u in B1]
        right = [(j, v) for j in range(len(blocks[1])) for v in B2]
        X = {}
        Y = {}
        for i, u in left:
            X[i, u] = {plus(p, bvalue(plus(m, x, neg(m, blocks[0][i][0]))),
                                   u + (0,) * (q - cut)) for x in blocks[0][i]}
        for j, v in right:
            Y[j, v] = {neg(p, plus(p, bvalue(plus(m, x, neg(m, blocks[1][j][0]))),
                                      (0,) * cut + v)) for x in blocks[1][j]}
        product_entries = {(i, u, j, v): sum(int(t in X[i, u]) * int(t in Y[j, v]) for t in B)
                           for i, u in left for j, v in right}
        n = max(map(len, lists))
        Zpi = sum(pi(plus(m, *t)) == pi(zero) for t in it.product(*lists))
        F = sum(plus(m, *t) != zero and K(plus(m, *t)) == K(zero)
                for t in it.product(*lists))
        probes = 0
        failures = 0
        for x in lists[0]:
            for i, b in enumerate(blocks[0]):
                for j, c in enumerate(blocks[1]):
                    v = plus(m, x, b[0], c[0])
                    if pi(v) != pi(zero):
                        continue
                    probes += 1
                    target = bvalue(v)
                    yes = product_entries[i, target[:cut], j, target[cut:]] > 0
                    hashed = any(K(plus(m, x, y, z)) == K(zero) for y in b for z in c)
                    actual = any(plus(m, x, y, z) == zero for y in b for z in c)
                    assert yes == hashed
                    assert not actual or yes
                    failures += bool(yes and not actual)
        assert failures <= F
        assert probes <= n * len(classes[0]) + Fraction(2 * n * n, sigma) + Fraction(Zpi, sigma ** 2)
        stats["support_instances"] += 1
        stats["literal_product_entries"] += len(product_entries)
        stats["probes_checked"] += probes
        stats["failed_probes_checked"] += failures

snapshot = json.loads(Path("audit/snapshot.json").read_text())
for path, digest in snapshot["files"].items():
    assert hashlib.sha256(Path(path).read_bytes()).hexdigest() == digest, path
out = {"job_id": JOB, "snapshot_digest": snapshot["digest"],
       "status": "all_exact_assertions_passed", "counts": dict(stats),
       "limits": ["Finite algebra/interface checks only; no proof of an asymptotic bound or priority.",
                  "The matrix primitive is checked by its published theorem statement, not reimplemented here.",
                  "The independent derivation of costs and success probability is in audit/math.md."]}
Path("audit/referee-verifier-results.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out))
