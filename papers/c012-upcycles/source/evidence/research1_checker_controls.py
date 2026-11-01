"""Adversarial certificate and cardinality-gate sanity controls."""
import itertools
import json
from pathlib import Path
from research1_lrat_check import check


def main():
    out=Path('evidence/research1-checker-controls')
    out.mkdir(exist_ok=True)
    unsat=out/'tiny-unsat.cnf'
    sat=out/'tiny-sat.cnf'
    good=out/'valid.lrat'
    bad=out/'invalid.lrat'
    missing=out/'missing-hint.lrat'
    empty=out/'incomplete.lrat'
    unsat.write_text('p cnf 1 2\n1 0\n-1 0\n')
    sat.write_text('p cnf 1 1\n1 0\n')
    good.write_text('3 0 1 2 0\n')
    bad.write_text('2 0 1 0\n')
    missing.write_text('3 0 99 0\n')
    empty.write_text('')
    accepted=check(unsat,good)
    rejected=[]
    for cnf,proof in [(sat,bad),(unsat,missing),(unsat,empty)]:
        try:
            check(cnf,proof)
        except AssertionError as exc:
            rejected.append(dict(cnf=str(cnf),proof=str(proof),reason=str(exc)))
        else:
            raise AssertionError('Checker accepted intentionally invalid proof')
    rows=[]
    for a,b,x,y in itertools.product([False,True],repeat=4):
        clauses=[(not a or y),(not b or not x or y),
                 (not y or a or b),(not y or a or x)]
        assert all(clauses)==(y==(a or (b and x)))
        rows.append(dict(a=a,b=b,x=x,y=y,clauses_hold=all(clauses)))
    result=dict(valid_unsat_control=accepted,invalid_certificates_rejected=rejected,
                cardinality_recurrence_all_16_rows=rows)
    Path('evidence/research1-checker-controls.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(valid_proof_accepted=True,invalid_proofs_rejected=len(rejected),
                          cardinality_gate_rows=len(rows))))


if __name__=='__main__':
    main()
