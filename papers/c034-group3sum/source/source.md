# Prospective immutable original: all bounded-exponent abelian-group3SUM

Primary: Ruhollah Majdoddin, *Thin matrix products up to D<=N^0.172 and
lossless reductions for 3SUM, Exact Triangle and APSP, with 3SUM over abelian
groups and a dichotomy for coordinatewise problems*, arXiv:2610.17420v1.
Frozen unmodified primary PDF SHA256:
a536921aea8fe16830262db76c624593c5815094ae495ef5afce8c761d1c3d2e.
Canonical source cache: /Users/mac/Documents/ChatGPT/STOC理论计算机/research/continuous/prospective/20261102T1415Z-geometry/2610.17420v1.pdf;
after standardADD also supplied at intake/primary/2610.17420v1.pdf.
The actual current arXiv record displayed v1 only
on2026-11-02. The author repository current main was inspected at
63e9490d3b5d62bf8b9f7f0a8103b0e409564a9d; its pinned README/tree show the same
prior scopes. No later full resolution was found in the bounded primary search;
this is not a global priority certificate or full audit of the source's proofs.

Original position: Open Problem19.26, Section19 Model.

## Exact mathematical reading

For every fixed integer M>=2, establish a uniform classical algorithm with a
fixed δ_M>0 independent of c, such that for every fixed c>0, every n and every
compactly given finite abelian G=product_i Z_(m_i), m_i dividing M and |G|<=n^c,
three lists S1,S2,S3 of at most n residue vectors are solved in
O_{M,c}(n^(2-δ_M) polylog(n)) charged bit/word operations. Return x_i in S_i with
x1+x2+x3=0 when one exists, and correctly report absence otherwise. Randomness,
if used, must have bounded error on each fixed input with an honest total cap.
All hashing, grouping, list generation, query calls, recovery and arithmetic
are charged. The saving is fixed for M and cannot vanish with n or c.

All compactly described abelian groups of that exponent are included, not
only one p³ case or equal-rank homogeneous groups. The routine embedding
x_i -> (M/m_i)x_i into Z_M^r can be used with its changed polynomial order bound.
The source's conditional Hdet formulation must be instantiated by an actually
verified prior primitive for an unconditional algorithm, not a new assumed
counting/sampling or matrix oracle. A stronger counting result may be useful
only when its actual costs and witness interface are proved.

## Prior and first test

Theorem19.17 already claims the complete exponent-dividing-p² class. In
particular Z4^d x F2^d is covered by its explicit embedding, despite its erroneous
appearance in the later list of open examples. Do not research or publish that
known subcase. Elementary groups and boundedly many cyclic factors are also
prior. Higher prime-power and mixed-prime layers motivate the full question.

The first bounded test is to reconstruct the source's light/heavy p² proof
and determine whether a FULL bounded-layer induction can satisfy the cost and
false-positive potentials in all layers simultaneously, starting with Z8 as
a diagnostic case. A Z8-only algorithm would remain partial to this packet.
Charge the total number, sizes and recovery of all subinstances. Do not assume
that a group-valued Exact Triangle theorem automatically supplies a small-node
3SUM or convolution reduction: an integer almost-linear hash need not exist
for torsion groups. Original fullscope and substantive new method are mandatory.

## Scope and publication boundary

This is a prospective source packet; no queue admission or research pass is
asserted. The original wording is frozen in the unmodified primary PDF above,
with version, exact position and hash; the following mathematical reading must
not be narrowed after admission. Preserve source.md bytes once installed.
Only complete original resolution with substantive innovation and actual fresh
correctness/novelty/value acceptance may become a resolution-paper. A special
case, conjecture, failed route, routine deduction or unverified claim remains
Markdown/code only. No manuscript or PDF for those outcomes.

A failed algorithm is not a lower bound on all algorithms. Conditional barriers
must state their assumptions and do not by themselves disprove an unconditional
algorithm-existence claim. Never reopen an already claimed resolution simply
because review or formalization is absent. Full original statements and current
follow-ups must be checked in TRIAGE before research.

Future manuscript author, if qualified: Zijian Zeng; UCSI University;
1002266693@ucsiuniversity.edu.my. Apply the shared STOC quality standard, the
12TOTALpage cap, official unmodified acmart, full proofs and truthful AI roles.
No external upload/submission/contact.
