#!/usr/bin/env python3
"""Diagnostic controls for the unaccepted trace-based unipotence lemma."""
from fractions import Fraction as F
import json
from pathlib import Path
import random
from root_scattered_check import invariant_basis, words


def eye(d):
    return [[F(int(i == j)) for j in range(d)] for i in range(d)]


def mul(a, b):
    d = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(d)), F(0))
             for j in range(d)] for i in range(d)]


class TraceWA:
    def __init__(self, matrices):
        self.matrices = matrices
        self.alphabet = tuple(matrices)
        self.d = len(next(iter(matrices.values())))
        self.dim = self.d * self.d + 1
        self.initial = [x for row in eye(self.d) for x in row] + [F(1)]

    def row_step(self, v, a):
        d = self.d
        x = [v[i*d:(i+1)*d] for i in range(d)]
        return [t for row in mul(x, self.matrices[a]) for t in row] + [v[-1]]

    def test(self):
        basis = invariant_basis(self)
        for w, v in basis:
            if sum(v[i*self.d+i] for i in range(self.d)) != self.d * v[-1]:
                return False, w, len(basis)
        return True, None, len(basis)


def main():
    rng = random.Random(20261102)
    controls = []
    for d in range(1, 7):
        for _ in range(12):
            matrices = {}
            for a in '01':
                m = eye(d)
                for i in range(d):
                    for j in range(i+1, d):
                        m[i][j] = F(rng.randrange(-3, 4), rng.randrange(1, 4))
                matrices[a] = m
            controls.append((matrices, True, 'simultaneously_upper_unitriangular'))
    controls.extend([
        ({'0': [[F(1), F(1)], [F(0), F(1)]],
          '1': [[F(1), F(0)], [F(1), F(1)]]}, False,
         'unipotent_generators_nonunipotent_product'),
        ({'0': [[F(-1), F(0)], [F(0), F(-1)]]}, False, 'minus_identity'),
        ({'0': [[F(0), F(-1)], [F(1), F(-1)]]}, False, 'third_root_rotation'),
        ({'0': [[F(1), F(0)], [F(0), F(2)]]}, False, 'nonunipotent_redundant_block'),
    ])
    report = dict(scope='Exact diagnostic controls for a proposed all-word trace test; not a fresh audit.',
                  seed=20261102, controls=len(controls), yes=0, no=0,
                  bounded_word_crosschecks=0, no_witnesses=[], mismatches=[])
    for matrices, expected, name in controls:
        wa = TraceWA(matrices)
        yes, witness, rank = wa.test()
        assert yes == expected, name
        assert rank <= wa.dim
        report['yes' if yes else 'no'] += 1
        if not yes:
            v = wa.initial.copy()
            for a in witness:
                v = wa.row_step(v, a)
            tr = sum(v[i*wa.d+i] for i in range(wa.d))
            assert tr != wa.d
            report['no_witnesses'].append(dict(control=name, word=witness, trace=str(tr), d=wa.d))
        for w in words(wa.alphabet, 5):
            v = wa.initial.copy()
            for a in w:
                v = wa.row_step(v, a)
            tr = sum(v[i*wa.d+i] for i in range(wa.d))
            if yes:
                assert tr == wa.d
            report['bounded_word_crosschecks'] += 1
    report['all_passed'] = True
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
