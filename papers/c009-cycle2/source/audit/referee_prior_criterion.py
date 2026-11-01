"""Fresh connected-component enumeration for the stated Theorem 12 comparison."""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import json
rows=[]
for L in [4,8,12,16]:
 coeff=Counter()
 for mask in range(1,(1<<L)-1):
  chosen={e for e in range(L) if mask&(1<<e)}
  unseen=chosen.copy(); sizes=[]
  while unseen:
   seed=unseen.pop(); todo=[seed]; component={seed}
   while todo:
    e=todo.pop()
    for f in [(e-1)%L,(e+1)%L]:
     if f in unseen: unseen.remove(f); component.add(f); todo.append(f)
   sizes.append(len(component))
  if any(k%2 for k in sizes): continue
  flips=sum(e%4>=2 for e in chosen)+len(chosen)//2
  coeff[tuple(sorted(sizes))]+=(-1)**flips
 def bound(p):
  ans=16*F(coeff[(4,)])
  for runs,c in coeff.items():
   k=len(runs); total=sum(runs)
   if c>=0: continue
   if k==1 and total>=6: ans+=F(c*2**total)/p**(total-4)
   elif k>=2: ans+=F(c*2**total,12**(k-2))/p**(total-2*k)
  return ans
 row={'length':L,'alpha2':coeff[(2,)],'scaled_expression_lower_using_pi_gt_3':str(bound(F(3))),'scaled_expression_upper_using_pi_lt_22_over_7':str(bound(F(22,7))),'nonzero_coefficients':{','.join(map(str,k)):v for k,v in sorted(coeff.items()) if v}}
 reference=json.loads(Path('evidence/theorem12-results.json').read_text())['rows']
 old=next(r for r in reference if r['length']==L)
 assert row['nonzero_coefficients']==old['coefficients']
 assert row['scaled_expression_lower_using_pi_gt_3']==old['scaled_expression_lower_pi_gt_3']
 assert row['scaled_expression_upper_using_pi_lt_22_over_7']==old['scaled_expression_upper_pi_lt_22_over_7']
 rows.append(row)
result={'job_id':'c009-cycle2-referee-eb6d40fb0393','scope':'Only applicability of one published sufficient criterion at four lengths. Neither failure nor success here proves priority.','rows':rows,'all_frozen_coefficients_and_bounds_reproduced':True}
Path('audit/referee-prior-criterion.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
