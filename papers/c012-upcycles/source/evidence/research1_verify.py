"""Independent literal expansion, with no SAT or mismatch-gate dependencies."""
import itertools


def verify(word, n, alphabet_size=2):
    L = len(word)
    assert L and all(c == '*' or 0 <= int(c) < alphabet_size for c in word)
    counts = [0] * alphabet_size**n
    ds = []
    for start in range(L):
        window = [word[(start + k) % L] for k in range(n)]
        wildcards = [k for k, c in enumerate(window) if c == '*']
        ds.append(len(wildcards))
        for replacement in itertools.product(range(alphabet_size), repeat=len(wildcards)):
            total_word = window[:]
            for k, letter in zip(wildcards, replacement):
                total_word[k] = str(letter)
            value = 0
            for letter in total_word:
                value = alphabet_size * value + int(letter)
            counts[value] += 1
    d = ds[0] if len(set(ds)) == 1 else None
    periodic = all((word[i] == '*') == (word[(i + n) % L] == '*') for i in range(L))
    valid = (L > n and '*' in word and any(c != '*' for c in word)
             and d is not None and L == alphabet_size**(n - d)
             and periodic and all(v == 1 for v in counts))
    return dict(valid=valid, word=word, n=n, a=alphabet_size, length=L,
                diamondicities=sorted(set(ds)), diamond_periodic=periodic,
                length_identity=d is not None and L == alphabet_size**(n-d),
                coverage_counts=counts, missing=sum(v == 0 for v in counts),
                multiply_covered=sum(v > 1 for v in counts))
