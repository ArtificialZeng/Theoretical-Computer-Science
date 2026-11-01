# Precise original problem

Job: c012-upcycles-triage-8176c8933a92; phase: triage; 2026-11-01.
The immutable statement is `source.md`, SHA256
`773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac`.

Fillmore, Goeckner, Kirsch, Martin and McGinnis, *The existence and structure
of universal partial cycles*, Designs, Codes and Cryptography 94, article 152
(2026), DOI 10.1007/s10623-026-01841-x, Section 9, Question 9.2 asks:
“Do there exist upcycles with d > 1?” The supplied arXiv:2310.13067v3,
Sections 2, 8 and 9, has the same question (printed p. 27).

## Definitions and quantifiers

For some integers a >= 2, n >= 1, L >= 1, and 2 <= d < n, is there a cyclic
partial word u in ({0,...,a-1} union {*})^L with an ordinary symbol and a
wildcard such that:

1. For every starting index i in Z/LZ the window (u[i+k])_(0<=k<n) has d
   wildcards, where all indices on u are reduced modulo L.
2. For every total word w in {0,...,a-1}^n, exactly one i in Z/LZ satisfies
   u[i+k] = * or u[i+k] = w[k] for every 0 <= k < n.

Each wildcard occurrence matches independently. The count is over starting
indices, including windows crossing the end; rotations of total words are not
identified. Nontriviality excludes ordinary De Bruijn cycles and the
single-wildcard degenerate cycle. Source Proposition 2.1 implies L > n.
Relabeling a finite alphabet as {0,...,a-1} does not change the question.

This is one existential question over ALL alphabets and orders. One explicit
valid d >= 2 witness gives an affirmative resolution. A negative resolution
must exclude every such a,n,u. No finite negative search answers it negatively.
The source is a question, so a future answer must explicitly say affirmative
or negative rather than rely on the runner's proved/disproved vocabulary.

## Nearest known results and status

The actual v3 PDF was re-extracted and matched to `intake/paper.txt`. Section 2
(pp. 2–3) gives n-periodicity of wildcard positions, L = a^(n-d), and
d L/n total wildcards. Section 8 (pp. 24–27) proves that the frame's minimum
period m divides gcd(n,L) (Theorem 8.2), m >= 4 (Corollary 8.13), and some
rotation of the pane frame is not curtained (Corollary 8.7). A length-m frame
f is k-curtained if for each 0 <= i < k at least one of f[i],f[m-k+i] is a
wildcard. Lemma 8.9 bounds d <= D(n)-1; Table 3 has D(8)=4.
Table 4 permits binary n=8 and 1<=d<=3; it does not assert existence for
d=2 or d=3. Theorem 3.1 supplies n=8,d=1 examples, and Corollary 5.2
multiplies alphabet size while preserving d. These do not resolve this question.

Status: **open-supported**, based on the inspected July 2026 publisher
Question 9.2 and Remark 6.6, the latest arXiv version (v3), and the 2025
*Universal partial tori* paper's Section 9. Bounded current searches found no
equivalent resolution; this is not exhaustive novelty certification.
See `evidence/triage-literature.md` for URLs, positions, date and limits.

## Proposed substantive delta and verification route

Nearest prior result: known examples have d=1, with alphabet multiplication
preserving d. Proposed delta: construct the first nontrivial d>=2 upcycle,
thereby answering the full original question affirmatively. Such a witness
would cross the presently unknown diamondicity boundary, not merely sharpen
a known frame bound. Theoretical significance and novelty require later
independent review. No qualifying contribution is claimed at triage.

First bounded positive-witness search: binary (n,d)=(8,2),(8,3), with L=64,32.
There are respectively 48 and 20 ordinary positions. Enumerate all n-periodic
weight-d masks up to rotations and reversal only. Source exclusions may prune
masks but must be cited as known restrictions.

For a fixed mask assign a Boolean variable x_p to each ordinary position
p modulo L. For each distinct starting pair i,j impose

  OR over k where both positions are ordinary of
  (x_((i+k) mod L) XOR x_((j+k) mod L)).

These constraints are exactly pairwise incompatibility of window subcubes.
Since each window covers 2^d words and L*2^d=2^n, they are equivalent to
unique coverage. Reuse the global position variables, encode XOR equivalences
in both directions, simplify x_p XOR x_p to false, and never introduce
independent free mismatch flags. No arbitrary permutation of coordinates is
a cyclic-word symmetry. Check any model by a separate literal expansion of
all windows into a 256-entry counting array, recomputing L and d.

Use an explicit solver/time cap in the research job, preserve all CNFs/logs,
and report per-mask SAT/UNSAT/unknown separately. A model may answer the full
question; UNSAT settles at most its exact finite encoding; timeouts settle
nothing. If these tests do not find a witness, another pass requires a new
structural kernel or changed construction, not simply a larger SAT cap.

Conjecture 9.1 (d=1), Question 9.4 (D(n)), two-dimensional tori, and isolated
frame classifications are not replacement targets. Unresolved or routine
partial work stays as evidence with no manuscript/PDF under project policy.

## Research pass 1 update (original scope unchanged)

Job `c012-upcycles-research-cfe911474960` completed the initial binary n8d2/d3
test: eight surviving dihedral frame classes are UNSAT, with independently
checked LRAT certificates; the remaining d3 class is excluded by the source's
Corollary 8.7. This is finite nonexistence evidence only. The original remains
unresolved and no publication candidate is asserted.

Failure analysis and a changed tile/Euler encoding now give a verified n12d3
period-4 exact partition of the 4096 total words with balanced literal overlaps,
but its selected graph has 22 components. Multiple cycles do not answer the
question. Connected selection is a precise next constructive kernel; its full
equivalence argument, artifacts, failure limits and bounded proposed test are
in `evidence/research1-results.md`. The quasi-family concept itself is already
in the 2025 tori paper. No novelty of that concept or elementary encoding is
claimed. See `checkpoint.md` for the single next test.

## Research pass 2 update: full-scope affirmative candidate

Job `c012-upcycles-research-456cb4499028` found an explicit binary upcycle
with (a,n,d,L)=(2,12,3,512). The original existential question is proposed
resolved affirmatively, with fresh correctness, novelty and significance
review pending. This does not narrow the original: one such witness suffices
for its full positive answer.

The exact word is in `evidence/research2-witness/witness.json`. A standalone
verifier directly compared every one of 4096 total words with all 512 cyclic
starts and found exactly one match each. A separate pair certificate supplies
an ordinary-symbol conflict for all 130816 distinct starting pairs. Every
12-window contains exactly three wildcards, length is 512=2^(12-3)>12, and
nontriviality and cyclic wrap are checked. The complete finite proof is
`evidence/research2-proof.md`; the small solver-free checker is
`evidence/research2-witness/minimal_check.py`. All claims concern this one
witness and the resulting existential answer; no minimality or general
construction is claimed. No finite negative search was promoted to a global
negative theorem.

Guarded connectivity refinement used three solver calls with component counts
22,32,1, within its predeclared 20-round/180-second ceiling. Known positive and
certified negative controls passed. The primary 2026 paper and current arXiv
record were rechecked, with no equivalent resolution located in the bounded
screen described in `evidence/research2-literature.md`. The proposed new value
is the d>1 existence witness, not novelty of exact-cover/Euler/SAT techniques.
No manuscript/PDF or acceptance is asserted. `claim.json` requests fresh review.
