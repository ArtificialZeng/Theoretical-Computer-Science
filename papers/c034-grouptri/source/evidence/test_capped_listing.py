"""Exact finite semantic tests; brute detector is not a fast backend benchmark."""
import hashlib
import itertools
import json
from pathlib import Path


def listing(relation, sizes, cap, cutoff, outer_mask, reverse=False):
    n = max(1, *sizes)
    N = 1 << (n - 1).bit_length()
    out = []
    count = {}
    positive = {}
    calls = {}

    def active(a, b, c):
        return (a < sizes[0] and b < sizes[1] and c < sizes[2]
                and (a, b) in outer_mask and (a, b, c) in relation
                and count.get((a, b), 0) < cap)

    def visit(A, B, C, depth):
        calls[depth] = calls.get(depth, 0) + 1
        if not any(active(a, b, c) for a in A for b in B for c in C):
            return
        positive[depth] = positive.get(depth, 0) + 1
        start = len(out)
        if len(A) <= cutoff:
            for a in A:
                for b in B:
                    for c in C:
                        if active(a, b, c):
                            out.append((a, b, c))
                            count[a, b] = count.get((a, b), 0) + 1
        else:
            half = len(A) // 2
            children = list(itertools.product((A[:half], A[half:]),
                                             (B[:half], B[half:]),
                                             (C[:half], C[half:])))
            if reverse:
                children.reverse()
            for child in children:
                visit(*child, depth + 1)
        assert len(out) > start, "positive cube emitted nothing"

    visit(tuple(range(N)), tuple(range(N)), tuple(range(N)), 0)
    assert len(out) == len(set(out))
    for a in range(sizes[0]):
        for b in range(sizes[1]):
            truth = sum((a, b, c) in relation and (a, b) in outer_mask
                        for c in range(sizes[2]))
            assert count.get((a, b), 0) == min(truth, cap)
    assert all(number <= len(out) for number in positive.values())
    assert all(number <= 8 ** depth for depth, number in calls.items())
    return len(out), sum(calls.values())


def run():
    tested = 0
    outputs = 0
    oracle_calls = 0
    triples = list(itertools.product(range(2), repeat=3))
    pairs = list(itertools.product(range(2), repeat=2))
    # Complete arbitrary Boolean triangle relations, so tests do not rely on
    # any algebraic special structure of group-zero triangles.
    for bits in range(1 << len(triples)):
        relation = {t for index, t in enumerate(triples) if bits >> index & 1}
        for maskbits in range(1 << len(pairs)):
            mask = {e for index, e in enumerate(pairs) if maskbits >> index & 1}
            for cap, cutoff, reverse in itertools.product((1, 2, 3), (1, 2), (False, True)):
                z, q = listing(relation, (2, 2, 2), cap, cutoff, mask, reverse)
                tested += 1
                outputs += z
                oracle_calls += q

    # Unequal, padded, empty, structured and larger held-out domains. These
    # are a selected deterministic family, not exhaustive at size >=3.
    held_out = 0
    for sizes in itertools.product(range(5), repeat=3):
        for mode in range(4):
            relation = {t for t in itertools.product(*(range(s) for s in sizes))
                        if mode == 0 or (mode == 1 and sum(t) % 2 == 0)
                        or (mode == 2 and t[2] == 0)
                        or (mode == 3 and t[0] == t[1] == t[2])}
            mask = set(itertools.product(range(sizes[0]), range(sizes[1])))
            for cap, cutoff, reverse in itertools.product((1, 2, 5), (1, 2, 4), (False, True)):
                listing(relation, sizes, cap, cutoff, mask, reverse)
                held_out += 1

    marker_tests = 0
    for modulus in (2, 3, 4, 6):
        for weights in itertools.product(range(modulus), repeat=3):
            for present in itertools.product((False, True), repeat=3):
                encoded = []
                for kind in range(3):
                    encoded.append((weights[kind] if present[kind] else 0,
                                    *(int(not present[kind] and coordinate == kind)
                                      for coordinate in range(3))))
                zero = all(sum(edge[coordinate] for edge in encoded) % modulus == 0
                           for coordinate in range(4))
                expected = all(present) and sum(weights) % modulus == 0
                assert zero == expected
                marker_tests += 1

    return {
        "job_id": "c034-grouptri-research-e96d630c6fdd",
        "status": "passed",
        "exhaustive_relation_tests": tested,
        "exhaustive_domain": "All 256 Boolean relations on [2]^3, all 16 outer-pair masks, caps 1/2/3, cutoffs 1/2, both child orders",
        "total_outputs_in_exhaustive_tests": outputs,
        "brute_detector_calls_in_exhaustive_tests": oracle_calls,
        "held_out_tests": held_out,
        "held_out_domain": "All 125 part-size triples in {0,1,2,3,4}^3 with four specified structured relations, three caps/cutoffs and both child orders",
        "marker_tests": marker_tests,
        "marker_domain": "Every one-coordinate weight triple and every 3-bit presence pattern for moduli 2,3,4,6",
        "limits": "Finite tests exercise bookkeeping and markers; the detector is brute force. They do not validate the asymptotic backend or prove an infinite theorem.",
        "source_sha256": hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


if __name__ == '__main__':
    result = run()
    Path('evidence/capped-listing-tests.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
