"""Bounded foreground cut refinement of exact-cover/Euler CNFs.

Every cut is guarded by both a currently selected root edge outside S and an
internal edge of S. All clauses, cut vertex sets, models and proofs are saved.
The old build/analyze functions are reused; literal checking imports no SAT.
"""
import argparse
import itertools
import json
import math
from pathlib import Path
import resource
import subprocess
import time
from datetime import datetime, timezone

from research1_euler import build, analyze
from research1_sat import sha, EXPECTED_SOURCE
from research1_lrat_check import check

JOB = 'c012-upcycles-research-456cb4499028'
OUT = Path('evidence/research2-connectivity')


def save(path, data):
    Path(path).write_text(json.dumps(data, indent=2) + '\n')


def cut_groups(meta, model):
    tiles = meta['tiles']
    roots = [e for e in model['selected_indices'] if set(tiles[e-1]) <= {'0', '*'}]
    assert len(roots) == 1
    root = roots[0]
    groups = []
    for component in model['components']:
        S = set(component)
        if tiles[root-1][:-1] in S:
            assert tiles[root-1][1:] in S
            continue
        assert tiles[root-1][1:] not in S
        internal = [e for e,t in enumerate(tiles,1) if t[:-1] in S and t[1:] in S]
        leaving = [e for e,t in enumerate(tiles,1) if t[:-1] in S and t[1:] not in S]
        clauses = [tuple([-root, -e] + leaving) for e in internal]
        selected = set(model['selected_indices'])
        assert not selected.intersection(leaving)
        assert any(e in selected for e in internal)
        assert any(not any((abs(x) in selected) == (x > 0) for x in c) for c in clauses)
        groups.append(dict(root=root, vertices=component, internal=internal,
                           leaving=leaving, clauses=clauses))
    assert len(groups) == model['component_count'] - 1
    return groups


def guard_controls():
    # Exhaust every selected subgraph of the complete directed 3-vertex graph,
    # including loops. Connected means its nonzero support is weakly connected.
    edges = list(itertools.product(range(3),repeat=2))
    checked = valid = 0
    missing_root = missing_internal = None
    for bits in itertools.product((False,True),repeat=len(edges)):
        selected = [e for e,b in enumerate(bits) if b]
        if not selected:
            continue
        support = {v for e in selected for v in edges[e]}
        if any(sum(bits[e] for e,(a,b) in enumerate(edges) if a==v) !=
               sum(bits[e] for e,(a,b) in enumerate(edges) if b==v) for v in support):
            continue
        seen = {min(support)}
        while True:
            new = seen | {b for e in selected for a,b in (edges[e],edges[e][::-1]) if a in seen}
            if new == seen:
                break
            seen = new
        if seen != support:
            continue
        valid += 1
        for subset in range(1,7):
            S = {v for v in range(3) if subset & (1<<v)}
            leaving = [i for i,(a,b) in enumerate(edges) if a in S and b not in S]
            for r,(a,b) in enumerate(edges):
                if a in S or b in S:
                    continue
                for e,(c,d) in enumerate(edges):
                    if c not in S or d not in S:
                        continue
                    exit_selected = any(bits[f] for f in leaving)
                    assert not bits[r] or not bits[e] or exit_selected
                    checked += 1
                    if bits[e] and not exit_selected:
                        missing_root = dict(bits=bits,S=sorted(S),root=r,internal=e)
                    if bits[r] and not exit_selected:
                        missing_internal = dict(bits=bits,S=sorted(S),root=r,internal=e)
    assert missing_root is not None and missing_internal is not None
    result = dict(job_id=JOB,all_subgraphs=512,connected_balanced_nonempty=valid,
                  guarded_cut_evaluations=checked,all_sound=True,
                  dropping_root_guard_counterexample=missing_root,
                  dropping_internal_guard_counterexample=missing_internal)
    save('evidence/research2-guard-controls.json',result)
    return result


