"""Exact adversarial tests. Enumeration is from the earlier, separate module.

Frozen test plan: all b=2,3,4, all distinct two-point horizons <=6 with
weights 1/5,...,4/5, and all one-hot horizons <=6, for R=rho_b,3/2,2.
Held-out tests: b=5, forecasts with >=3 atoms; arbitrary signed prefix costs;
boundaries and larger b certified by dual inequalities, without enumeration.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json
import random
from pathlib import Path
from prefix_oracle import optimize, verify, linear_oracle, forecast_costs, objective
from triage_exact import vertices, solve


def encode(x):
    if isinstance(x,Q): return str(x)
    if isinstance(x,dict): return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x


def relaxed_vertices(b,R,M):
    """Independent generic basis enumeration, omitting the moment row."""
    A=[[Q(b+t-1-x) if t<=x else Q(0) for t in range(1,M+1)]
       for x in range(1,b)]
    rhs=[(R-1)*x for x in range(1,b)]
    out=set()
    for k in range(1,min(b,M)+1):
        for s in combinations(range(M),k):
            for active in combinations(range(b-1),k-1):
                mat=[[Q(1)]*k]+[[A[j][t] for t in s] for j in active]
                v=solve(mat,[Q(1)]+[rhs[j] for j in active])
                if v is None or min(v)<0: continue
                f=tuple(v[s.index(t)] if t in s else Q(0) for t in range(M))
                if all(sum(x*y for x,y in zip(row,f))<=cap
                       for row,cap in zip(A,rhs)): out.add(f)
    return sorted(out)


def main():
    records=[]
    coverage=[]
    max_calls=0
    for b in (2,3,4):
        rho=Q(b**b,b**b-(b-1)**b)
        for R in (rho,Q(3,2),Q(2)):
            vv=vertices(b,R,7)
            forecasts=[{x:Q(1)} for x in range(1,7)]
            forecasts += [{x:Q(a,5),y:Q(5-a,5)}
                          for x,y in combinations(range(1,7),2) for a in range(1,5)]
            for p in forecasts:
                r=optimize(b,R,p)
                val=verify(b,R,p,r)
                g=forecast_costs(b,p,range(1,8))
                expected=min(sum(g[t]*f[t-1] for t in range(1,8)) for f in vv)
                assert val==expected,(b,R,p,val,expected)
                records.append(dict(family='specified-small',b=b,R=R,p=p,
                                    value=val,result=r))
                max_calls=max(max_calls,r['calls'])
            coverage.append(dict(b=b,R=str(R),M=7,vertices=len(vv),cases=len(forecasts)))
            print('completed',b,str(R),len(forecasts),flush=True)
            Path('evidence/oracle-test-cases.json').write_text(json.dumps(encode(records),indent=2)+'\n')
    # Held-out multipeak forecasts and a larger dimension.
    b=5
    rho=Q(b**b,b**b-(b-1)**b)
    for R in (rho,Q(3,2),Q(7,4),Q(3)):
        vv=vertices(b,R,9)
        forecasts=[{1:Q(1,7),3:Q(2,7),8:Q(4,7)},
                   {2:Q(3,8),5:Q(1,8),7:Q(1,2)},
                   {i:Q(1,8) for i in range(1,9)}]
        for p in forecasts:
            r=optimize(b,R,p)
            val=verify(b,R,p,r)
            g=forecast_costs(b,p,range(1,10))
            expected=min(sum(g[t]*f[t-1] for t in range(1,10)) for f in vv)
            assert val==expected,(b,R,p,val,expected)
            records.append(dict(family='held-out',b=b,R=R,p=p,value=val,result=r))
            max_calls=max(max_calls,r['calls'])
        coverage.append(dict(b=b,R=str(R),M=9,vertices=len(vv),cases=3))
        print('completed held-out',b,str(R),flush=True)
        Path('evidence/oracle-test-cases.json').write_text(json.dumps(encode(records),indent=2)+'\n')
    rng=random.Random(434444406)
    signed_count=0
    signed_records=[]
    for b in range(2,6):
        for R in (Q(3,2),Q(3),Q(11,2)):
            vv=relaxed_vertices(b,R,7)
            for j in range(12):
                costs={t:Q(rng.randrange(-9,10),rng.randrange(1,8)) for t in range(1,8)}
                f,alpha,y,events=linear_oracle(b,R,costs)
                val=objective(costs,f)
                expected=min(sum(costs[t]*v[t-1] for t in range(1,8)) for v in vv)
                assert val==expected,(b,R,costs,val,expected)
                assert sum(f.values())==1 and min(f.values())>=0
                for x in range(1,b):
                    assert sum((b+t-1-x)*v for t,v in f.items() if t<=x)<=(R-1)*x
                assert val==alpha-sum((R-1)*x*y[x] for x in range(1,b))
                signed_records.append(dict(b=b,R=R,costs=costs,policy=f,alpha=alpha,y=y,value=val,events=events))
                signed_count+=1
    for b,R,p in [(12,Q(8,5),{1:Q(1,3),11:Q(1,3),23:Q(1,3)}),
                  (20,Q(2),{3:Q(2,9),27:Q(7,9)}),
                  (40,Q(8,5),{1:Q(1,5),13:Q(1,5),55:Q(3,5)}),
                  (100,Q(2),{1:Q(2,5),101:Q(3,5)}),
                  (3,Q(5),{1:Q(1,2),9:Q(1,2)})]:
        r=optimize(b,R,p)
        val=verify(b,R,p,r)
        records.append(dict(family='large-dual-only',b=b,R=R,p=p,value=val,result=r))
        max_calls=max(max_calls,r['calls'])
        print('completed large',b,str(R),flush=True)
    Path('evidence/oracle-test-cases.json').write_text(json.dumps(encode(records),indent=2)+'\n')
    Path('evidence/linear-oracle-test-cases.json').write_text(json.dumps(encode(signed_records),indent=2)+'\n')
    bisection_records=[]
    for b,R,p in [(3,Q(3,2),{1:Q(2,5),2:Q(3,5)}),
                  (4,Q(3,2),{1:Q(1,5),6:Q(4,5)}),
                  (5,Q(7,4),{2:Q(3,8),5:Q(1,8),7:Q(1,2)})]:
        r=optimize(b,R,p,max_chord_probes=0)
        val=verify(b,R,p,r)
        assert val==verify(b,R,p,optimize(b,R,p))
        bisection_records.append(dict(b=b,R=R,p=p,value=val,result=r))
    Path('evidence/bisection-test-cases.json').write_text(json.dumps(encode(bisection_records),indent=2)+'\n')
    summary=dict(job_id='robust-stopping-research-a43d444f406e',
                 arithmetic='exact rational; no floating point',
                 full_optimizer_enumeration_cases=606,
                 full_optimizer_dual_only_cases=5,
                 signed_linear_oracle_enumeration_cases=signed_count,
                 forced_bisection_cases=len(bisection_records),
                 coverage=coverage,max_oracle_calls=max_calls,mismatches=0,
                 scope='Finite tests and same-worker certificates; no fresh referee')
    Path('evidence/oracle-tests.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
