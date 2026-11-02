#!/usr/bin/env python3
"""Exact, bounded 2-good-chain experiment. Run from project root."""
import hashlib
import itertools
import json
import random
from fractions import Fraction as Q
from pathlib import Path

OUT = Path('evidence/research-pass-1')
SEED = 25025393

def enc(x):
    if isinstance(x, Q):
        return str(x)
    raise TypeError(type(x).__name__)

def coverage(masks, weights):
    n = len(masks)
    unions = [0] * (1 << n)
    vals = [Q(0)] * (1 << n)
    for s in range(1, 1 << n):
        b = s & -s
        unions[s] = unions[s ^ b] | masks[b.bit_length()-1]
        vals[s] = sum((Q(w) for j, w in enumerate(weights) if unions[s] >> j & 1), Q(0))
    return vals

def verify_function(v, n):
    assert v[0] == 0 and all(x >= 0 for x in v)
    # All diminishing-return inequalities with adjacent supersets suffice.
    for s in range(1 << n):
        for i in range(n):
            if s >> i & 1:
                continue
            assert v[s | (1 << i)] >= v[s]
            for j in range(i+1, n):
                if not s >> j & 1:
                    assert v[s | (1 << i)] + v[s | (1 << j)] >= v[s] + v[s | (1 << i) | (1 << j)]

def analyze(name, h, g, desc, perm_check=False):
    n = (len(h)-1).bit_length()
    N = (1 << n)-1
    verify_function(h, n)
    verify_function(g, n)
    f = [h[s]+g[N ^ s] for s in range(N+1)]
    opt = [max(f[s] for s in range(N+1) if s.bit_count() == k) for k in range(n+1)]
    good = [2*f[s] >= opt[s.bit_count()] for s in range(N+1)]
    reach, back = [False]*(N+1), [False]*(N+1)
    parent = [None]*(N+1)
    reach[0] = True
    for s in range(1,N+1):
        if good[s]:
            for i in range(n):
                if s >> i & 1 and reach[s ^ (1 << i)]:
                    reach[s], parent[s] = True, s ^ (1 << i)
                    break
    back[N] = True
    for s in range(N-1,-1,-1):
        back[s] = good[s] and any(back[s | (1 << i)] for i in range(n) if not s >> i & 1)
    dead = [s for s in range(N) if reach[s] and not any(good[s | (1 << i)] for i in range(n) if not s >> i & 1)]
    trapped = [s for s in range(N) if reach[s] and not back[s]]
    chain = []
    s = N
    if reach[N]:
        while s:
            p = parent[s]
            chain.append((s ^ p).bit_length()-1)
            s = p
        chain.reverse()
        s = 0
        for i in chain:
            s |= 1 << i
            assert good[s]
    if perm_check:
        brute = 0
        for p in itertools.permutations(range(n)):
            s, ok = 0, True
            for i in p:
                s |= 1 << i
                if not good[s]:
                    ok = False
                    break
            brute += int(ok)
        assert bool(brute) == reach[N]
    else:
        brute = None
    return dict(name=name,n=n,description=desc,h=h,g=g,f=f,opt=opt,good=good,
                reachable=reach,can_finish=back,parent=parent,chain=chain,
                complete_chain=reach[N],dead_ends=dead,trapped_reachable=trapped,
                permutation_good_count=brute)

def source_cases():
    scales = [Q(1,4),Q(1,2),Q(1),Q(2),Q(4)]
    for n in range(2,9):
        # Prop.11 at curvature 1: star item 0 covers all n-1 atoms.
        masks = [(1 << (n-1))-1]+[1 << i for i in range(n-1)]
        v = coverage(masks, [1]*(n-1))
        for scale in scales:
            yield f'prop11-n{n}-scale{scale}',v,[scale*x for x in v],dict(family='Prop11-c1',masks=masks,g_scale=scale)
    for k in (2,3):
        U = list(itertools.product(range(1,k+1),repeat=k))
        masks = [sum(1 << j for j,t in enumerate(U) if t[-1] == i) for i in range(1,k+1)]
        masks += [sum(1 << j for j,t in enumerate(U) if t[i] == k) for i in range(k)]
        h = coverage(masks,[1]*len(U))
        weights = [0]*k+[(k-1)**(i-1)*k**(k-i) for i in range(1,k+1)]
        g = [Q(sum(weights[i] for i in range(2*k) if s >> i & 1)) for s in range(1 << (2*k))]
        for scale in scales:
            for swap in (False,True):
                a,b = h,[scale*x for x in g]
                if swap:
                    a,b = b,a
                yield f'prop19-k{k}-scale{scale}-swap{int(swap)}',a,b,dict(family='Prop19',k=k,masks=masks,modular_weights=weights,g_scale=scale,swapped=swap,labeled_duplicate_items=True)

def random_cases():
    rng = random.Random(SEED)
    for z in range(200):
        n = 1+z%8
        U = rng.randint(1,12)
        funcs, desc = [],dict(family='seeded-weighted-coverage',seed=SEED,index=z,universe_size=U)
        for key in ('h','g'):
            density = rng.choice([Q(1,8),Q(1,4),Q(1,2),Q(3,4)])
            masks = [sum(1 << j for j in range(U) if rng.randrange(density.denominator) < density.numerator) for i in range(n)]
            weights = [rng.randint(1,5) for j in range(U)]
            if (z%29 == 0 and key == 'h') or (z%31 == 0 and key == 'g'):
                masks = [0]*n
            funcs.append(coverage(masks,weights))
            desc[key] = dict(masks=masks,weights=weights)
        yield f'random-{z:03d}',*funcs,desc

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    results=[]
    for name,h,g,desc in itertools.chain(source_cases(),random_cases()):
        r = analyze(name,h,g,desc,perm_check=len(h)<=64)
        results.append(r)
        if not r['complete_chain']:
            break
    raw=json.dumps(results,default=enc,indent=2)
    (OUT/'chain-tables.json').write_text(raw+'\n')
    summary=dict(seed=SEED,case_count=len(results),source_cases=sum(r['description']['family']!='seeded-weighted-coverage' for r in results),random_cases=sum(r['description']['family']=='seeded-weighted-coverage' for r in results),no_chain=[r['name'] for r in results if not r['complete_chain']],local_dead_ends=[dict(name=r['name'],sets=r['dead_ends']) for r in results if r['dead_ends']],trapped_reachable=[dict(name=r['name'],sets=r['trapped_reachable']) for r in results if r['trapped_reachable']],permutation_verified_count=sum(r['permutation_good_count'] is not None for r in results),tables_sha256=hashlib.sha256((raw+'\n').encode()).hexdigest(),scope='Finite instances only. Source family universes may exceed 12; random universes <=12. No universal theorem.')
    (OUT/'chain-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    main()
