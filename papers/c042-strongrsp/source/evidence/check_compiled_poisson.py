#!/usr/bin/env python3
"""R3 bounded-comparison compiler, exact rational certificates and event tests.

Production routines never use rational numerator division/floor. The reference
weights may have much larger encodings and are validation only.
"""
from fractions import Fraction as F
from collections import Counter
from pathlib import Path
import hashlib
import json

ST = Counter()

def locate(x, top):
    """Largest bounded integer <= x, using comparisons, including endpoints."""
    lo, hi = 0, top + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2  # bounded CONTROL index, not arbitrary-weight floor
        ST['bounded_binary_comparisons'] += 1
        if F(mid) <= x: lo = mid
        else: hi = mid
    return lo

def down(x, b, top=1):
    assert 0 <= x <= top
    return F(locate(x * (1 << b), top * (1 << b)), 1 << b)

def up(x, b, top):
    z = down(x, b, top)
    return z if z == x else z + F(1, 1 << b)

def compiler(mu, q, U, b):
    if mu == 0:
        return [F(1)] * q, F(0), None
    h = F(1, 1 << b)
    mode = locate(mu, U)
    H = 2 * U + b + 2
    w = [F(0)] * (H + 1)
    w[mode] = F(1)
    for k in range(mode, 0, -1): w[k-1] = down(w[k] * k / mu, b)
    for k in range(mode, H): w[k+1] = down(w[k] * mu / (k+1), b)
    Sminus = sum(w)
    E = ((H+1)**2 + 1) * h
    Splus = Sminus + E
    tau = 2 * E + h
    out, partial = [], F(0)
    for j in range(q):
        partial += w[j]
        out.append(down(partial / Splus, b))
    ST['compiled_tables'] += 1
    return out, tau, (mode, H, w, Sminus, Splus)

def reference(mu, q, U, b, data):
    mode, H, low, Sminus, Splus = data
    r = [F(0)] * (H+1)
    r[mode] = 1
    for k in range(mode, 0, -1): r[k-1] = r[k] * k / mu
    for k in range(mode, H): r[k+1] = r[k] * mu / (k+1)
    # Every ratio after H is <= this one; geometric upper tail is rational.
    ratio = mu / (H+1)
    tail = r[H] * ratio / (1-ratio)
    assert tail <= F(1, 1 << b)
    assert all(0 <= a-c <= H * F(1, 1 << b) for a,c in zip(r,low))
    S = sum(r)
    assert Sminus <= S <= S + tail <= Splus
    cumul, lo, hi = F(0), [], []
    for j in range(q):
        cumul += r[j]
        lo.append(cumul / (S+tail))
        hi.append(cumul / S)
    ST['normalizer_certificates'] += 1
    return lo, hi

def pmf(cdf): return [cdf[0]] + [b-a for a,b in zip(cdf,cdf[1:])] + [1-cdf[-1]]

def grid(eta, delta, U, b):
    xs = [delta]
    while xs[-1] < U:
        raw = (1+eta/4) * xs[-1]
        nxt = F(U) if raw >= U else min(F(U), up(raw, b, U))
        assert xs[-1] < nxt <= (1+eta/2)*xs[-1]
        if nxt < U: assert nxt >= (1+eta/4)*xs[-1]
        xs.append(nxt)
    return xs

def main():
    records = []
    for q in (2, 3, 7, 16):
        U, b = 4*q, 48
        means = sorted(set([F(0), F(1,1<<50), F(1,128), F(1,2),
                            F(1)-F(1,1024), F(1), F(1)+F(1,1024),
                            F(q,3), F(q), F(2*q), F(U)-F(1,256), F(U)]))
        prev = [F(1)] * q
        for mu in means:
            cdf,tau,data = compiler(mu,q,U,b)
            if data: lo,hi = reference(mu,q,U,b,data)
            else: lo=hi=[F(1)]*q
            env = [min(x,y) for x,y in zip(prev,cdf)]
            assert env == sorted(env)
            assert all(x <= y for x,y in zip(env,prev))
            assert all(0 <= x <= l <= u <= 1 and u-x <= tau
                       for x,l,u in zip(env,lo,hi))
            law = pmf(env)
            assert min(law)>=0 and sum(law)==1
            assert all((p*(1<<b)).denominator==1 for p in law)
            ST['cdf_coordinate_certificates'] += q
            records.append({'q':q,'mean':str(mu),'bits':b,'cdf':list(map(str,env)),
                            'tau':str(tau),'normalizer_tail_certified':bool(data)})
            prev = env
    # Adversarial bounded dyadic grid, actual event direction and extreme aspects.
    event_records=[]
    for eta in (F(1,4), F(1,16)):
        n,q,delta,b=8,8,F(1,1<<16),28
        xs=grid(eta,delta,4*q,b)
        for total,maxedge in [(F(1),F(1,7)),(F(1,1<<200),F(1,7*(1<<200))),
                              (F(1<<200),F(1<<200,7)),(F(5,3),F(5,3))]:
            raw=q*maxedge/((1+4*eta)*total)
            a=max(x for x in xs if x<=raw)
            event=q*maxedge/((1+4*eta)*a)
            assert total<=event<=(1+eta/2)*total
            event_records.append({'eta':str(eta),'length_optimum':str(total),
                                  'max_edge':str(maxedge),'covering_event':str(event),
                                  'grid_size':len(xs)})
        # Explicit mean quantization and grid monotonicity, using all grid cells.
        for j in range(1,len(xs)):
            for raw in (xs[j], (xs[j]+xs[j-1])/2):
                rounded=next(x for x in xs if x>=raw)
                assert raw<=rounded<=(1+eta/2)*raw+delta
                ST['mean_rounding_checks']+=1
    out={'job_id':'c042-strongrsp-research-a3a11d57c4b5',
         'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
         'all_checks_passed':True,'statistics':dict(ST),'tables':records,
         'event_records':event_records,
         'scope':'Finite exact rational checks; compiler rounding is bounded binary comparison. '
                 'Reference uses unrounded relative-mode rational weights plus a rigorous geometric tail, '
                 'not an exponential oracle. q=2,3,7,16, specified means, eta=1/4,1/16 event fixtures. '
                 'This alone is neither a universal theorem nor a full RSP resolution.'}
    Path('evidence/compiled-poisson-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('tables','event_records')}))

if __name__=='__main__': main()
