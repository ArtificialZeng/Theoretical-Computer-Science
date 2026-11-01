#!/usr/bin/env python3
"""Exact discovery of small profile-LP primal/dual certificates; no floating point."""
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement
from math import comb, prod
import json

def solve(a,b):
 a=[[Q(v) for v in row]+[Q(t)] for row,t in zip(a,b)]
 n=len(b)
 for j in range(n):
  p=next((r for r in range(j,n) if a[r][j]),None)
  if p is None:return None
  a[j],a[p]=a[p],a[j]
  d=a[j][j];a[j]=[v/d for v in a[j]]
  for r in range(n):
   if r!=j:
    d=a[r][j];a[r]=[x-d*y for x,y in zip(a[r],a[j])]
 return [row[-1] for row in a]

def discover(k,m,delta=None):
 ps=list(combinations_with_replacement(range(k+1),m))
 data=[([Q(1),Q(sum(p)),Q(sum(comb(v,2) for v in p))],1-prod(Q(k-v,k) for v in p)) for p in ps]
 cap=Q(k*(k-1),2*m)*(1+(delta or 0))
 rhs=[Q(1),Q(k),cap]
 best=None
 for ids in combinations(range(len(ps)),3):
  w=solve([[data[i][0][j] for i in ids] for j in range(3)],rhs)
  if w is None or min(w)<0:continue
  val=sum(wt*data[i][1] for i,wt in zip(ids,w))
  if best is None or val>best[0]:best=(val,[(ps[i],str(wt)) for i,wt in zip(ids,w) if wt])
 dual=None
 for ids in combinations(range(len(ps)),3):
  y=solve([data[i][0] for i in ids],[data[i][1] for i in ids])
  if y is None or (delta is not None and y[2]<0):continue
  if not all(sum(x*t for x,t in zip(row,y))>=f for row,f in data):continue
  val=sum(x*t for x,t in zip(rhs,y))
  if dual is None or val<dual[0]:dual=(val,y)
 assert best and dual and best[0]==dual[0],(k,m,delta,best,dual)
 return {'k':k,'m':m,'model':'equality' if delta is None else 'upper','delta':None if delta is None else str(delta),'profiles':len(ps),'C_target':str(cap),'optimum':str(best[0]),'primal':best[1],'dual_y0_yT_yC':list(map(str,dual[1]))}
if __name__=='__main__':
 rows=[discover(2,2),discover(2,3),discover(3,2),discover(3,3),discover(3,3,Q(1))]
 print(json.dumps(rows,indent=2))
