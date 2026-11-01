# Fresh mathematical referee assessment

**Verdict: accept the exact frozen resolution-paper claim.** The binary
(n,d,L)=(12,3,512) word is a valid nontrivial upcycle. It answers the
immutable existential Question 9.2 affirmatively in full scope. The new
existence phenomenon has substantive mathematical value relative to the
primary results checked below.

Referee job: `c012-upcycles-referee-9a733cb83e73`.
Snapshot: `920933319e6b98bd521f6c300a93b0e7fa46ae3d6600fa970801ea528789f85e`.

## Input boundary and scope

I read source.md, problem.md, claim.json, audit/snapshot.json and the listed
decisive evidence, plus the required project policies and supervisor note.
I did not read checkpoint.md, state.json, previous audit verdicts, owner
confidence, job transcripts or separate progress summaries. The supervisor
note's finite checks were not adopted as a fresh verdict. Actual cited
primary results were reopened independently.

All frozen file hashes and the canonical snapshot digest were recomputed
successfully. The immutable source hash remains
`773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac`.
No frozen file or proposed claim was changed during review.

The source asks existence over all finite alphabets and orders. One binary
example with d>=2 suffices for an affirmative answer; it does not require
all parameter triples to be realized. Conversely, the earlier finite
negative searches would not suffice. Acceptance here uses only the positive
word. No minimality, d=2 existence, general construction, classification,
or answer to Conjecture 9.1 is inferred.

## Reconstruction from definitions

Decode the four displayed strings of octal digits in the frozen proof by
replacing each digit b by a wildcard followed by its three binary bits.
There are 128 digits and therefore 512 positions. The reconstructed word
agrees exactly with witness.json and word.txt. Its SHA256 without a trailing
newline is
`c52b51a5317f1aa0080108366f9253d68e33e0723136a8ab261dadc8f5b73bb3`.

The wildcard positions are exactly zero modulo four. Since four divides
512, this statement remains true across the cyclic boundary. Every window
of twelve positions therefore has exactly three wildcards and nine ordinary
positions. The word contains 128 wildcards and 384 ordinary symbols; its
length exceeds twelve. It is nontrivial, and each window has exactly eight
distinct total-word completions. In particular, there are no repeated
physical positions within a window.

For starting index i let C_i be the subset of {0,1}^12 compatible with the
window at i. Two such sets are disjoint exactly when the windows specify
opposite ordinary bits at some common offset. If there is no opposite pair,
choose the value specified by either window at each specified coordinate
and an arbitrary bit at each remaining coordinate; this gives a common
completion. This proves the equivalence, including shared global character
positions: all comparisons use the same serialized cyclic word.

I verified the saved conflict offset for every pair i<j, with no omissions:
130816 pairs. Every offset is an integer from zero to eleven and points
to two ordinary, unequal characters. Thus the C_i are pairwise disjoint.
Their total size is 512 times 8 = 4096 = |{0,1}^12|. They partition the
entire space, with each total word covered at exactly one starting index.
This is a complete finite existence proof; it does not depend on any SAT
encoding, solver response, connectivity lemma or negative-search result.

## Independent exact computation and adversarial checks

The new audit/referee-verifier.py imports neither candidate checker nor
discovery code. It constructs integer masks M_i and values V_i from each
cyclic window, using the bit for offset k at position 11-k. Compatibility
with total word x is exactly (x & M_i) == V_i. Testing all 4096 integers
against all 512 starts (2097152 tests) gives exactly one match each.

Independently within this fresh implementation, expanding every wildcard
assignment in every window produces the same count array, all entries one.
All 4096 saved inverse-coverage entries agree with the fresh results, and
every start is used eight times. All 130816 pairs also satisfy the integer
conflict formula ((V_i XOR V_j) & M_i & M_j) != 0, in addition to the
literal saved-offset check. The eleven wrapping starts account for 88
distinct total words and are included in both coverage computations.

The published n=4,d=1 word and the first n=8,d=1 word of Theorem 3.1 pass
the fresh checker. Single-bit damaged and all-zero n=4 and n=12 controls
are rejected, with both missing and multiply covered words. Rotating,
reversing and complementing the candidate preserve its verified property.
Detailed results are in audit/referee-verification.json. The candidate's
larger verification script was inspected but not rerun because it also
reads a control file outside the frozen packet. No such dependency is
needed for this review.

These are exhaustive integer computations at the complete quantified
finite ranges, rather than samples or floating-point evidence. They are
reproducible Python checks, without a claim of proof-assistant certification.

## Prior work, novelty and substantive value

The independently opened
[2026 publisher paper](https://link.springer.com/article/10.1007/s10623-026-01841-x)
has the same definitions and Question 9.2 as the frozen source. Its
Theorem 3.1 gives n=8,d=1 examples; its alphabet multiplier retains d;
its frame restrictions do not supply the new example. Its Remark 6.6
explicitly identifies d>1 existence as open. The current
[arXiv record](https://arxiv.org/abs/2310.13067) lists v3 from 14 April 2025.

The [2025 tori paper](https://link.springer.com/article/10.1007/s10623-025-01609-9),
Definition 8.2 and Section 9, distinguishes multi-cycle quasi-families and
also records the d=1 boundary of then-known examples. This candidate is a
single cyclic word by direct verification. The independent current
search and author-page check found no equivalent resolution; the source
comparisons, queries and limits are recorded in audit/referee-literature.md.

The substantive delta is the first d>1 upcycle found in that literature
screen and the resulting affirmative answer to the full published question.
It is not merely another d=1 example, a routine consequence of an existing
alphabet multiplier, a bound on allowed frames, or a disconnected cover.
Known operations preserving d cannot obtain it from the previous d=1
examples. The verification being elementary once a seed is supplied does
not make the seed's existence an elementary corollary of prior work.

The result establishes that a single universal cycle can accommodate
multiple independent wildcards in every window, changing a previously
unknown existence boundary. It also provides a concrete base object to
which existing structural and alphabet-multiplication results apply. The
facts 12 does not divide 512 and the frame has period four place it in a
distinct regime already highlighted by the source. These give substantive
value to a focused combinatorics resolution, without asserting a new
general method or judging suitability for STOC.

## Gaps, limitations and disposition

No mathematical gap was found in the frozen existential claim, its
certificate argument or its complete verification. No claim revision is
needed. The novelty finding is a bounded current primary-source screen;
absolute priority and unpublished work cannot be certified by it. This
local fresh review is not external peer review or a guarantee of publication.

The strict project publication policy is satisfied for this exact
resolution-paper scope. Acceptance does not extend to the unneeded
discovery-method claims or earlier finite nonexistence experiments, which
were not independently audited here. No manuscript or PDF was authored,
and no submission, upload or external contact was made. The structural
check-math gate is recorded separately; that gate checks integrity and
provenance rather than mathematical truth.
