#!/usr/bin/env python3
"""Held-out q=3 tests, fixed after the q=2 oracle/statement was written."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json
spec=importlib.util.spec_from_file_location('oracle',Path('evidence/check_boundary_oracle.py'))
o=importlib.util.module_from_spec(spec);spec.loader.exec_module(o)
q=3;n=3;z=[F(1),F(0),F(0),F(0)]
# Independent structured attack: zero edges, exact one/two-tick moves,
# parallel edges, certain overflow, and a 1/2^40 same-layer escape mixture.
fixtures=[
 [(0,1,z,z),(1,2,z,z)],
 [(0,1,[F(1,2),F(0),F(0),F(1,2)],z),(1,2,z,z)],
 [(0,1,[F(1,2**40),F(0),F(0),1-F(1,2**40)],z),(1,2,z,z),(2,1,z,z)],
 [(0,1,z,z),(1,2,[F(0),F(0),F(1),F(0)],z),(0,2,[F(3,4),F(0),F(0),F(1,4)],z)],
 [(0,1,[F(3,4),F(1,4),F(0),F(0)],z),(1,2,z,[F(0),F(1),F(0),F(0)]),
  (0,2,[F(1,2),F(0),F(0),F(1,2)],z),(0,2,z,[F(0),F(0),F(0),F(1)])],
 [(1,2,z,z),(2,1,z,z),(1,1,z,z)]
]
checks=policies=nonterm=strict=raw_nonmonotone=0;subsets=0;serialized=[]
for edges in fixtures:
 src={0:{(i,j):o.RHO for i in range(q) for j in range(q)}}
 truth,st=o.run(n,q,edges,{1,2},src,True)
 policies+=st['policy_evaluations'];nonterm+=st['nonterminating_policies']
 for mask in range(4):
  A={v for v in (1,2) if mask>>(v-1)&1}
  for mode in (0,1):
   raw={v:{(i,j):min(o.TOP,truth[v,i,j]*(o.ALPHA if mode==0 or (i+j)%2==0 else 1))
           for i in range(q) for j in range(q)} for v in (1,2) if v not in A}
   for tab in raw.values():
    raw_nonmonotone+=any(tab[i,j]>tab.get((i+1,j),o.TOP) or tab[i,j]>tab.get((i,j+1),o.TOP)
                          for i in range(q) for j in range(q))
   B={**src,**{v:o.close(tab,q) for v,tab in raw.items()}}
   got,_=o.run(n,q,edges,A,B);ref,st=o.run(n,q,edges,A,B,True)
   policies+=st['policy_evaluations'];nonterm+=st['nonterminating_policies'];subsets+=1
   assert got==ref
   for v in A:
    for i in range(q):
     for j in range(q):
      assert truth[v,i,j]<=got[v,i,j]<=o.ALPHA*truth[v,i,j]
      assert got[v,i,j]<=got.get((v,i+1,j),o.TOP)
      assert got[v,i,j]<=got.get((v,i,j+1),o.TOP)
      strict+=got[v,i,j]>truth[v,i,j];checks+=1
 serialized.append([[u,v,[str(x) for x in pl],[str(x) for x in pc]] for u,v,pl,pc in edges])
result={'job_id':'c042-strongrsp-research-c6b8438a850b','q':q,'vertices':n,'fixtures':len(fixtures),
 'active_subsets_times_boundary_modes':subsets,'active_state_comparisons':checks,
 'stationary_policy_evaluations':policies,'policy_evaluations_with_closed_nontermination':nonterm,
 'strictly_inflated_active_values':strict,'nonmonotone_raw_boundary_tables_repaired':raw_nonmonotone,
 'all_checks_passed':True,'arithmetic':'exact Fraction; no probability or tolerance approximation',
 'scope':'Six structured held-out q=3 rational clock systems, every active-vertex subset and two boundary modes; finite support only, not original RSP resolution.',
 'fixture_edges':serialized}
Path('evidence/boundary-oracle-heldout-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='fixture_edges'}))
