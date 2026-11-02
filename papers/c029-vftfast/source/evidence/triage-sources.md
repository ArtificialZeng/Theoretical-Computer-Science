# Bounded triage evidence

Job: c029-vftfast-triage-c8f458fcdb95. Role: triage. Date: 2026-11-02 UTC.
Entry clock: 04:49:05; final source/model discrimination completed by 04:50:27,
before the 04:51:03 main-test closing time. No agents, background workers,
proof experiments, exhaustive diagnostic reruns, manuscript or PDF were created.

## Source status and inspected evidence

The intake manifest and handoff were read. All six supplied primary input hashes
and source.md against its existing runner digest were verified; see
triage-integrity.json. The following sources were actually inspected, not merely
identified from search snippets.

1. Parter, Popova, Tzalik, *New Fault-Tolerant (alpha,beta)-Spanners*,
   https://arxiv.org/abs/2610.33934 and
   https://arxiv.org/html/2610.33934v1 . Live retrieval on 2026-11-02 shows only
   v1, submitted 24 October 2026. Theorem 1.4, printed p.4, establishes the
   near-linear-fault size/stretch tradeoff. Printed pp.4--5 explicitly leave the
   running-time improvement open; Section 2.3 and Algorithm 1 (printed pp.24--25)
   enumerate length-d paths and require a fault witness avoiding the entire path.
   Local text inspected at lines 165--220, 460--490 and 1385--1468. The live HTML
   independently confirms the theorem, running-time discussion and parameters.
   Theorem 1.3/Corollary 3.20 have larger polynomial dependence on f; Question 1.2
   is answered in the same paper and is not the frozen question.
2. Dinitz, Robelle, *Efficient and Simple Algorithms for Fault-Tolerant Spanners*,
   https://arxiv.org/abs/2002.10889v2 ; supplied version dated 24 May 2020.
   Theorem 2 (printed p.3) gives a polynomial-time (2k-1,0) construction with
   O(k*f^(1-1/k)*n^(1+1/k)) edges. Section 3.1, Algorithm 2 and Theorem 4
   (printed pp.5--6) give a length-bounded-cut gap test by repeated BFS and
   deletion of internal path vertices, allowing a factor-t fault inflation.
   These local primary passages were inspected. The published PODC 2020 record
   is also cited precisely in the new source bibliography.
3. Bodwin, Dinitz, Robelle, *Optimal Vertex Fault-Tolerant Spanners in Polynomial
   Time*, https://arxiv.org/abs/2007.08401v3 ; supplied version dated
   31 October 2020. Theorem 1.3 and Section 1.2.1 (printed pp.3--4) give
   randomized polynomial-time optimal-size (2k-1,0) VFT spanners, using induced
   subgraph sampling. These local primary passages were inspected. This is
   SODA 2021, pp.2924--2938, as the new source bibliography confirms.
4. The live author publications page,
   https://www.weizmann.ac.il/math/parter/publications , lists the new source as
   SODA 2027. This establishes a current author-side record, not a verdict about
   our target or any future research result.

Current searches included the exact new-paper title with polynomial-time terms,
the authors plus fault-spanner/sqrt/polynomial terms, and the two older exact
titles. No equivalent full uniform algorithm was found in this bounded check.
This is **open-supported**, not an exhaustive priority certificate. No historical
registry was supplied inside this project; no cross-project registry or private
transcript was read. Duplicate clearance against a wider registry remains
unverified. No mathematical equivalence with a supplied older result was found.

## Admission discrimination and first test

The immutable question is sharper than merely improving the source's time:
it requires polynomial time uniformly over k and f, all vertex fault sets, and
the same near-linear-fault sparsity. The constants may depend only on fixed
delta. Pure multiplicative algorithms and algorithms polynomial only for fixed
k do not settle it. A successful uniform construction would remove an explicit
algorithmic bottleneck at the source's new size/stretch frontier; its actual
technical and venue significance would require fresh review after resolution.

There are two coupled search variables in Algorithm 1: the chosen path P and
the cut F avoiding V(P). The old cut relaxation does not eliminate n^d path
enumeration, and its unrestricted deletions need not avoid a chosen P.
The decisive first research test is the explicit gap separator in problem.md,
including the transfer of the source packing bound to its insertion sequence.
This test is a proof obligation, not a claimed algorithm or a proved obstruction.
With r=O_delta(log n), replacing f by O(r*f) in the existing size expression
would cost only a polylogarithmic factor. The unknown step is finding P and its
compatible F without enumeration and without invalidating the packing proof.
Any sampling approach must also prove a simultaneous high-probability guarantee
against adaptively selected witnesses. Neither that guarantee nor a separator
has been established in triage.

Decision: advance to bounded research. Candidate kind: none. Original status:
unresolved. No acceptance or venue-readiness assessment is asserted.
