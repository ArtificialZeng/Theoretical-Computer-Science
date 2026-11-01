"""Fresh exact certificate and adversarial checks; no frozen files are written.

The saved-certificate checks do not import any research implementation. New
stress tests import only the candidate optimizer and check its output directly.
Run from the project root with: python3 -B audit/referee_verify.py
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[1]
JOB = 'robust-stopping-referee-1afb6017baeb'


def cost(b, t, x):
    return x if x < t else b + t - 1


def check_full(b, R, p, out):
    assert isinstance(b, int) and b >= 2
    assert R >= F(b**b, b**b - (b-1)**b)
    assert p and all(x >= 1 and v >= 0 for x, v in p.items())
    assert sum(p.values()) == 1
    f, lam, alpha, y = (out[k] for k in ('policy', 'lam', 'alpha', 'y'))
    assert f and all(isinstance(t, int) and t >= 1 and v >= 0 for t,v in f.items())
    assert sum(f.values()) == 1
    assert lam >= 0 and set(y) == set(range(1,b)) and min(y.values()) >= 0
    mu = sum(v*(t-1) for t,v in f.items())
    assert mu <= (R-1)*b
    for x in range(1,b):
        assert sum(v*cost(b,t,x) for t,v in f.items()) <= R*x
    # The preceding exact prefixes, together with b+mu <= Rb, prove all x.
    # Directly check additional horizons without using prefix coefficients.
    for x in set(f) | {b, b+1, max(f)+1}:
        assert sum(v*cost(b,t,x) for t,v in f.items()) <= R*min(x,b)
    g = lambda t: sum(v*cost(b,t,x) for x,v in p.items())
    allowed = set(range(1,b+1)) | {x+1 for x,v in p.items() if v and x >= b}
    assert set(f) <= allowed
    assert sum(t >= b for t in f) <= 2
    # On every tail interval between positive forecast atoms, g(t)+lam(t-1)
    # has nonnegative slope. Its left endpoint suffices. Prefix days are
    # checked separately; this proves every omitted positive integer t.
    test_days = allowed | {x for x,v in p.items() if v and x >= b}
    for t in test_days:
        lhs = g(t) + lam*(t-1) + sum(
            (b+t-1-x)*v for x,v in y.items() if x >= t)
        assert lhs >= alpha, (b, R, p, t, lhs, alpha)
    primal = sum(v*g(t) for t,v in f.items())
    dual = alpha - (R-1)*sum(x*v for x,v in y.items()) - lam*(R-1)*b
    assert primal == dual
    assert lam*(mu-(R-1)*b) == 0
    return primal


def check_linear(b, R, c, f, alpha, y):
    assert f and set(f) <= set(c)
    assert sum(f.values()) == 1 and min(f.values()) >= 0
    assert set(y) == set(range(1,b)) and min(y.values()) >= 0
    for x in range(1,b):
        assert sum(v*cost(b,t,x) for t,v in f.items()) <= R*x
    for t in c:
        assert c[t]+sum((b+t-1-x)*v for x,v in y.items() if x>=t) >= alpha
    assert sum(c[t]*v for t,v in f.items()) == (
        alpha-(R-1)*sum(x*v for x,v in y.items()))


def decode_result(o):
    return {'policy': {int(t):F(v) for t,v in o['policy'].items()},
            'lam':F(o['lam']), 'alpha':F(o['alpha']),
            'y':{int(t):F(v) for t,v in o['y'].items()}}


def snapshot_check():
    s = json.loads((ROOT/'audit/snapshot.json').read_text())
    assert all(hashlib.sha256((ROOT/n).read_bytes()).hexdigest()==h
               for n,h in s['files'].items())
    d = hashlib.sha256(json.dumps(s['files'], sort_keys=True,
                         separators=(',',':'), ensure_ascii=False).encode()).hexdigest()
    assert d == s['digest']
    return s


def main():
    snap = snapshot_check()
    counts = {}
    for name in ('oracle-test-cases.json','bisection-test-cases.json'):
        recs = json.loads((ROOT/'evidence'/name).read_text())
        for rec in recs:
            p = {int(t):F(v) for t,v in rec['p'].items()}
            assert check_full(rec['b'],F(rec['R']),p,decode_result(rec['result'])) == F(rec['value'])
        counts[name] = len(recs)
    recs = json.loads((ROOT/'evidence/linear-oracle-test-cases.json').read_text())
    for z in recs:
        c,f,y = ({int(t):F(v) for t,v in z[k].items()} for k in ('costs','policy','y'))
        check_linear(z['b'],F(z['R']),c,f,F(z['alpha']),y)
    counts['linear-oracle-test-cases.json'] = len(recs)

    sys.path.insert(0,str(ROOT/'evidence'))
    from prefix_oracle import optimize, linear_oracle
    rng = random.Random(0x1afb6017)
    signed = 0
    # Exhaustive repeated costs force simultaneous activations and cap ties.
    for b in range(2,6):
        for R in (F(3,2),F(b),F(13,2)):
            for cs in product((-1,0,1),repeat=b+1):
                c={t:F(v) for t,v in enumerate(cs,1)}
                f,alpha,y,_=linear_oracle(b,R,c)
                check_linear(b,R,c,f,alpha,y)
                signed += 1

    mass_ties = 0
    # Choose r so an explicitly prescribed raw prefix schedule has mass 1.
    for b in range(2,10):
        a=b-1
        for k in range(1,min(3,a)+1):
            for B in combinations(range(1,b),k):
                factor=F(1);last=0
                for i in B:
                    factor *= 1+F(i-last,a);last=i
                R=1+1/(factor-1)
                c={t:F(0 if t in B else 2) for t in range(1,b+2)}
                f,alpha,y,_=linear_oracle(b,R,c)
                check_linear(b,R,c,f,alpha,y)
                assert sum(v for t,v in f.items() if t<b)==1
                mass_ties += 1

    random_full = 0
    max_calls = 0
    for j in range(360):
        b=rng.randrange(2,18)
        rho=F(b**b,b**b-(b-1)**b)
        R=(rho, rho+F(1,10**8), F(2), F(b), F(11,2))[j%5]
        xs=sorted(set(rng.randrange(1,3*b+7) for _ in range(rng.randrange(1,9))))
        if j%11==0:
            xs.append(10**(10+j%17)+j)
        ws=[rng.randrange(1,17) for _ in xs]
        p={x:F(w,sum(ws)) for x,w in zip(xs,ws)}
        p[10**35+j]=F(0)  # Zero atoms must not enlarge the candidate support.
        o=optimize(b,R,p)
        check_full(b,R,p,o)
        random_full += 1
        max_calls=max(max_calls,o['calls'])
        if j%90==0:
            print(json.dumps({'completed_random_full':j+1}),flush=True)

    fallback=[]
    for b,R,p in [(2,F(4,3),{1:F(1)}),
                  (3,F(3,2),{1:F(2,5),2:F(3,5)}),
                  (6,F(7,4),{2:F(2,7),5:F(1,7),19:F(4,7)})]:
        o=optimize(b,R,p,max_chord_probes=0)
        val=check_full(b,R,p,o)
        fast=optimize(b,R,p)
        assert val==check_full(b,R,p,fast)
        fallback.append({'b':b,'R':str(R),'value':str(val),
                         'isolation_steps':o['isolation_steps'],'calls':o['calls']})
    # Independently recompute the exact conceptual separation.
    b,R,p=3,F(3,2),{1:F(2,5),2:F(3,5)}
    g=lambda t:sum(v*cost(b,t,x) for x,v in p.items())
    assert [g(t) for t in (1,2,3)]==[F(3),F(14,5),F(8,5)]
    K=(R-1)*b
    assert all(g(t)>=3-F(7,10)*(t-1) for t in (1,2,3))
    assert all(g(t)>=4-F(6,5)*(t-1) for t in (2,3))
    assert 3-F(7,10)*K==F(39,20)
    assert 4-F(6,5)*K==F(11,5)
    snapshot_check()
    summary={'job_id':JOB,'snapshot_digest':snap['digest'],
             'frozen_files_verified':len(snap['files']),
             'serialized_certificates_verified':counts,
             'new_exhaustive_signed_tie_cases':signed,
             'new_exact_prefix_mass_one_cases':mass_ties,
             'new_random_full_certificates':random_full,
             'new_default_max_calls':max_calls,
             'new_forced_bisection':fallback,
             'counterexample_values':['39/20','14/5','11/5'],
             'arithmetic':'fractions.Fraction only; all inequalities exact',
             'scope':'Fresh deterministic arithmetic checks, combined with the analytic audit; finite tests alone do not prove the quantified theorem.'}
    (ROOT/'audit/referee-checks.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
