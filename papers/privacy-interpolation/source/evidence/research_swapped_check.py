#!/usr/bin/env python3
"""Rational continuous-cell certificates for the full swapped-triplet family.

Includes b>1/2, which was outside the supplied seed. No candidate imports.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import json

HERE = Path(__file__).resolve().parent


def cell(left, right, rows):
    return {'interval': list(map(str, (left, right))),
            'coefficients': [list(map(str, row)) for row in rows]}


def main():
    params = set()
    for den in (12, 13):
        for aa in range(1, den):
            for bb in range(1, den-aa):
                a, high = F(aa, den), F(bb, den)
                if a < high and high > F(1, 2):
                    params.add((a, high))
    params.update([(F(1, 16), F(3, 4)), (F(1, 9), F(3, 4)),
                   (F(1, 100000), F(50001, 100000)),
                   (F(999, 10000), F(9, 10)),
                   (F(1, 1000000), F(999, 1000))])
    records = []
    phase_counts = {'cap_in_initial_phase': 0, 'cap_after_binary_half_crossing': 0,
                    'exact_minimum_budget': 0, 'constant_reservoir_boundary': 0}
    for a, high in sorted(params):
        c = 1-a-high
        crossing = 1/(2*(1-high))
        k = 1/(4*(1-high))
        minimum_exp = k/a
        scale = 1000000
        root_lo = F(isqrt(minimum_exp.numerator*scale*scale//minimum_exp.denominator), scale)
        switches = {1+(crossing-1)*F(i, 3) for i in range(4)}
        switches.update(crossing+(root_lo-crossing)*F(i, 3) for i in range(1, 4))
        rn, rd = isqrt(minimum_exp.numerator), isqrt(minimum_exp.denominator)
        if rn*rn == minimum_exp.numerator and rd*rd == minimum_exp.denominator:
            switches.add(F(rn, rd))
        for switch in sorted(switches):
            if switch <= crossing:
                peak = c*switch
                b = (1-peak)/(2*a)
                rows = [[c, 0, 0], [a, 0, 0], [-(1-high), 0, 1]]
                cells = [cell(F(1), switch, rows)]
                phase_counts['cap_in_initial_phase'] += 1
            else:
                peak = 1-a*switch-k/switch
                b = (1-peak)/(2*a)
                rows = [[c, 0, 0], [a, 0, 0], [-(1-high), 0, 1]]
                later = [[-a, -k, 1], [a, 0, 0], [0, k, 0]]
                cells = [cell(F(1), crossing, rows), cell(crossing, switch, later)]
                phase_counts['cap_after_binary_half_crossing'] += 1
            cells.append(cell(switch, b, [[0, 0, peak], [a, 0, 0], [-a, 0, 2*a*b]]))
            assert minimum_exp <= b*b and b <= (a+high)/(2*a)
            assert c <= peak and switch <= b
            phase_counts['exact_minimum_budget'] += b*b == minimum_exp
            phase_counts['constant_reservoir_boundary'] += peak == c
            records.append({'family': 'general-swapped', 'E': str(high/a),
                            'a': str(a), 'x': str(switch), 'B': str(b), 'Z': str(b*b),
                            'p': list(map(str, (c, a, high))),
                            'q': list(map(str, (c, high, a))),
                            'peak': str(peak), 'half_cells': cells})
    out = {'basis': 'r_i(u)=A_i*u+B_i/u+C_i; reflected second half swaps coordinates 1,2',
           'certificates': records}
    (HERE/'research-swapped-path-certificates.json').write_text(json.dumps(out, indent=2)+'\n')
    result = {'job_id': 'privacy-interpolation-research-294f008bff48',
              'status': 'exact rational general-family construction checks passed; consumer verification separate',
              'parameter_pairs': len(params), 'certificates': len(records),
              'coverage': 'all b>1/2 swapped pairs with a,b,c positive on denominator 12 or 13, plus five boundary/scale cases',
              'phase_counts': phase_counts,
              'limits': 'Universal proof is analytic; finite certificates do not establish a theorem or novelty.'}
    (HERE/'research-swapped-exact-results.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
