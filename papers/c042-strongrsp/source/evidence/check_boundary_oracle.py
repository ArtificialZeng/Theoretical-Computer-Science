#!/usr/bin/env python3
"""Exact finite tests of a vertex-block two-clock boundary solver.
No numerical Poisson oracle and no full RSP claim. Run from project root.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import importlib.util, json, random, hashlib

spec=importlib.util.spec_from_file_location('old_checker',Path('intake/check_first_hit_boundaries.py'))
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
RHO=old.RHO; TOP=1+RHO; ALPHA=old.ALPHA

# Edges are (predecessor, head, length-increment law, cost-increment law).
# Each law has q+1 buckets, with bucket q the overflow tail.
def close(B,q):
    D=dict(B)
    for i in reversed(range(q)):
        for j in reversed(range(q)):
            D[i,j]=min(D[i,j],D.get((i+1,j),TOP),D.get((i,j+1),TOP))
    return D

def transfer(edge,i,j,table,q):
    u,v,pl,pc=edge
    ans=F(0)
    for a,pa in enumerate(pl):
        for b,pb in enumerate(pc):
            ans+=pa*pb*(TOP if i+a>=q or j+b>=q else table[u,i+a,j+b])
    return ans

def run(n,q,edges,A,B,enumerate_policies=False):
    table={(v,i,j):B[v][i,j] for v in B for i in range(q) for j in range(q)}
    stats={'policy_evaluations':0,'nonterminating_policies':0,'edge_transfers':0}
    for i in reversed(range(q)):
        for j in reversed(range(q)):
            tick={v:min(table.get((v,i+1,j),TOP),table.get((v,i,j+1),TOP)) for v in A}
            if enumerate_policies:
                av=sorted(A); ix={v:k for k,v in enumerate(av)}; acts=[]
                for v in av:
                    options=[]
                    # The old checker encodes terminal cost as a mixture rho/TOP.
                    def terminal(z):
                        r=[F(0)]*(len(av)+2)
                        r[-1]=(z-RHO)/(TOP-RHO);r[-2]=1-r[-1]
                        return r
                    options.append(terminal(tick[v]))
                    for e in edges:
                        u,w,pl,pc=e
                        if w!=v:continue
                        p=pl[0]*pc[0]
                        if u in A:
                            fake=dict(table);fake[u,i,j]=F(0)
                            const=transfer(e,i,j,fake,q)
                            # const has mass (1-p) and prices in [rho,TOP].
                            r=[F(0)]*(len(av)+2);r[ix[u]]=p
                            r[-1]=(const-(1-p)*RHO)/(TOP-RHO)
                            r[-2]=(1-p)-r[-1]
                            assert min(r)>=0 and sum(r)==1
                            options.append(r)
                        else:options.append(terminal(transfer(e,i,j,table,q)))
                    acts.append(options)
                if av:
                    values,p,nt=old.optimum(acts,{})
                    stats['policy_evaluations']+=p;stats['nonterminating_policies']+=nt
                    for v,z in zip(av,values):table[v,i,j]=z
            else:
                keys=dict(tick)
                for e in edges:
                    u,v,*_=e
                    if v in A and u not in A:
                        keys[v]=min(keys[v],transfer(e,i,j,table,q));stats['edge_transfers']+=1
                pending=set(A);last=RHO
                while pending:
                    u=min(pending,key=lambda v:(keys[v],v));pending.remove(u)
                    assert keys[u]>=last;last=keys[u];table[u,i,j]=keys[u]
                    for e in edges:
                        x,v,*_=e
                        if x==u and v in pending:
                            z=transfer(e,i,j,table,q);stats['edge_transfers']+=1
                            assert z>=table[u,i,j]
                            keys[v]=min(keys[v],z)
    return table,stats

def main():
    rng=random.Random(2026110301);q=2;n=4;fixtures=[]
    # Two active zero-resource vertices in a closed SCC; explicit source is 0.
    zero=[F(1),F(0),F(0)]
    fixtures.append([(1,2,zero,zero),(2,1,zero,zero)])
    # Tiny same-layer exit probability, and a zero self-loop.
    fixtures.append([(0,1,[F(1,1024),F(0),F(1023,1024)],zero),
                     (1,2,zero,zero),(2,1,zero,zero),(3,3,zero,zero)])
    for _ in range(22):
        edges=[]
        for v in range(1,n):
            for u in rng.sample(range(n),2):
                laws=[]
                for _ in range(2):
                    bins=[0,0,0]
                    for _ in range(4):bins[rng.randrange(3)]+=1
                    laws.append([F(x,4) for x in bins])
                edges.append((u,v,*laws))
        fixtures.append(edges)
    checks=policies=nonterm=subsets=0;serialized=[]
    for edges in fixtures:
        src={0:{(i,j):RHO for i in range(q) for j in range(q)}}
        truth,st=run(n,q,edges,set(range(1,n)),src,True)
        policies+=st['policy_evaluations'];nonterm+=st['nonterminating_policies']
        for mask in range(1<<(n-1)):
            A={v for v in range(1,n) if mask>>(v-1)&1}
            raw={v:{(i,j):min(TOP,truth[v,i,j]*(ALPHA if rng.randrange(2) else 1))
                    for i in range(q) for j in range(q)} for v in range(1,n) if v not in A}
            B={**src,**{v:close(prices,q) for v,prices in raw.items()}}
            got,st=run(n,q,edges,A,B)
            ref,rt=run(n,q,edges,A,B,True)
            policies+=rt['policy_evaluations'];nonterm+=rt['nonterminating_policies'];subsets+=1
            assert got==ref
            for v in A:
                for i in range(q):
                    for j in range(q):
                        z=got[v,i,j];x=truth[v,i,j]
                        assert x<=z<=ALPHA*x
                        assert z<=got.get((v,i+1,j),TOP)
                        assert z<=got.get((v,i,j+1),TOP)
                        checks+=1
        serialized.append([[u,v,[str(x) for x in pl],[str(x) for x in pc]] for u,v,pl,pc in edges])
    source_hash=hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
    result={'job_id':'c042-strongrsp-research-c6b8438a850b','source_sha256':source_hash,
            'seed':2026110301,'fixtures':len(fixtures),'vertices':n,'q':q,
            'active_vertex_subsets':subsets,'active_state_comparisons':checks,
            'stationary_policy_evaluations':policies,'policy_evaluations_with_closed_nontermination':nonterm,
            'rho':str(RHO),'alpha':str(ALPHA),'all_checks_passed':True,
            'scope':'24 specified rational two-clock systems; every vertex-active subset; exact policy enumeration. These increment laws are not claimed to be Poisson laws. No all-input RSP or runtime certification.',
            'fixture_edges':serialized}
    Path('evidence/boundary-oracle-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='fixture_edges'}))

if __name__=='__main__':main()
