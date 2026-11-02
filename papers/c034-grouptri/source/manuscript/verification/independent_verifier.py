"""Fresh finite checks. No imports from, or writes to, frozen candidate evidence.

Brute-force relations and prime solvers certify finite semantics only, not speed.
"""
import hashlib
import itertools as it
import json
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path

JOB = 'c034-grouptri-referee-e6a7f319b8fe'
STATS = Counter()
RNG = random.Random(703411)


def pf(m):
    return next(p for p in range(2, m + 1) if m % p == 0)


def vec(a, b, m, sign=1):
    return tuple((x + sign*y) % m for x, y in zip(a, b))


def zeros(tables, sizes, m):
    a, b, c = tables
    return {(i, k, j) for i, k, j in it.product(*(range(z) for z in sizes))
            if vec(a[i, k], b[k, j], m) == c[i, j]}


def verify_listing():
    # An iterative stack traversal, with arbitrary Boolean relations and
    # leaf cutoffs. Each popped cube receives a fresh dynamic-mask query.
    for sizes in it.product(range(4), repeat=3):
        triples = list(it.product(*(range(z) for z in sizes)))
        for mode in range(8):
            rel = {t for t in triples if RNG.randrange(4) <= mode % 4}
            n = max(1, *sizes)
            N = 1 << (n - 1).bit_length()
            cap = 1 + mode % (n+1)
            cut = (1, 2, 4)[mode % 3]
            count = Counter()
            outputs = set()
            stack = [(tuple(range(N)),) * 3]
            positive_leaves = 0
            while stack:
                I, J, K = stack.pop()
                active = lambda t: t in rel and count[t[:2]] < cap
                if not any(active(t) for t in it.product(I, J, K)):
                    continue
                if len(I) <= cut:
                    before = len(outputs)
                    for t in it.product(I, J, K):
                        if active(t):
                            assert t not in outputs
                            outputs.add(t)
                            count[t[:2]] += 1
                    assert len(outputs) > before
                    positive_leaves += 1
                else:
                    h = len(I)//2
                    children = list(it.product((I[:h], I[h:]),
                                               (J[:h], J[h:]),
                                               (K[:h], K[h:])))
                    RNG.shuffle(children)
                    stack.extend(children)
            for i, j in it.product(range(sizes[0]), range(sizes[1])):
                assert count[i, j] == min(cap, sum(t[:2] == (i, j) for t in rel))
            assert positive_leaves <= len(outputs)
            STATS['listing_instances'] += 1


