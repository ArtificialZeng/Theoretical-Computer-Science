#!/usr/bin/env python3
"""Recheck saved certificates in exact arithmetic, independently of their discovery.

No optimizer and no nonstandard dependencies. Finite domains are reported.
Infinite-parameter proofs are in proof-dossier.md, not inferred from these tests.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product
from math import comb, prod
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
JOB='coverage-sparse-research-357cde21e920'
SOURCE='eb7061a17cead0bc8cc0e4426f3f8260ac3137dd23b6f4813d8f4952b00ec731'

def f(k,a):return 1-prod(Q(k-v,k) for v in a)
def occ(k,m,s):return [((s>>(k*r))&((1<<k)-1)).bit_count() for r in range(m)]
def stats(a):return sum(a),sum(comb(v,2) for v in a)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def finite_certificates():
 out=[]
 for row in json.loads((HERE/'finite-certificates.json').read_text()):
  k,m=row['k'],row['m']; n=k*m
  y=list(map(Q,row['dual_y0_yT_yC'])); val=Q(row['optimum']);cap=Q(row['C_target'])
  profiles=list(combinations_with_replacement(range(k+1),m))
  assert len(profiles)==row['profiles']
  slacks=[]
  for a in profiles:
   t,c=stats(a);slack=y[0]+y[1]*t+y[2]*c-f(k,a)
   assert slack>=0
   slacks.append({'occupancy':a,'slack':str(slack)})
  assert y[0]+y[1]*k+y[2]*cap==val
  if row['model']=='upper':assert y[2]>=0
  orbit=defaultdict(list)
  for s in range(1<<n):
   a=occ(k,m,s);t,c=stats(a)
   assert y[0]+y[1]*t+y[2]*c>=f(k,a)
   orbit[tuple(sorted(a))].append(s)
  law=defaultdict(Q)
  for a,wt in row['primal']:
   masks=orbit[tuple(a)]
   for s in masks:law[s]+=Q(wt)/len(masks)
  assert sum(law.values())==1 and min(law.values())>=0
  for i in range(n):assert sum(p for s,p in law.items() if (s>>i)&1)==Q(1,m)
  edges=[(k*r+i,k*r+j) for r in range(m) for i,j in combinations(range(k),2)]
  for i,j in edges:
   moment=sum(p for s,p in law.items() if (s>>i)&1 and (s>>j)&1)
   if row['model']=='equality':assert moment==Q(1,m*m)
   else:assert moment<=(1+Q(row['delta']))/m**2
  assert sum(p*f(k,occ(k,m,s)) for s,p in law.items())==val
  out.append({**row,'labeled_subsets_verified':1<<n,'vertex_marginals_verified':n,
              'edge_moments_verified':len(edges),'primal_support_size':len(law),
              'profile_dual_slacks':slacks})
 return out

def matching_law(m,t):
 law=defaultdict(Q)
 if m==1:law[3]=Q(1);return law
 for r in range(m):law[3<<(2*r)]+=t/m
 for r,s in combinations(range(m),2):
  for i,j in product(range(2),repeat=2):
   law[(1<<(2*r+i))|(1<<(2*s+j))]+=(1-t)/(4*comb(m,2))
 return law

def matching_tests():
 out=[]
 for m in range(1,13):
  for mode in ['multiplicative','additive']:
   vals=([Q(0),Q(1,3),Q(1),Q(max(0,m-1)),Q(m),Q(m+1)] if mode=='multiplicative'
         else [Q(0),Q(1,m*m),Q(1,3*m),Q(1,m),Q(2,m),Q(1)])
   for error in sorted(set(vals)):
    cap=(1+error)/m**2 if mode=='multiplicative' else Q(1,m*m)+error
    t=min(Q(1),m*cap);law=matching_law(m,t)
    assert sum(law.values())==1 and min(law.values())>=0
    for i in range(2*m):assert sum(p for s,p in law.items() if (s>>i)&1)==Q(1,m)
    for r in range(m):
     edge=3<<(2*r);moment=sum(p for s,p in law.items() if s&edge==edge)
     assert moment<=cap
     if error==0:assert moment==Q(1,m*m)
    value=sum(p*f(2,occ(2,m,s)) for s,p in law.items())
    assert value==Q(3,4)+t/4
    out.append({'m':m,'mode':mode,'error':str(error),'mixture_t':str(t),'value':str(value)})
 return {'m_range':[1,12],'cases':out,'case_count':len(out),'nature':'finite exact coupling checks; no asymptotic inference'}

def core_dual_tests():
 profiles=local=lines=0
 for k in range(2,41):
  q=Q(k-1,k);alpha=1-q**k;beta=q**k/k
  for a in range(k+1):
   assert 0<=q**a-Q(k-a,k)<=Q(comb(a,2),k*k);local+=1
  for t in range(8*k+1):
   assert 1-q**t<=alpha+beta*(t-k);lines+=1
  if k<=8:
   for m in range(1,7):
    for a in combinations_with_replacement(range(k+1),m):
     t,c=stats(a);assert f(k,a)<=alpha+beta*(t-k)+Q(c,k*k);profiles+=1
 return {'local_k_range':[2,40],'local_cases':local,'integer_line_t_range':'0..8k','line_cases':lines,
         'occupancy_k_range':[2,8],'occupancy_m_range':[1,6],'sorted_profiles':profiles,
         'completeness':'Every ordered occupancy vector in this finite domain is a permutation of a checked sorted profile; all quantities are invariant.'}

def product_tests():
 out=[]
 for k in range(2,5):
  for m in range(1,5):
   n=k*m
   if n>12:continue
   alpha_m=1-Q(m-1,m)**m
   expectation=Q(0)
   for s in range(1<<n):
    t=s.bit_count();p=Q(1,m)**t*Q(m-1,m)**(n-t)
    expectation+=p*f(k,occ(k,m,s))
   assert expectation==alpha_m
   U=1-Q(k-1,k)**k+Q(k-1,2*k*m)
   assert alpha_m<=U
   out.append({'k':k,'m':m,'n':n,'product_value':str(expectation),'sparse_upper':str(U)})
 assert 1-Q(2,3)**3==Q(19,27)<Q(3,4)
 return {'cases':out,'correction':{'k':2,'m':3,'full_independent_value':'19/27','alpha_k':'3/4','claim_refuted':'The product expectation is alpha_k for every k,m.'}}

def heterogeneous_tests():
 # For every finite-certificate primal, choose irregular nonnegative edge errors
 # that cover its exact tested moments, then check the averaged general bound.
 out=[]
 for row in json.loads((HERE/'finite-certificates.json').read_text()):
  k,m=row['k'],row['m'];weights=[(a,Q(w)) for a,w in row['primal']]
  EC=sum(w*stats(a)[1] for a,w in weights)
  edge_count=m*comb(k,2);moment=EC/edge_count
  base=max(Q(0),moment-Q(1,m*m))
  errs=[base+Q(j%3,17*m*m) for j in range(edge_count)]
  bound=1-Q(k-1,k)**k+Q(k-1,2*k*m)+sum(errs)/(k*k)
  assert Q(row['optimum'])<=min(Q(1),bound)
  out.append({'k':k,'m':m,'model':row['model'],'sum_e':str(sum(errs)),'upper':str(min(Q(1),bound))})
 return {'cases':out,'scope':'finite examples only; all heterogeneous budgets follow analytically from the nonnegative pointwise dual'}

def main():
 assert digest(ROOT/'source.md')==SOURCE
 result={'job_id':JOB,'arithmetic':'Python standard-library fractions.Fraction; exact integers/rationals',
         'finite_lp':finite_certificates(),'matching':matching_tests(),'core_dual':core_dual_tests(),
         'mutual_independence':product_tests(),'heterogeneous_errors':heterogeneous_tests(),
         'constant_table':[{'k':k,'alpha_k':str(1-Q(k-1,k)**k),'inverse':str(1/(1-Q(k-1,k)**k)),
                            'coefficient_(k-1)/(2k)':str(Q(k-1,2*k))} for k in range(2,7)],
         'source_sha256':SOURCE,'limits':'Finite checks supplement, and do not prove, all-parameter statements. No new model context or fresh referee was used.'}
 assert digest(ROOT/'source.md')==SOURCE
 (HERE/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps({'finite_optima':[r['optimum'] for r in result['finite_lp']],
                   'matching_cases':result['matching']['case_count'],'core_dual':result['core_dual'],
                   'product_cases':len(result['mutual_independence']['cases']),'source_sha256':SOURCE},indent=2))
if __name__=='__main__':main()
