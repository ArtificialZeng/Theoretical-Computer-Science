#!/usr/bin/env python3
"""Exact finite test of upward-rounded static labels and finite-rank error.
Fraction numerator division is only a checker convenience; the proof specifies
charged bounded binary comparisons for production rounding.
"""
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
import importlib.util
import hashlib
import json

spec=importlib.util.spec_from_file_location('base','evidence/check_boundary_oracle.py')
base=importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
RHO,TOP=base.RHO,base.TOP


def upward(x,b):
    scale=1<<b
    return F((x.numerator*scale+x.denominator-1)//x.denominator,scale)


def run(n,q,edges,A,B,b):
    table={(v,i,j):B[v][i,j] for v in B for i in range(q) for j in range(q)}
    actual=dict(table)
    rank={key:0 for key in table}
    st=Counter()
    for i in reversed(range(q)):
        for j in reversed(range(q)):
            keys={}
            ptr={}
            for v in A:
                choices=[(table.get((v,i+1,j),TOP),('tick',v,i+1,j)),
                         (table.get((v,i,j+1),TOP),('tick',v,i,j+1))]
                keys[v],ptr[v]=min(choices,key=lambda item:item[0])
            for k,e in enumerate(edges):
                u,v,*_=e
                if v in A and u not in A:
                    z=upward(base.transfer(e,i,j,table,q),b)
                    if z<keys[v]:keys[v],ptr[v]=z,('edge',k)
            pending=set(A)
            last=RHO
            while pending:
                u=min(pending,key=lambda v:(keys[v],v))
                pending.remove(u)
                assert keys[u]>=last
                table[u,i,j]=last=keys[u]
                pointer=ptr[u]
                if pointer[0]=='tick':
                    _,v,a,c=pointer
                    actual[u,i,j]=actual.get((v,a,c),TOP)
                    rank[u,i,j]=1+rank.get((v,a,c),0)
                else:
                    edge=edges[pointer[1]]
                    v,_,pl,pc=edge
                    actual[u,i,j]=base.transfer(edge,i,j,actual,q)
                    rank[u,i,j]=1+max([rank.get((v,i+a,j+c),0)
                                               for a,pa in enumerate(pl)
                                               for c,pc0 in enumerate(pc) if pa and pc0])
                assert actual[u,i,j]<=table[u,i,j]
                for k,e in enumerate(edges):
                    v,w,*_=e
                    if v==u and w in pending:
                        raw=base.transfer(e,i,j,table,q)
                        assert raw>=table[u,i,j]
                        z=upward(raw,b)
                        if z<keys[w]:keys[w],ptr[w]=z,('edge',k)
                st['settled_states']+=1
    # Check every action, including ignored already-popped and self-loop edges.
    h=F(1,1<<b)
    for v in A:
        for i in range(q):
            for j in range(q):
                for e in edges:
                    if e[1]==v:
                        assert table[v,i,j]<=base.transfer(e,i,j,table,q)+h
                        st['bellman_residual_checks']+=1
                assert table[v,i,j]<=table.get((v,i+1,j),TOP)
                assert table[v,i,j]<=table.get((v,i,j+1),TOP)
    return table,actual,rank,st


def main():
    packet=json.loads(Path('evidence/boundary-oracle-results.json').read_text())
    fixtures=[]
    for x in packet['fixture_edges']:
        fixtures.append([(u,v,list(map(F,pl)),list(map(F,pc))) for u,v,pl,pc in x])
    # Held-out extremely small exit mass and a parallel alternative.
    z=[F(1),F(0),F(0)]
    fixtures.append([(0,1,[F(1,1<<40),F(0),1-F(1,1<<40)],z),
                     (1,2,z,z),(2,1,z,z),(2,3,z,z),(1,3,z,z)])
    n,q=4,2
    totals=Counter()
    records=[]
    for f,edges in enumerate(fixtures):
        src={0:{(i,j):RHO for i in range(q) for j in range(q)}}
        truth,_=base.run(n,q,edges,{1,2,3},src,True)
        for b in (5,8,12):
            h=F(1,1<<b)
            for mask in range(8):
                A={v for v in (1,2,3) if mask>>(v-1)&1}
                B=dict(src)
                for v in (1,2,3):
                    if v not in A:
                        B[v]=base.close({(i,j):min(TOP,upward(F(17,16)*truth[v,i,j],b))
                                         for i in range(q) for j in range(q)},q)
                ref,rs=base.run(n,q,edges,A,B,True)
                got,actual,rank,st=run(n,q,edges,A,B,b)
                totals.update(st)
                totals['reference_policy_evaluations']+=rs['policy_evaluations']
                totals['reference_nonterminating_policies']+=rs['nonterminating_policies']
                H=(2*q+1)*(len(A)+1)
                err=F(0)
                maxrank=0
                for v in A:
                    for i in range(q):
                        for j in range(q):
                            key=(v,i,j)
                            assert ref[key]<=actual[key]<=got[key]<=ref[key]+H*h
                            assert rank[key]<=H
                            err=max(err,got[key]-ref[key])
                            maxrank=max(maxrank,rank[key])
                            totals['value_and_policy_comparisons']+=1
                            totals['strict_rounding_inflations']+=got[key]>ref[key]
                records.append({'fixture':f,'bits':b,'active':sorted(A),
                                'max_error':str(err),'error_bound':str(H*h),
                                'max_realized_policy_rank':maxrank,'rank_bound':H})
    out={'job_id':'c042-strongrsp-research-266844093669',
         'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
         'all_checks_passed':True,'fixtures':len(fixtures),'cases':len(records),
         'totals':dict(totals),'records':records,
         'scope':'Specified rational q=2 finite fixtures with all active vertex subsets and b=5,8,12. '
                 'Policy enumeration is the prior reference implementation, not an independent referee. '
                 'No full RSP or conservative Poisson construction claim. '
                 'This checker tests rounded static values, policies and residuals; '
                 'rounded offline composition is a proof extension, not experimentally implemented here.'}
    Path('evidence/rounded-oracle-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))


if __name__=='__main__':main()