def verify_local_lifts():
    for m in range(4, 37):
        for p in range(2, m):
            if m % p or pf(p) != p:
                continue
            q = m//p
            # Exhaust every potential triple and every three kernel offsets.
            for alpha, beta, tau in it.product(range(p), repeat=3):
                for x, y, z in it.product(range(q), repeat=3):
                    a = (alpha + tau + p*x) % m
                    b = (beta - tau + p*y) % m
                    c = (alpha + beta + p*z) % m
                    residual = ((a-alpha-tau) % m,
                                (b-beta+tau) % m,
                                (c-alpha-beta) % m)
                    assert all(v % p == 0 for v in residual)
                    aa, bb, cc = (v//p for v in residual)
                    assert ((a+b-c) % m == 0) == ((aa+bb-cc) % q == 0)
                    STATS['local_gauge_kernel_cases'] += 1
    for q in range(2, 37):
        for present in it.product((False, True), repeat=3):
            for plus_labels in it.product(range(q), repeat=3):
                encoded = [((plus_labels[k] if present[k] else 0),)
                           + tuple(int(not present[k] and k == t) for t in range(3))
                           for k in range(3)]
                answer = all(sum(e[t] for e in encoded) % q == 0 for t in range(4))
                assert answer == (all(present) and sum(plus_labels) % q == 0)
                STATS['complete_mask_cases'] += 1


def verify_graphs():
    # Directly construct witness sets to separate this check of decomposition
    # and lifting from the independently checked listing implementation.
    for m in (4, 6, 8, 9, 10, 12, 16, 18, 25, 27, 30, 36):
        p, q = pf(m), m//pf(m)
        for case in range(30):
            sizes = (RNG.randrange(1, 7), RNG.randrange(1, 7), RNG.randrange(1, 7))
            n, d = max(sizes), 1 + case % 3
            s = RNG.randrange(1, n+1)
            random_v = lambda modulus: tuple(RNG.randrange(modulus) for _ in range(d))
            a = {(i,k): random_v(m) for i,k in it.product(range(sizes[0]), range(sizes[1]))}
            b = {(k,j): random_v(m) for k,j in it.product(range(sizes[1]), range(sizes[2]))}
            c = {(i,j): random_v(m) for i,j in it.product(range(sizes[0]), range(sizes[2]))}
            if case % 3:
                u = [random_v(p) for _ in range(sizes[0])]
                v = [random_v(p) for _ in range(sizes[2])]
                t = [random_v(p) for _ in range(sizes[1])]
                for table, base in ((a, lambda i,k: vec(u[i],t[k],p)),
                                    (b, lambda k,j: vec(v[j],t[k],p,-1)),
                                    (c, lambda i,j: vec(u[i],v[j],p))):
                    for e in table:
                        residue = base(*e)
                        table[e] = tuple(z + p*RNG.randrange(q) for z in residue)
            qa, qb, qc = [{e: tuple(x % p for x in w) for e,w in table.items()}
                          for table in (a,b,c)]
            quotient_truth = zeros((qa,qb,qc), sizes, p)
            original_truth = zeros((a,b,c), sizes, m)
            cap = n//s + 1
            witnesses = {(i,j): sorted(k for ii,k,jj in quotient_truth if (ii,jj)==(i,j))
                         for i,j in c}
            few = {t for t in quotient_truth if len(witnesses[t[0],t[2]]) < cap}
            stored = {}
            for ij, ks in witnesses.items():
                if len(ks) >= cap:
                    RNG.shuffle(ks)
                    stored[ij] = set(ks[:cap])
            pivots = {}
            while stored:
                score = Counter(k for ks in stored.values() for k in ks)
                h = min(score, key=lambda k: (-score[k], k))
                for ij in list(stored):
                    if h in stored[ij]:
                        pivots[ij] = h
                        del stored[ij]
            membership = Counter(few)
            for h in sorted(set(pivots.values())):
                slots = {}
                for k in range(sizes[1]):
                    f = Counter(vec(qb[h,j],qb[k,j],p,-1) for j in range(sizes[2]))
                    slots[k] = sorted(v for v,z in f.items() if z*s*s > n)
                for i,k,j in quotient_truth - few:
                    if pivots[i,j] == h and vec(qa[i,k],qa[i,h],p,-1) not in slots[k]:
                        membership[i,k,j] += 1
                for l in range(s*s):
                    tau = {k: slots[k][l] for k in slots if l < len(slots[k])}
                    e1 = {(i,k) for i,k in a if k in tau and vec(qa[i,k],qa[i,h],p,-1)==tau[k]}
                    e2 = {(k,j) for k,j in b if k in tau and vec(qb[h,j],qb[k,j],p,-1)==tau[k]}
                    e3 = {ij for ij in c if pivots.get(ij)==h}
                    triangles = {(i,k,j) for i,k,j in it.product(*(range(z) for z in sizes))
                                 if (i,k) in e1 and (k,j) in e2 and (i,j) in e3}
                    membership.update(triangles)
                    result = []
                    for kind, (table, edges) in enumerate(zip((a,b,c),(e1,e2,e3))):
                        new = {}
                        for e,w in table.items():
                            if e not in edges:
                                plus = (0,)*d + tuple(int(kind==t) for t in range(3))
                            else:
                                if kind == 0:
                                    i,k=e
                                    residue=vec(vec(w,qa[i,h],m,-1),tau[k],m,-1)
                                elif kind == 1:
                                    k,j=e
                                    residue=vec(vec(w,qb[h,j],m,-1),tau[k],m)
                                else:
                                    i,j=e
                                    residue=vec(vec(w,qa[i,h],m,-1),qb[h,j],m,-1)
                                assert all(z % p == 0 for z in residue)
                                plus=tuple((z//p if kind<2 else -z//p) % q for z in residue)+(0,0,0)
                            new[e] = plus if kind<2 else tuple(-z % q for z in plus)
                        result.append(new)
                    assert zeros(result,sizes,q) == original_truth & triangles
                    STATS['explicit_kernel_instances'] += 1
            assert set(membership)==quotient_truth
            assert all(z==1 for z in membership.values())
            STATS['graph_decompositions'] += 1


def verify_exponents():
    delta={}
    e=Fraction(1,1000)
    for m in range(2,2049):
        p=pf(m)
        delta[m] = e if p==m else delta[m//p]/144000
        if p != m:
            theta=delta[m//p]/12
            raw=e*theta/6
            assert delta[m]==raw/2
            assert min(theta,1-theta,1-3*theta,delta[m//p]-3*theta)>=raw
        STATS['exact_cost_ledger_cases'] += 1


if __name__ == '__main__':
    verify_listing()
    verify_local_lifts()
    verify_graphs()
    verify_exponents()
    result={
        'job_id':JOB,
        'snapshot_digest':'05aa22d3dd75b43826bffb43bc7976a87898d16ab67f0597c8e4a686ca39b771',
        'status':'passed', 'seed':703411, 'counts':dict(STATS),
        'coverage':{
            'listing':'All size triples in {0,1,2,3}^3, eight seeded arbitrary Boolean relations each; varying caps, cutoffs and shuffled depth-first child orders.',
            'local_lifts':'Every proper prime divisor p of each composite M<=36, all p^3 potential triples and (M/p)^3 kernel-offset triples in one coordinate.',
            'masks':'All q in [2,36], all 8 edge-presence patterns, all q^3 one-coordinate plus-label triples.',
            'graphs':'360 seeded complete inputs of sides 1..6, dimensions 1..3, twelve listed composite moduli, independent randomized capped witness subsets; ordinary and dense-gauge quotient modes.',
            'exponents':'Exact rational ledger for every M in [2,2048].'
        },
        'limits':'Finite semantic checks with brute-force detectors; no asymptotic benchmark or formal proof. No proposer test code imported or frozen file changed.',
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }
    Path('audit/independent-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
