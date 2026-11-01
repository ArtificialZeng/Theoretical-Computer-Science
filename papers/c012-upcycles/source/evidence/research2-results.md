# Research pass 2 results

Job `c012-upcycles-research-456cb4499028`, 1 November 2026. Decision:
**candidate**, kind **resolution-paper**, original status **proved** in the
sense of an affirmative answer to the frozen existence question. Fresh
correctness, current-novelty and significance review remains pending. No
acceptance, publication quality, manuscript, PDF or external submission is
asserted.

## Decisive new result

An explicit (a,n,d,L)=(2,12,3,512) cyclic word was found and checked. The
word and octal block encoding are in `research2-witness/witness.json`.
`research2-proof.md` gives the complete finite-certificate proof and exact
scope. The standalone verifier checks all 4096 total binary words against all
512 cyclic starting indices and obtains counts identically one. It also
finds and validates an ordinary conflict for every one of 130816 distinct
starting pairs. All windows have three wildcards, the mask is periodic with
period four (hence n-periodic), and 512=2^(12-3)>12. The word has 128 wildcard
positions and 384 ordinary positions. All 11 boundary-crossing starts are
included; they uniquely cover 88 words. This one positive witness answers the
full existential original question; no global negative inference is involved.

## Assigned test and preserved attempts

The changed test implemented the previously specified guarded cuts on exact
subcube cover plus balanced literal 11-symbol overlap. For a selected root
edge r outside a component vertex set S and a possible internal edge e of S,
the added clause is `-y_r OR -y_e OR OR(y_f : f leaves S)`. Soundness follows
because a connected support retaining r and e crosses S, and vertex balance
equates the number of entering and leaving selected edges. The guards allow
later solutions to drop r or omit S. All possible internal e are considered.

The target's three rounds selected 512 tiles each, with component counts
22,32,1. The first model repeated the previous 21 components of length 24 and
one of length 8; the second had 32 components of length 16. The first two
models generated 488 and 496 cuts. The last CNF has 2048 variables and 38360
clauses. A single Euler tour recovers the serialized word, whose validity is
then checked without relying on the graph model. Target solver wall time was
about 0.285 seconds; no timeout or cap escalation occurred. Every intermediate
CNF, proof stream, log, component list and cut set remains in
`research2-connectivity/`.

## Adversarial controls and checking limits

The cut-guard test exhausts all 512 selected subgraphs of the complete directed
three-vertex graph including loops. The 63 nonempty balanced connected supports
satisfy all 1512 tested guarded cuts. Explicit counterexamples show why dropping
either guard is unsound. This finite test supplements the general soundness
argument; it is not a proof of every implementation property.

Pinned source n4d1 and n8d1 and unpinned n4d1 all produce connected valid tours.
A flipped n4 pin is UNSAT. The certified n8d2 period-four negative control gives
four components in each of its first two rounds and is UNSAT in its third.
The separate LRAT/RUP checker verifies both new UNSAT certificates. Its n8
scope is finite only and agrees with the pass-1 global-position certificate.
`research2-benchmarks.json` records all runs.

The standalone word verifier imports no solver or prior build/graph/verifier
module. Its positive source controls pass; n4 and n12 flipped-bit and all-zero
controls fail. `research2-witness/minimal_check.py` is an additional short
solver-free reconstruction and exhaustive check from the printed octal digits.
These computations occurred in this research context. No fresh referee or
external peer review has yet taken place.

## Literature, value, and handoff

The actual July 2026 publisher Question 9.2/Remark 6.6 and latest arXiv record
were rechecked. Bounded targeted searches, the current author's page, and the
author-cited code repository revealed no inspected equivalent resolution.
`research2-literature.md` has precise references, searched scope and limits.
The proposed substantive new value is the explicit upcycle crossing d=1 to
d=3 and thereby resolving the published full existence question. The SAT,
Euler and connectivity tools are not claimed as new general mathematics.

The construction also has 12 not dividing 512, the regime raised immediately
after source Question 9.2. No theory of all such parameters is asserted.
Previous finite failures, their certificates, usage records and counters are
preserved unchanged. Two research passes have now been consumed of three;
no further research expansion is needed before review.

Next test: the designated fresh referee should read only the frozen claim
packet, reconstruct the word from its octal encoding, independently verify
ALL 4096 words and nontriviality/diamondicity/length/cyclic boundary conditions,
then check current primary novelty and substantive significance. Reject if any
of these fail. A positive internal check is not acceptance.
