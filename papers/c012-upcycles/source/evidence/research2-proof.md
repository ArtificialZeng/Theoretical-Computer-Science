# Proposed affirmative resolution: an explicit binary upcycle of diamondicity three

This is a mathematical evidence packet for fresh review, not an accepted
manuscript. Its claim is the full existential question in `source.md`, answered
affirmatively by one finite witness. No minimality, classification, general
construction, or resolution of the diamondicity-one conjecture is claimed.

## Exact statement and witness

There exists a nontrivial universal partial cycle over {0,1} for words of
length 12, with diamondicity 3 and cyclic length 512.

Concatenate the following four strings into a string P of 128 octal digits:

```text
00177617563754173657321716771457
12371016661655164636441633162656
22161556133611160676045602151214
46141314063206120412261006540236
```

Replace each digit b in P by `*` followed by the three-bit binary expansion
of b, including leading zeroes. Concatenate these 128 blocks and read the
resulting word u cyclically, with zero-based indices modulo 512. The exact
word is also serialized in `research2-witness/witness.json` and `word.txt`.
Its SHA256, excluding a trailing newline, is
`c52b51a5317f1aa0080108366f9253d68e33e0723136a8ab261dadc8f5b73bb3`.
Hashes are integrity checks, not mathematical premises.

## Complete finite certificate argument

Let W_i=(u[i+k]) for 0<=k<12, at each of the 512 distinct starting indices.
Let C_i be the set of binary 12-words compatible with W_i, where each wildcard
is independently replaced by 0 or 1. The word has a wildcard precisely at
indices congruent to zero modulo 4. Every 12 consecutive positions contain
exactly three such indices, including across the cyclic boundary, since
4 divides 512. Hence every C_i has size 2^3=8. There are ordinary symbols
and wildcards, and 512>12, so the nontriviality requirements hold.

Two sets C_i and C_j are disjoint if and only if some offset k has two
ordinary, unequal symbols in W_i and W_j. The forward implication follows
contrapositively: in the absence of such an offset, choose their common
ordinary value wherever either window specifies one, and any binary value
elsewhere, to obtain a simultaneous completion. The reverse implication is
immediate from the contradictory specified symbols.

`research2-witness/pair-conflicts.json` gives a conflict offset k in {0,...,11}
for every pair i<j, ordered first by increasing i and then by increasing j.
There are exactly binomial(512,2)=130816 entries and no failures.
`research2_verify_witness.py` constructs and then checks EVERY entry directly
against the serialized word, using the nested loops over all these pairs.
Thus the C_i are pairwise disjoint. Their union is a subset of {0,1}^12 and
has size 512*8=4096=2^12. It is therefore all of {0,1}^12. Each word has exactly
one compatible starting index. This proves the assertion and answers the
immutable Question 9.2 affirmatively.

The finite certificate premise can also be checked without the saved pair
table: the self-contained `research2-witness/minimal_check.py` reconstructs
u from the displayed digits, enumerates all 4096 binary words, and for each
one directly compares all 512 cyclic windows. Every exact integer count is 1.
The verifier uses only the Python standard library and has no SAT, graph,
prior verifier, or saved solver-model dependency. Its entire check is:

```python
from itertools import product
P = ('00177617563754173657321716771457'
     '12371016661655164636441633162656'
     '22161556133611160676045602151214'
     '46141314063206120412261006540236')
u = ''.join('*' + format(int(b), '03b') for b in P)
assert len(P) == 128 and len(u) == 512
assert all((c == '*') == (i % 4 == 0) for i, c in enumerate(u))
W = [''.join(u[(i+k) % 512] for k in range(12)) for i in range(512)]
assert all(w.count('*') == 3 for w in W)
for x in product('01', repeat=12):
    assert sum(all(c == '*' or c == b for c, b in zip(w, x)) for w in W) == 1
```

These are exhaustive exact finite checks with stated ranges, not a bounded
negative search or a numerical fit. A reviewer should rerun them or provide
another implementation. No external formal verification is claimed.

## Corroboration, controls, and discovery provenance

The discovery program independently expanded every cyclic window's eight
completions into a 4096-entry count array; all entries were 1. The standalone
verifier instead enumerated all total words and directly tested all starting
indices. Its full inverse table is `research2-witness/inverse-coverage.json`:
each total word has one index, and every index occurs eight times. The 11
windows crossing the boundary uniquely cover 88 words, all included in the
checks. The source n4d1/n8d1 controls pass; flipped-bit and all-zero controls
at n4 and n12 fail. These are checks within this research context, not a fresh
referee or independent peer review.

The witness was found by exact cover of binary 12-words by possible partial
12-tiles, balanced literal 11-symbol overlaps, and guarded connectivity cuts.
After component counts 22 and 32, the third model had one component of 512
edges. An Euler tour produced the word above. Both guards were tested on all
512 subgraphs of the directed three-vertex graph, including loops. The known
negative n8d2 period-4 case became UNSAT after two cut rounds; its final CNF
certificate passed the separate LRAT/RUP checker. All attempts and cut groups
are retained in `research2-connectivity/`. None of those solver claims is
needed to validate the displayed positive witness.

The exact-cover/Euler idea and standard connectivity cuts are not claimed as
new general methods. The proposed substantive contribution is an explicit
upcycle with d>1 resolving the published existence question. No theorem from
the prior literature is needed for the finite existence proof itself.

## Prior work, novelty and limits

The [July 2026 primary paper](https://link.springer.com/article/10.1007/s10623-026-01841-x)
by Fillmore, Goeckner, Kirsch, Martin and McGinnis asks the original question
in Section 9, Question 9.2, and identifies its open status in Remark 6.6.
Theorem 3.1 supplies binary n8 examples with d=1. Theorem 5.1/Corollary 5.2
multiply the alphabet size while retaining n and d; that operation does not
produce this d=3 witness from the known d=1 examples. The frame-period
restriction in Theorem 8.2 and the period-four restriction in Corollary 8.14
allow the present parameters without constructing them.

The [2025 tori paper](https://link.springer.com/article/10.1007/s10623-025-01609-9)
by Carey, Kearney, Kirsch and Popescu already introduces universal partial
quasi-families (Section 8); its Section 9 discusses the then-known d=1 setting.
A disconnected quasi-family would not answer the original question. The
present witness is one cyclic word, verified directly as such. Also,
12 does not divide 512, so it realizes the nondivisible-length regime raised
immediately after Question 9.2; no further theory of that regime is claimed.

Primary pages, the latest arXiv record (v3, 14 April 2025), an author's current
publication page, and the author-cited code repository were rechecked on
1 November 2026. Targeted searches using n12, 512, d3 and d>1 found no equivalent
resolution in the inspected sources. Exact records and limits are in
`research2-literature.md` and the saved web records. This is a bounded novelty
screen, not a proof of priority. A fresh referee must assess correctness,
current novelty, and substantive theoretical significance before acceptance.

Known mathematical gaps in the finite witness argument: none identified by
the researcher. Fresh mathematical, novelty and significance review remains
pending. No manuscript, PDF, external submission, upload, or contact was made.
