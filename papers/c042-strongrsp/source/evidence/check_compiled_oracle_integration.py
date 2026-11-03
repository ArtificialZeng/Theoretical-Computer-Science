#!/usr/bin/env python3
"""Reproduce the exact R3 inline compiler-to-oracle integration test."""
from fractions import Fraction as F
import importlib.util,json
from pathlib import Path

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main():
 c=load('compiled','evidence/check_compiled_poisson.py')
 r=load('rounded','evidence/check_rounded_oracle.py')
 q,U,b=2,8,48
 means=[F(0),F(1,128),F(1,4),F(3,2)]
 laws={};optimistic={};pessimistic={}
 for mu in means:
  a,t,d=c.compiler(mu,q,U,b)
  lo,hi=c.reference(mu,q,U,b,d) if d else ([F(1)]*q,[F(1)]*q)
  laws[mu]=c.pmf(a);optimistic[mu]=c.pmf(hi);pessimistic[mu]=c.pmf(lo)
 fixtures=[[(0,1,means[1],means[1]),(1,2,means[2],means[1]),(2,3,means[1],means[2]),(2,1,F(0),F(0))],
           [(0,1,F(0),F(0)),(1,2,means[1],means[1]),(2,1,F(0),F(0)),(2,3,means[3],means[1]),(3,3,F(0),F(0))]]
 records=[];checks=0
 src={0:{(i,j):r.RHO for i in range(q) for j in range(q)}}
 for fi,fixture in enumerate(fixtures):
  def edges(ls):return [(u,v,ls[ml],ls[mc]) for u,v,ml,mc in fixture]
  low,_=r.base.run(4,q,edges(optimistic),{1,2,3},src,False)
  high,_=r.base.run(4,q,edges(pessimistic),{1,2,3},src,False)
  exact,_=r.base.run(4,q,edges(laws),{1,2,3},src,False)
  got,actual,rank,st=r.run(4,q,edges(laws),{1,2,3},src,32)
  H=(2*q+1)*4
  for key in exact:
   assert low[key]<=high[key]<=exact[key]<=got[key]
   assert exact[key]<=actual[key]<=got[key]<=exact[key]+F(H,1<<32)
   assert rank[key]<=H
   checks+=1
  records.append({'fixture':fi,'states':len(exact),'max_rank':max(rank.values()),'rank_bound':H})
 out={'job_id':'c042-strongrsp-research-a3a11d57c4b5','all_checks_passed':True,'state_checks':checks,'records':records,'scope':'Finite compiler-to-static-rounded-oracle integration on two q=2 graphs including zero cycles and self-loop. Exact rational Poisson CDF enclosures give ordered reference laws. Prior oracle implementation reused; not independent review or full algorithm execution.','reproduction':'evidence/check_compiled_oracle_integration.py'}
 Path('evidence/compiled-oracle-integration-results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))

if __name__=='__main__':main()
