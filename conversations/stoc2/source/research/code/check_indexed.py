"""Reproduce the indexed implementation row of manuscript Table 2."""
import json
from pathlib import Path
from verify import words, interval, ed
from k_repair import repair


def main():
    count = 0
    for s in words('ab#', 7):
        truth = interval(s)
        for k in range(5):
            result = repair(s, k)
            expected = truth if truth <= k else None
            assert result['distance'] == expected, (s, k, truth, result)
            if result['repair'] is not None:
                fixed = result['repair']
                assert fixed.count('#') == 1
                left, right = fixed.split('#')
                assert left == right[::-1]
                assert ed(s, fixed) == truth, (s, k, result)
            count += 1
    report = {'threshold_and_witness_checks': count, 'max_length': 7,
              'budgets': [0, 1, 2, 3, 4]}
    output = Path(__file__).resolve().parents[1]/'results'/'indexed_verification.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
