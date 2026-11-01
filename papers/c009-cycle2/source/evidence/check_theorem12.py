"""Independently enumerate cyclic selected-edge components and bound Theorem 12."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json,datetime
rows=[]
for length in [4,8,12,16]:
 coeff=Counter()
 for mask in range(1,2**length-1):
  starts=[i for i in range(length) if (mask>>i)&1 and not (mask>>((i-1)%length))&1]
  runs=[]
  for start in starts:
   run=0
   while (mask>>((start+run)%length))&1: run+=1
   runs.append(run)
  if any(run%2 for run in runs): continue
  minus=sum((mask>>i)&1 for i in range(length) if i%4>=2)
  coeff[tuple(sorted(runs))]+=(-1)**(minus+sum(runs)//2)
 def expression(p):
  total=F(16*coeff[(4,)])
  for runs,c in coeff.items():
   k=len(runs);s=sum(runs)
   if c>=0: continue
   if k==1 and s>=6: total+=c*F(2**s)/p**(s-4)
   if k>=2: total+=c*F(2**s)/(12**(k-2)*p**(s-2*k))
  return total
 lower,upper=expression(F(3)),expression(F(22,7))
 old=json.loads(Path('intake/prior-cycle-coefficients.json').read_text())['rows']
 oldrow=next(x for x in old if x['length']==length)
 nonzero={','.join(map(str,r)):c for r,c in sorted(coeff.items()) if c}
 assert nonzero==oldrow['exact_coefficients']
 rows.append({'length':length,'gamma':1,'alpha2':coeff[(2,)],'coefficients':nonzero,'scaled_expression_lower_pi_gt_3':str(lower),'scaled_expression_upper_pi_lt_22_over_7':str(upper),'criterion_rigorously_sufficient':lower>=0,'criterion_rigorously_fails':upper<0})
result={'job_id':'c009-cycle2-triage-408b44cde59f','utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'Only the specified sufficient criterion, at four finite lengths. Failure is not a counterexample to the target or proof of novelty.','rows':rows}
Path('evidence/theorem12-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps([{k:v for k,v in row.items() if k!='coefficients'} for row in rows],indent=2))
