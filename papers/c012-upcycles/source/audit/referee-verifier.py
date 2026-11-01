"""Fresh referee verifier, independent of the candidate's programs and SAT data.

Run from PROJECT_DIR. Only reads frozen inputs and writes its own audit result.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

JOB = 'c012-upcycles-referee-9a733cb83e73'
ROOT = Path(__file__).resolve().parents[1]


def check(word, n):
    """Use integer masks, then independently expand every wildcard choice."""
    length = len(word)
    patterns = []
    diamonds = []
    expanded = [0] * (1 << n)
    starts = [[] for _ in expanded]
    for start in range(length):
        mask = value = 0
        free = []
        for k in range(n):
            char = word[(start + k) % length]
            bit = 1 << (n - 1 - k)
            if char == '*':
                free.append(bit)
            else:
                assert char in '01'
                mask |= bit
                if char == '1':
                    value |= bit
        patterns.append((mask, value))
        diamonds.append(len(free))
        for assignment in range(1 << len(free)):
            total = value
            for j, bit in enumerate(free):
                if assignment & (1 << j):
                    total |= bit
            expanded[total] += 1
            starts[total].append(start)
    # This second computation tests every word against every starting index.
    direct = [sum((total & mask) == value for mask, value in patterns)
              for total in range(1 << n)]
    assert direct == expanded
    return diamonds, expanded, starts, patterns


snapshot = json.loads((ROOT / 'audit/snapshot.json').read_text())
assert all(sha256((ROOT / file).read_bytes()).hexdigest() == digest
           for file, digest in snapshot['files'].items())
canonical = json.dumps(snapshot['files'], sort_keys=True,
                       separators=(',', ':'), ensure_ascii=False).encode()
assert sha256(canonical).hexdigest() == snapshot['digest']

# Transcribed directly from the frozen proof, rather than trusting its decoder.
octal = ('00177617563754173657321716771457'
         '12371016661655164636441633162656'
         '22161556133611160676045602151214'
         '46141314063206120412261006540236')
word = ''.join('*' + bin(int(digit))[2:].zfill(3) for digit in octal)
witness = json.loads((ROOT / 'evidence/research2-witness/witness.json').read_text())
assert octal == witness['pane_representation'] and len(octal) == 128
assert word == witness['word']
assert word == (ROOT / 'evidence/research2-witness/word.txt').read_text().strip()
assert len(word) == 512 and set(word) == set('*01')
assert (witness['a'], witness['n'], witness['d'], witness['length']) == (2,12,3,512)
assert sha256(word.encode()).hexdigest() == witness['word_sha256']
assert all((char == '*') == (index % 4 == 0) for index, char in enumerate(word))

diamonds, counts, starts, patterns = check(word, 12)
assert set(diamonds) == {3} and counts == [1] * 4096
assert len(word) == 2 ** (12 - 3) and len(word) > 12
inverse = [indices[0] for indices in starts]
assert Counter(inverse) == Counter({i: 8 for i in range(512)})
saved_inverse = json.loads((ROOT / 'evidence/research2-witness/inverse-coverage.json').read_text())
assert inverse == saved_inverse['unique_start_by_lexicographic_total_word']
assert counts == saved_inverse['coverage_counts']

certificate = json.loads((ROOT / 'evidence/research2-witness/pair-conflicts.json').read_text())
offsets = certificate['first_ordinary_conflict_offsets']
assert certificate['pair_count'] == len(offsets) == 512 * 511 // 2
checked = 0
for index, (i, j) in enumerate(combinations(range(512), 2)):
    k = offsets[index]
    assert type(k) is int and 0 <= k < 12
    first, second = word[(i+k) % 512], word[(j+k) % 512]
    assert first in '01' and second in '01' and first != second
    mask_i, value_i = patterns[i]
    mask_j, value_j = patterns[j]
    assert ((value_i ^ value_j) & mask_i & mask_j) != 0
    checked += 1
assert checked == 130816

controls = []
for label, test_word, n, expected in [
    ('known_n4d1', '001*110*', 4, True),
    ('known_n8d1_theorem3_1',
     '0000010*1111101*0010010*1101101*1110000*0001111*1110011*0101100*'
     '1110010*0101001*1000110*0100001*1011110*0101101*0000110*1101001*',
     8, True),
    ('bad_n4_single_bit', '101*110*', 4, False),
    ('bad_n4_all_zero', '000*000*', 4, False),
    ('bad_n12_single_bit', word[:1] + '1' + word[2:], 12, False),
    ('bad_n12_all_zero', ''.join('*' if c == '*' else '0' for c in word),12,False),
    ('rotation_n12', word[509:] + word[:509], 12, True),
    ('reflection_n12', word[::-1], 12, True),
    ('alphabet_complement_n12', word.translate(str.maketrans('01','10')),12,True),
]:
    ds, cs, _, _ = check(test_word, n)
    observed = cs == [1] * (1 << n) and len(set(ds)) == 1
    assert observed == expected
    controls.append(dict(label=label, expected_valid=expected, observed_valid=observed,
                         minimum_count=min(cs), maximum_count=max(cs)))

wrap_words = sum(start >= 501 for start in inverse)
assert wrap_words == 88
report = dict(
    job_id=JOB, snapshot_digest=snapshot['digest'], snapshot_integrity=True,
    source_sha256=sha256((ROOT / 'source.md').read_bytes()).hexdigest(),
    word_sha256=sha256(word.encode()).hexdigest(), a=2, n=12, d=3, length=512,
    octal_digits=128, wildcard_count=word.count('*'), ordinary_count=512-word.count('*'),
    diamondicities=sorted(set(diamonds)), exact_all_word_count=4096,
    all_start_count=512, compatibility_tests=4096*512,
    coverage_count_histogram=dict(Counter(counts)),
    direct_bitmask_comparison_agrees_with_independent_expansion=True,
    saved_inverse_entries_checked=len(inverse),
    saved_pair_conflict_entries_checked=checked,
    all_pairs_also_have_integer_mask_conflicts=True,
    starts_per_total_word=1, completions_per_start=8,
    wrap_starts=11, words_covered_by_wrap_starts=wrap_words,
    controls=controls, no_candidate_program_imports=True, no_solver_dependency=True,
    valid_original_existential_witness=True,
)
target = ROOT / 'audit/referee-verification.json'
target.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report))
