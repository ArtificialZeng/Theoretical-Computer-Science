"""Small independent LRAT/RUP-only checker, rejecting all unsupported RAT steps.

Original clauses are numbered from 1. Each addition is checked by negating its
clause and unit-propagating the positively numbered hint clauses in sequence.
No solver code or solver libraries are imported. Deletions remove clauses.
This deliberately rejects negative RAT hints rather than silently trusting them.
"""
import argparse
import hashlib
import json
from pathlib import Path
import time


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_cnf(path):
    clauses = {}
    pending = []
    declared = None
    variables = None
    for line in Path(path).read_text().splitlines():
        if not line or line.startswith('c'):
            continue
        if line.startswith('p '):
            _, kind, variables, declared = line.split()
            assert kind == 'cnf'
            variables, declared = int(variables), int(declared)
            continue
        for x in map(int, line.split()):
            if x:
                assert abs(x) <= variables
                pending.append(x)
            else:
                clauses[len(clauses)+1] = tuple(pending)
                pending = []
    assert not pending and len(clauses) == declared
    return clauses


def check(cnf, proof):
    start = time.monotonic()
    clauses = read_cnf(cnf)
    initial = len(clauses)
    greatest = initial
    additions = deletions = 0
    empty = False
    for line_number, line in enumerate(Path(proof).read_text().splitlines(), 1):
        if not line or line.startswith('c'):
            continue
        t = line.split()
        if t[1] == 'd':
            assert t[-1] == '0'
            for key in map(int, t[2:-1]):
                clauses.pop(key, None)
                deletions += 1
            continue
        key = int(t[0])
        assert key > greatest, (line_number, 'nonincreasing clause index')
        greatest = key
        z = t.index('0')
        clause = tuple(map(int, t[1:z]))
        assert t[-1] == '0'
        hints = list(map(int, t[z+1:-1]))
        assert all(h > 0 for h in hints), (line_number, 'RAT hints unsupported')
        values = {}
        contradiction = False
        # Assume the new clause is false.
        for lit in clause:
            var, val = abs(lit), lit < 0
            if var in values and values[var] != val:
                contradiction = True
                break
            values[var] = val
        if not contradiction:
            for hint in hints:
                assert hint in clauses, (line_number, 'missing hint', hint)
                unassigned = set()
                satisfied = False
                for lit in clauses[hint]:
                    var = abs(lit)
                    if var not in values:
                        unassigned.add(lit)
                    elif values[var] == (lit > 0):
                        satisfied = True
                        break
                if satisfied:
                    raise AssertionError((line_number, 'nonunit satisfied hint', hint))
                if not unassigned:
                    contradiction = True
                    break
                assert len(unassigned) == 1, (line_number, 'nonunit hint', hint)
                lit = next(iter(unassigned))
                values[abs(lit)] = lit > 0
        assert contradiction, (line_number, 'no RUP conflict')
        clauses[key] = clause
        additions += 1
        if not clause:
            empty = True
    assert empty, 'No checked empty clause: not an UNSAT certificate'
    return dict(cnf=str(cnf), proof=str(proof), cnf_sha256=digest(cnf),
                proof_sha256=digest(proof), initial_clauses=initial,
                checked_additions=additions, deletions=deletions,
                checked_empty_clause=empty, verdict='verified-UNSAT-of-this-CNF',
                checker='independent Python LRAT/RUP-only checker',
                elapsed_seconds=time.monotonic()-start)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('cnf')
    parser.add_argument('proof')
    parser.add_argument('--out')
    args = parser.parse_args()
    result = check(args.cnf, args.proof)
    if args.out:
        Path(args.out).write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))