def run(label,mask,pinned=None,max_rounds=20,total_cap=180,per_call=30):
    assert sha('source.md') == EXPECTED_SOURCE
    OUT.mkdir(exist_ok=True)
    base,meta = build(mask,pinned)
    encoding = OUT/(label+'.encoding.json')
    save(encoding,meta)
    clauses = list(base)
    present = set(clauses)
    groups_all = []
    rounds = []
    elapsed_total = 0.0
    result = dict(job_id=JOB,label=label,n=meta['n'],d=meta['d'],mask=mask,
                  max_rounds=max_rounds,total_solver_wall_cap_seconds=total_cap,
                  per_call_wall_cap_seconds=per_call,encoding=str(encoding),
                  initial_clauses=len(base),rounds=rounds,cut_groups=groups_all,
                  outcome='running',original_question_resolved=False)
    result_path = OUT/(label+'.result.json')
    for turn in range(max_rounds):
        remaining = total_cap-elapsed_total
        if remaining < 0.1:
            result['outcome'] = 'solver-budget-exhausted'
            break
        wall_cap = min(per_call,remaining)
        # Solver's integer CPU limit supplements, never replaces, wall timeout.
        cpu_cap = max(1,math.ceil(wall_cap))
        prefix = OUT/(label+f'.r{turn:02d}')
        cnf = Path(str(prefix)+'.cnf')
        proof = Path(str(prefix)+'.lrat')
        log = Path(str(prefix)+'.log')
        with cnf.open('w') as f:
            f.write(f'c {JOB}: guarded connectivity refinement\n')
            f.write(f'p cnf {meta["variables"]} {len(clauses)}\n')
            for c in clauses:
                f.write(' '.join(map(str,c))+' 0\n')
        command = ['/opt/homebrew/bin/cadical','--check','--lrat','--no-binary',
                   '-t',str(cpu_cap),str(cnf),str(proof)]
        before = resource.getrusage(resource.RUSAGE_CHILDREN)
        start = time.monotonic()
        timeout = False
        with log.open('w') as f:
            try:
                code = subprocess.run(command,stdout=f,stderr=subprocess.STDOUT,
                                      timeout=wall_cap).returncode
            except subprocess.TimeoutExpired:
                code,timeout = None,True
        elapsed = time.monotonic()-start
        elapsed_total += elapsed
        after = resource.getrusage(resource.RUSAGE_CHILDREN)
        status = 'SAT' if code==10 else 'UNSAT' if code==20 else 'unknown'
        record = dict(round=turn,status=status,returncode=code,wall_timeout=timeout,
                      elapsed_seconds=elapsed,wall_cap_seconds=wall_cap,
                      child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                      clauses=len(clauses),cnf=str(cnf),log=str(log),proof=str(proof),
                      cnf_sha256=sha(cnf),proof_sha256=sha(proof) if proof.exists() else None)
        rounds.append(record)
        if code == 10:
            values = {}
            for line in log.read_text().splitlines():
                if line.startswith('v '):
                    for x in map(int,line[2:].split()):
                        if x:
                            values[abs(x)] = x>0
            assert len(values)==meta['variables']
            assert all(any(values[abs(x)]==(x>0) for x in c) for c in clauses)
            selected = [e for e in range(1,len(meta['tiles'])+1) if values[e]]
            model = analyze(meta,selected)
            model_path = Path(str(prefix)+'.model-verification.json')
            save(model_path,model)
            record.update(model_verification=str(model_path),
                          component_count=model['component_count'],
                          component_edge_counts=model['component_edge_counts'])
            if model['component_count']==1:
                assert model['upcycle']['valid']
                result.update(outcome='connected-witness',witness=str(model_path),
                              original_question_resolved=meta['d']>=2)
            else:
                new_groups = cut_groups(meta,model)
                cut_path = Path(str(prefix)+'.cuts.json')
                save(cut_path,new_groups)
                groups_all.append(str(cut_path))
                added = 0
                for group in new_groups:
                    for c in group['clauses']:
                        c = tuple(c)
                        if c not in present:
                            clauses.append(c)
                            present.add(c)
                            added += 1
                assert added > 0
                record.update(cut_groups=len(new_groups),new_cuts=added,cuts=str(cut_path))
        elif code == 20:
            checked = check(cnf,proof)
            proof_check = Path(str(prefix)+'.proof-check.json')
            save(proof_check,checked)
            record['proof_check'] = str(proof_check)
            result['outcome'] = 'fixed-frame-UNSAT-with-checked-CNF-certificate'
        else:
            result['outcome'] = 'unknown-solver-limit-or-error'
        result.update(solver_wall_seconds=elapsed_total,
                      completed_utc=datetime.now(timezone.utc).isoformat())
        save(result_path,result)
        print(json.dumps(dict(label=label,**record)),flush=True)
        if result['outcome'] != 'running':
            break
    else:
        result['outcome'] = 'round-limit-disconnected'
    save(result_path,result)
    print(json.dumps(dict(label=label,outcome=result['outcome'],rounds=len(rounds),
                          solver_wall_seconds=elapsed_total)),flush=True)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['controls','target'])
    args=parser.parse_args()
    if args.mode=='controls':
        guard_controls()
        data=json.loads(Path('evidence/triage-sanity.json').read_text())
        records=[]
        for control in data['controls'][:2]:
            mask=''.join('*' if c=='*' else '.' for c in control['word'][:control['n']])
            r=run('pinned_'+control['label'],mask,control['word'],total_cap=10,per_call=10)
            assert r['outcome']=='connected-witness'
            records.append(r)
        r=run('unpinned_n4d1','...*',total_cap=10,per_call=5)
        assert r['outcome']=='connected-witness'
        records.append(r)
        r=run('bad_flip_n4','...*','101*110*',total_cap=10,per_call=5)
        assert r['outcome']=='fixed-frame-UNSAT-with-checked-CNF-certificate'
        records.append(r)
        r=run('negative_n8d2_period4','*...*...',total_cap=60,per_call=5)
        assert r['outcome']!='connected-witness'
        records.append(r)
        save('evidence/research2-benchmarks.json',dict(job_id=JOB,records=records))
    else:
        run('n12d3_period4','...*'*3)
