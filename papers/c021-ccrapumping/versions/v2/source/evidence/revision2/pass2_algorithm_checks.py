#!/usr/bin/env python3
"""Independent coefficient oracle vs inherited WA decision and construction."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product, permutations
from math import factorial
from pathlib import Path
import hashlib
import json
import random
from root_scattered_check import PatternWA, decide, synthesize, evaluate_ccra


def commutative_coefficients(terms):
    combined = defaultdict(F)
    for p, c in terms:
        combined[p] += c
    classes = defaultdict(list)
    for p, c in combined.items():
        if c:
            classes[tuple(sorted(Counter(p).items()))].append(c)
    for key, coefficients in classes.items():
        total = sum(m for _, m in key)
        size = factorial(total)
        for _, m in key:
            size //= factorial(m)
        if len(coefficients) != size or len(set(coefficients)) != 1:
            return False
    return True


def direct_value(terms, w):
    value = F(0)
    for p, c in terms:
        dp = [1]+[0]*len(p)
        for a in w:
            for j in range(len(p), 0, -1):
                if p[j-1] == a:
                    dp[j] += dp[j-1]
        value += c*dp[-1]
    return value


def main():
    rng = random.Random(20261105)
    small = ['', '0', '1', '00', '01', '10', '11']
    cases = []
    for coefficients in product((-1, 0, 1), repeat=len(small)):
        cases.append(([(p, F(c)) for p, c in zip(small, coefficients) if c], '01'))
    for alphabet in ('01', 'abc'):
        for _ in range(90):
            terms = []
            for _ in range(rng.randrange(1, 8)):
                p = ''.join(rng.choice(alphabet) for _ in range(rng.randrange(7)))
                c = F(rng.randrange(-5, 6)*(2**83+9), (2**79+3)*rng.randrange(1, 6))
                terms.append((p, c))
            cases.append((terms, alphabet))
        for _ in range(10):
            multiset = ''.join(rng.choice(alphabet) for _ in range(5))
            coefficient = F(-2**71-7, 2**67+3)
            terms = [(p, coefficient) for p in sorted(set(map(''.join, permutations(multiset))))]
            # Include repeated-pattern cancellation in both YES and NO cases.
            terms += [(''.join(reversed(multiset)), F(7)),
                      (''.join(reversed(multiset)), F(-7))]
            cases.append((terms, alphabet))
            if len(terms) > 3:
                cases.append((terms[1:], alphabet))
    cases += [([], ''), ([('', F(-7, 3))], ''),
              ([('ab', F(2)), ('ab', F(-2))], 'ab'),
              ([('aaaaaa', F(2, 11))], 'a')]
    report = dict(job_id='c021-ccrapumping-research-b9b720512ca2', seed=20261105,
                  scope='Finite exact algorithm checks; universal CCRA exclusion depends on pass2-proof.md.',
                  coefficient_oracle='Parikh-class coefficient equality and multinomial support size',
                  cases=len(cases), exhaustive_binary_degree_le2_ternary_coefficients=3**7,
                  yes=0, no=0, checked_no_certificates=0, yes_machine_value_checks=0,
                  direct_wa_value_checks=0, max_dimension=0, max_no_length=0,
                  max_coefficient_numerator_bits=0, mismatches=[])
    for terms, alphabet in cases:
        report['max_coefficient_numerator_bits'] = max(
            [report['max_coefficient_numerator_bits']]+[abs(c.numerator).bit_length() for _, c in terms])
        wa = PatternWA(terms, alphabet)
        report['max_dimension'] = max(report['max_dimension'], wa.dim)
        yes, certificate, _ = decide(wa)
        assert yes == commutative_coefficients(terms), terms
        report['yes' if yes else 'no'] += 1
        if not yes:
            x, y = certificate
            assert Counter(x) == Counter(y)
            assert direct_value(terms, x) != direct_value(terms, y)
            assert len(x) == len(y) <= 2*wa.dim
            report['max_no_length'] = max(report['max_no_length'], len(x))
            report['checked_no_certificates'] += 1
        machine = synthesize(terms) if yes else None
        inputs = ['', ''.join(alphabet), ''.join(reversed(alphabet))]
        if alphabet:
            inputs += [''.join(rng.choice(alphabet) for _ in range(rng.randrange(14)))
                       for _ in range(5)]
        for w in inputs:
            expected = direct_value(terms, w)
            assert wa.value(w) == expected
            report['direct_wa_value_checks'] += 1
            if yes:
                assert evaluate_ccra(machine, w) == expected
                report['yes_machine_value_checks'] += 1
    report['all_passed'] = True
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report['inherited_algorithm_sha256'] = hashlib.sha256(
        Path(__file__).with_name('root_scattered_check.py').read_bytes()).hexdigest()
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, sort_keys=True))


if __name__ == '__main__':
    main()
