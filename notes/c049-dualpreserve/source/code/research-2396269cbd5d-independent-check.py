#!/usr/bin/env python3
"""Independent exact check of the saved extremizer and generic density bounds."""
from pathlib import Path
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from fractions import Fraction
import hashlib,json
PREFIX='research-2396269cbd5d';JOB='c049-dualpreserve-research-2396269cbd5d'
spec=spec_from_file_location('orientation',Path(__file__).with_name(PREFIX+'-energy-test.py'))
module=module_from_spec(spec);spec.loader.exec_module(module)

def main():
    data=json.loads(Path(__file__).with_name(PREFIX+'-energy-results.json').read_text())
    case=data['critical_graph_screens'][-1]['maximizer'];n=case['n'];ed=case['edges'];P=case['demands'];m=len(ed)
    def reach(s,t,F):
        seen={s};queue=[s]
        for u in queue:
            if u==t:return True
            for e,(x,y) in enumerate(ed):
                if x==u and e not in F and y not in seen:seen.add(y);queue.append(y)
        return False
    failures=[set(F) for k in range(3) for F in combinations(range(m),k)]
    covers={};witnesses={}
    for s in range(n):
        for t in range(n):
            if s==t:continue
            covered=set()
            for F in failures:
                if not reach(s,t,F):continue
                for e in range(m):
                    if e not in F and not reach(s,t,F|{e}):
                        covered.add(e)
                        if [s,t] in P:witnesses.setdefault(e,{'pair':[s,t],'failures':sorted(F)})
            covers[s,t]=covered
    assert len(witnesses)==m
    assert all(len(S)<m for S in covers.values()) # no single demand suffices
    assert module.brute_energy(n,ed)==case['energy']==module.flow_energy(n,ed)
    density_checks=0;maxratio=Fraction(0)
    for q in range(2,6):
        universe=list(combinations(range(q),2));H=sum((Fraction(1,i) for i in range(1,2*q-2)),Fraction(0))
        for mask in range(1,1<<len(universe)):
            edges=[e for j,e in enumerate(universe) if mask>>j&1]
            D=max(Fraction(sum(1 for u,v in edges if U>>u&1 and U>>v&1)**2,U.bit_count()) for U in range(1,1<<q))
            E=module.path_reverse(q,edges)[0]
            assert D<=E<=(2+H/2)*D
            maxratio=max(maxratio,Fraction(E)/D);density_checks+=1
    result={'job_id':JOB,'status':'all independent declared checks passed','saved_extremizer':case,
        'direct_failure_sets_tested_per_demand':len(failures),'direct_failure_tested_demands':n*(n-1),
        'minimum_demand_cardinality_independently_verified':2,'mandatory_edge_witnesses':witnesses,
        'orientation_checked_by_all_orientations_and_flow':True,
        'generic_density_inequality_exact_nonempty_graph_checks':density_checks,
        'maximum_observed_energy_over_density_on_this_finite_range':str(maxratio),
        'limits':'Saved n=4 extremizer only for direct failures. Density check covers all nonempty simple undirected graphs n=2..5. This is same-worker deterministic verification, not a fresh referee or an asymptotic critical-graph theorem.',
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_name(PREFIX+'-independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','generic_density_inequality_exact_nonempty_graph_checks','maximum_observed_energy_over_density_on_this_finite_range']}))

if __name__=='__main__':main()
