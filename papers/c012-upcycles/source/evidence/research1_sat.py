"""Exact global-position XOR CNF; bounded foreground solver, no dependencies.

Run benchmarks: python3 evidence/research1_sat.py benchmark
Run one mask:  python3 evidence/research1_sat.py target MASK
The eight admitted masks are in research1-plan.json. Each solver has a 60 s cap.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import resource
import shutil
import subprocess
import time
from datetime import datetime, timezone

from research1_verify import verify

JOB = 'c012-upcycles-research-cfe911474960'
OUT = Path('evidence/research1-sat')
EXPECTED_SOURCE = '773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build(n, mask, length=None, pinned=None, complement_break=False):
    d = mask.count('*')
    L = length if length is not None else 2**(n-d)
    assert len(mask) == n and L % n == 0
    position = {p: i+1 for i, p in enumerate(p for p in range(L) if mask[p % n] != '*')}
    clauses, gates, pairs = [], {}, []
    self_false = 0
    for i in range(L):
        for j in range(i+1, L):
            mismatch = set()
            for k in range(n):
                p, q = (i+k) % L, (j+k) % L
                if p not in position or q not in position:
                    continue
                if p == q:
                    self_false += 1
                    continue
                x, y = sorted((position[p], position[q]))
                if (x, y) not in gates:
                    z = len(position) + len(gates) + 1
                    gates[x, y] = z
                    clauses.extend(((x, y, -z), (-x, -y, -z),
                                    (x, -y, z), (-x, y, z)))
                mismatch.add(gates[x, y])
            pairs.append((i, j, sorted(mismatch)))
    clauses.extend(tuple(c) for _, _, c in pairs)
    if complement_break:
        clauses.append((-min(position.values()),))
    if pinned is not None:
        assert len(pinned) == L
        assert all((pinned[p] == '*') == (p not in position) for p in range(L))
        clauses.extend((v if pinned[p] == '1' else -v,) for p, v in position.items())
    meta = dict(n=n, d=d, length=L, mask=mask,
                position_variables={str(p): v for p, v in position.items()},
                xor_gates=[dict(x=x, y=y, z=z) for (x, y), z in gates.items()],
                variables=len(position)+len(gates), clauses=len(clauses),
                window_pairs=len(pairs), self_mismatch_predicates_removed=self_false,
                complement_break=complement_break, pinned_word=pinned)
    return clauses, meta


def write_cnf(path, clauses, meta):
    with path.open('w') as f:
        f.write(f'c {JOB}: exact global-position XOR encoding\n')
        f.write(f'p cnf {meta["variables"]} {len(clauses)}\n')
        for clause in clauses:
            f.write(' '.join(map(str, clause)) + ' 0\n')


def evaluate(clauses, values):
    return all(any(values[abs(t)] == (t > 0) for t in clause) for clause in clauses)


def run(label, n, mask, pinned=None, length=None, cap=60):
    assert sha('source.md') == EXPECTED_SOURCE
    OUT.mkdir(exist_ok=True)
    clauses, meta = build(n, mask, length, pinned, complement_break=pinned is None)
    cnf = OUT / (label + '.cnf')
    metadata = OUT / (label + '.encoding.json')
    log = OUT / (label + '.log')
    proof = OUT / (label + '.lrat')
    write_cnf(cnf, clauses, meta)
    metadata.write_text(json.dumps(meta, indent=2) + '\n')
    solver = shutil.which('cadical')
    assert solver
    command = [solver, '--check', '--lrat', '--no-binary', '-t', str(cap), str(cnf), str(proof)]
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    start = time.monotonic()
    timeout = False
    with log.open('w') as f:
        try:
            result = subprocess.run(command, stdout=f, stderr=subprocess.STDOUT, timeout=cap+2)
            code = result.returncode
        except subprocess.TimeoutExpired:
            code, timeout = None, True
    elapsed = time.monotonic() - start
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    text = log.read_text()
    status = 'SAT' if code == 10 else 'UNSAT' if code == 20 else 'unknown'
    record = dict(job_id=JOB, label=label, status=status, returncode=code,
                  hard_timeout=timeout, elapsed_seconds=elapsed, cap_seconds=cap,
                  child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  command=command, completed_utc=datetime.now(timezone.utc).isoformat(),
                  cnf=str(cnf), encoding=str(metadata), log=str(log), proof=str(proof),
                  cnf_sha256=sha(cnf), proof_sha256=sha(proof) if proof.exists() else None,
                  source_sha256=sha('source.md'),
                  variables=meta['variables'], clauses=meta['clauses'])
    if status == 'SAT':
        assignments = {}
        for line in text.splitlines():
            if line.startswith('v '):
                for v in map(int, line[2:].split()):
                    if v:
                        assignments[abs(v)] = v > 0
        assert len(assignments) == meta['variables']
        assert evaluate(clauses, assignments), 'SAT model fails original CNF'
        word = ''.join('*' if str(p) not in meta['position_variables'] else
                       str(int(assignments[meta['position_variables'][str(p)]]))
                       for p in range(meta['length']))
        verification = verify(word, n)
        assert verification['valid'], 'SAT model fails independent expansion'
        model_path = OUT / (label + '.model-verification.json')
        model_path.write_text(json.dumps(verification, indent=2) + '\n')
        record['model_verification'] = str(model_path)
    record_path = OUT / (label + '.result.json')
    record_path.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record), flush=True)
    return record


def benchmark():
    data = json.loads(Path('evidence/triage-sanity.json').read_text())
    records = []
    # Full positive controls at both source orders, pinned to the exact source words.
    for control in data['controls'][:2]:
        word, n = control['word'], control['n']
        mask = ''.join('*' if c == '*' else '.' for c in word[:n])
        result = run('benchmark_' + control['label'], n, mask, word)
        assert result['status'] == 'SAT'
        records.append(result)
    for label, word, n in [('bad_flip_n4', '101*110*', 4),
                           ('bad_zero_n4', '000*000*', 4),
                           ('bad_flip_n8', '1' + data['controls'][1]['word'][1:], 8)]:
        assert not verify(word, n)['valid']
        mask = ''.join('*' if c == '*' else '.' for c in word[:n])
        result = run(label, n, mask, word)
        assert result['status'] == 'UNSAT'
        records.append(result)
    # Exhaust all 64 ordinary assignments in the small frame. Auxiliary gates
    # are evaluated deterministically, so this tests the full generated formula.
    clauses, meta = build(4, '...*')
    valid = []
    for bits in itertools.product((False, True), repeat=6):
        values = dict(enumerate(bits, 1))
        for gate in meta['xor_gates']:
            values[gate['z']] = values[gate['x']] != values[gate['y']]
        word = ''.join('*' if str(p) not in meta['position_variables'] else
                       str(int(values[meta['position_variables'][str(p)]])) for p in range(8))
        assert evaluate(clauses, values) == verify(word, 4)['valid']
        if evaluate(clauses, values):
            valid.append(word)
    result = dict(job_id=JOB, records=records, exhaustive_n4_assignments=64,
                  valid_n4_words=valid, exact_cnf_literal_agreement=True)
    Path('evidence/research1-benchmarks.json').write_text(json.dumps(result, indent=2) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['benchmark', 'target'])
    parser.add_argument('mask', nargs='?')
    args = parser.parse_args()
    if args.mode == 'benchmark':
        benchmark()
    else:
        assert args.mask in ('**......', '*.*.....', '*..*....', '*...*...',
                             '***.....', '**.*....', '**..*...', '*.*.*...')
        label = 'n8d' + str(args.mask.count('*')) + '_' + args.mask.replace('*', 'x').replace('.', 'o')
        run(label, 8, args.mask)
