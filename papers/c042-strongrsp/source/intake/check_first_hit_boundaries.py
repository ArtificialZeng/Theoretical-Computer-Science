#!/usr/bin/env python3
"""Exact stationary-policy comparison for tiny absorbing systems; no RSP/time theorem."""
from fractions import Fraction as F
from itertools import product
import random
import json
from pathlib import Path

RHO=F(1,32)
ALPHA=F(9,8)

def solve(A,b):
    n=len(b);a=[list(row)+[v] for row,v in zip(A,b)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if a[i][j])
        a[j],a[pivot]=a[pivot],a[j]
        x=a[j][j];a[j]=[v/x for v in a[j]]
        for i in range(n):
            if i!=j:
                x=a[i][j]
                a[i]=[u-x*v for u,v in zip(a[i],a[j])]
    return [a[i][-1] for i in range(n)]

def evaluate(actions,policy,boundary):
    n=len(actions);active=[i for i in range(n) if i not in boundary]
    rows={i:actions[i][policy[i]] for i in active}
    good={i for i in active if rows[i][n]+rows[i][n+1]+sum(rows[i][j] for j in boundary)>0}
    while True:
        new=good|{i for i in active if any(rows[i][j]>0 for j in good)}
        if new==good:break
        good=new
    good=sorted(good);bad=set(active)-set(good)
    vals=dict(boundary);vals.update({i:1+RHO for i in bad})
    A=[];b=[]
    for i in good:
        r=rows[i]
        A.append([F(i==j)-r[j] for j in good])
        b.append(r[n]*RHO+r[n+1]*(1+RHO)+sum(r[j]*vals[j] for j in vals))
    vals.update(zip(good,solve(A,b)))
    return [vals[i] for i in range(n)],len(bad)

def optimum(actions,boundary):
    n=len(actions);active=[i for i in range(n) if i not in boundary]
    best=[None]*n;count=nonterm=0
    for choices in product(*[range(len(actions[i])) for i in active]):
        policy=dict(zip(active,choices));v,bad=evaluate(actions,policy,boundary)
        count+=1;nonterm+=bad>0
        for i,x in enumerate(v):
            best[i]=x if best[i] is None else min(best[i],x)
    return best,count,nonterm

def main():
    rng=random.Random(20261103);fixtures=[]
    n=3
    # Explicit zero-cycle and exit choices, then held fixed seeded rational systems.
    fixtures.append([[[F(1),F(0),F(0),F(0),F(0)],[F(0),F(0),F(0),F(1),F(0)]],
                     [[F(0),F(1),F(0),F(0),F(0)],[F(0),F(0),F(0),F(0),F(1)]],
                     [[F(0),F(0),F(1),F(0),F(0)],[F(1,2),F(1,2),F(0),F(0),F(0)]]])
    for _ in range(79):
        mdp=[]
        for _ in range(n):
            options=[]
            for _ in range(2):
                buckets=[0]*(n+2)
                for _ in range(4):buckets[rng.randrange(n+2)]+=1
                options.append([F(x,4) for x in buckets])
            mdp.append(options)
        fixtures.append(mdp)
    policies=nonterm=subsets=checks=0
    for actions in fixtures:
        truth,p,nt=optimum(actions,{})
        policies+=p;nonterm+=nt
        assert all(RHO<=x<=1+RHO for x in truth)
        for mask in range(1<<n):
            boundary={i:min(ALPHA*truth[i],1+RHO) for i in range(n) if mask>>i&1}
            got,p,nt=optimum(actions,boundary)
            policies+=p;nonterm+=nt;subsets+=1
            for x,y in zip(truth,got):
                assert x<=y<=ALPHA*x,(mask,x,y)
                checks+=1
    result={'seed':20261103,'systems':len(fixtures),'states_per_system':n,'actions_per_state':2,
            'inactive_subsets':subsets,'pointwise_inequality_checks':checks,
            'stationary_policies_evaluated':policies,'evaluated_policies_with_closed_nonterminating_states':nonterm,
            'rho':str(RHO),'alpha':str(ALPHA),'arithmetic':'exact Fraction Gaussian elimination; nontermination assigned failure cost1+rho',
            'all_checks_passed':True,'scope':'All stationary deterministic policies and all inactive subsets for80 specified tiny rational systems; not all systems, actual Poisson DP boundary label-setting, all-n offline work, or the original RSP theorem.',
            'fixtures':[[[[str(x) for x in row] for row in options] for options in mdp] for mdp in fixtures]}
    out=Path(__file__).with_name('first-hit-boundary-results.json');out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fixtures'}))

if __name__=='__main__':main()
