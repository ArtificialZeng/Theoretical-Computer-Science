"""Separate balanced subcube tiling from literal overlap/cyclic gluing.

Necessary relaxation: choose L/m distinct tiles of each of the m frame
orientations, partitioning all binary n-words. Cyclic overlap is omitted.
The selector/cardinality CNF and LRAT certificate/model are preserved.
Run: python3 evidence/research1_relaxation.py
"""
import itertools
import json
from pathlib import Path
import subprocess
import time
from research1_sat import JOB, sha

OUT = Path('evidence/research1-relaxation')


def build(mask):
    n = len(mask)
    d = mask.count('*')
    L = 2**(n-d)
    frames = list(dict.fromkeys(mask[s:]+mask[:s] for s in range(n)))
    m = len(frames)
    assert L % m == 0
    tiles, rows = [], []
    for frame in frames:
        row = []
        for bits in itertools.product('01', repeat=n-d):
            letters = iter(bits)
            tile = ''.join('*' if c == '*' else next(letters) for c in frame)
            tiles.append(tile)
            row.append(len(tiles))
        rows.append(row)
    clauses = []
    for bits in itertools.product('01', repeat=n):
        compatible = []
        for r, frame in enumerate(frames):
            value = 0
            for k, c in enumerate(frame):
                if c != '*':
                    value = 2*value+int(bits[k])
            compatible.append(rows[r][value])
        clauses.append(tuple(compatible))
        clauses.extend((-x,-y) for x,y in itertools.combinations(compatible,2))
    nv = len(tiles)
    # Recurrence for count-at-least-j, exact equivalence in four clauses.
    nv += 1
    truth = nv
    clauses.append((truth,))
    count = L//m
    for row in rows:
        previous = [truth]+[-truth]*(count+1)
        for x in row:
            current = [truth]
            for j in range(1,count+2):
                nv += 1
                y, a, b = nv, previous[j], previous[j-1]
                clauses.extend(((-a,y),(-b,-x,y),(-y,a,b),(-y,a,x)))
                current.append(y)
            previous = current
        clauses.extend(((previous[count],),(-previous[count+1],)))
    meta = dict(mask=mask,n=n,d=d,length=L,frame_period=m,
                tiles_per_orientation=count,frames=frames,tiles=tiles,
                selector_rows=rows,variables=nv,clauses=len(clauses),
                scope='necessary phase-balanced subcube tiling relaxation; no cyclic overlap constraints')
    return clauses,meta


def verify_tiles(meta,selected):
    n = meta['n']
    counts = [0]*2**n
    by_orientation = [0]*meta['frame_period']
    for index in selected:
        tile = meta['tiles'][index-1]
        row = next(r for r,ids in enumerate(meta['selector_rows']) if index in ids)
        by_orientation[row] += 1
        holes = [i for i,c in enumerate(tile) if c == '*']
        for bits in itertools.product('01',repeat=len(holes)):
            word = list(tile)
            for k,c in zip(holes,bits):
                word[k] = c
            counts[int(''.join(word),2)] += 1
    assert all(c == 1 for c in counts)
    assert by_orientation == [meta['tiles_per_orientation']]*meta['frame_period']
    # Literal overlaps are a separate, necessary Hamiltonian-cycle kernel.
    adjacency = {str(i):[j for j in selected if j != i and
                        meta['tiles'][i-1][1:] == meta['tiles'][j-1][:-1]] for i in selected}
    indegree = {str(i):sum(i in out for out in adjacency.values()) for i in selected}
    return dict(selected_indices=selected,selected_tiles=[meta['tiles'][i-1] for i in selected],
                coverage_counts=counts,counts_by_orientation=by_orientation,
                literal_overlap_adjacency=adjacency,
                zero_outdegree=[int(i) for i,v in adjacency.items() if not v],
                zero_indegree=[int(i) for i,v in indegree.items() if not v])


def run(mask,cap=20):
    OUT.mkdir(exist_ok=True)
    label = 'n8d'+str(mask.count('*'))+'_'+mask.replace('*','x').replace('.','o')
    clauses,meta = build(mask)
    cnf = OUT/(label+'.cnf')
    proof = OUT/(label+'.lrat')
    log = OUT/(label+'.log')
    encoding = OUT/(label+'.encoding.json')
    with cnf.open('w') as f:
        f.write(f'p cnf {meta["variables"]} {len(clauses)}\n')
        for c in clauses:
            f.write(' '.join(map(str,c))+' 0\n')
    encoding.write_text(json.dumps(meta,indent=2)+'\n')
    cmd = ['/opt/homebrew/bin/cadical','--check','--lrat','--no-binary','-t',str(cap),str(cnf),str(proof)]
    start=time.monotonic()
    with log.open('w') as f:
        try:
            code=subprocess.run(cmd,stdout=f,stderr=subprocess.STDOUT,timeout=cap+2).returncode
        except subprocess.TimeoutExpired:
            code=None
    result = dict(job_id=JOB,mask=mask,status='SAT' if code==10 else 'UNSAT' if code==20 else 'unknown',
                  returncode=code,cap_seconds=cap,elapsed_seconds=time.monotonic()-start,
                  cnf=str(cnf),proof=str(proof),log=str(log),encoding=str(encoding),
                  cnf_sha256=sha(cnf),proof_sha256=sha(proof),
                  scope=meta['scope'],variables=meta['variables'],clauses=meta['clauses'])
    if code==10:
        values={}
        for line in log.read_text().splitlines():
            if line.startswith('v '):
                for x in map(int,line[2:].split()):
                    if x:
                        values[abs(x)]=x>0
        assert all(any(values[abs(x)]==(x>0) for x in c) for c in clauses)
        selected=[i for i in range(1,len(meta['tiles'])+1) if values[i]]
        verified=verify_tiles(meta,selected)
        model=OUT/(label+'.model-verification.json')
        model.write_text(json.dumps(verified,indent=2)+'\n')
        result.update(model_verification=str(model),zero_indegree=len(verified['zero_indegree']),
                      zero_outdegree=len(verified['zero_outdegree']))
    out=OUT/(label+'.result.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)
    return result


if __name__=='__main__':
    plan = dict(job_id=JOB,per_mask_seconds=20,overall_solver_budget_seconds=160,
                changed_test='Remove cyclic overlap and test phase-balanced exact subcube partitions.',
                possible_meaning='UNSAT proves obstruction already at balanced tiling; SAT localizes remaining gap to literal cyclic gluing. No full original resolution from either outcome.')
    Path('evidence/research1-relaxation-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    for mask in ['**......','*.*.....','*..*....','*...*...',
                 '***.....','**.*....','**..*...','*.*.*...']:
        run(mask)
