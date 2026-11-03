# Current primary-source comparison and proposed mathematical delta

Job c015-imagebound-research-337b679e5617, checked 2026-11-01. This records a
bounded novelty screen and the proposer's significance assessment. It is not
a fresh referee verdict, external review, or proof of priority.

## Primary records actually checked

1. Stefan Kiefer and Andrew Ryzhikov, *The Complexity of Reachability Problems
   in Strongly Connected Finite Automata*, MFCS 2025, 62:1--19,
   DOI [10.4230/LIPIcs.MFCS.2025.62](https://doi.org/10.4230/LIPIcs.MFCS.2025.62).
   Local intake/primary.txt and intake/primary.pdf: Sections 2, 7 and 9.
   The global all-word definition and the stated upper bound match source.md;
   the final question is “Is this bound tight?” The current
   [arXiv record](https://arxiv.org/abs/2504.13784) still lists v2,
   2025-07-23. The source does not itself spell out the fixed-k asymptotic
   quantifiers; those are explicitly assigned by the user and frozen in
   problem.md. Our theorem covers all of them, not just a special value of k.

2. Andrew Ryzhikov, *On shortest products for nonnegative matrix mortality*,
   RP 2024, 104--119, DOI 10.1007/978-3-031-72621-7_8; current
   [arXiv:2405.19622v4](https://arxiv.org/html/2405.19622v4), 2025-06-15.
   Inspected Sections 1, 2.2, 4 and 5. Section 4 recalls the sharp arbitrary-
   alphabet partial-DFA bound n(n+1)/2, attributed there to Rystsov 1997;
   the original Rystsov proof was not separately checked in this pass.
   The simple binary DFA in Section 4 has a cyclic queue and a deterministic
   excursion, and is the direct structural motivation for our transition
   rule. Its proof does not assert a globally k-image-bounded construction
   for k>=2. Section 3's unrestricted-NFA exponential bounds do not impose
   the global fixed-k promise. Correction to earlier intake wording: the
   simple DFA construction is in Section 4 of v4, not Section 5.

3. Dmitry Ananichev and Vojtech Vorel, *A new lower bound for reset threshold
   of binary synchronizing automata with sink*, J. Automata, Languages and
   Combinatorics 24(2--4):153--164 (2019), DOI 10.25596/jalc-2019-153.
   [Publisher first page](https://jalc.de/issues/2019/issue_24_2-4/abs-153.pdf)
   verifies the published authors/title/scope. The earlier single-author
   [arXiv:1701.07954v1](https://arxiv.org/pdf/1701.07954), Section 2,
   contains the deterministic tail construction and Lemma 2.1: appending a
   tail of length h, a multiple of the permutation order, adds nh to the
   reset threshold of an n-state almost-permutation automaton. The tail
   uses h additional states. This verifies the older sequential-delay
   mechanism, but not the compressed k-clock realization or its image bound.
   The complete 2019 journal text was not obtained; we do not attribute a
   verified journal lemma number to the arXiv version.

4. Stefan Kiefer and Andrew Ryzhikov, *The Asymptotic Size of Finite Irreducible
   Semigroups of Rational Matrices*, STACS 2026, 60:1--20,
   DOI [10.4230/LIPIcs.STACS.2026.60](https://doi.org/10.4230/LIPIcs.STACS.2026.60).
   [Publisher text](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.60/LIPIcs.STACS.2026.60.html),
   Sections 1--2 and Theorem 29 inspected. Its mortality bound 3^(n^2)
   assumes a finite ordinary rational matrix semigroup. Finiteness of the
   Boolean support semigroup does not imply that hypothesis. The current
   [author publication list](https://sites.google.com/site/ryzandrew/research)
   was also checked for follow-ups.

5. Rahul Chandelkar and Samrath Singh Chadha, *Quadratic bounds for
   uncompletable words and matrix mortality*,
   [arXiv:2609.30817v2](https://arxiv.org/html/2609.30817v2),
   2026-09-28. Abstract, Introduction and Theorem 1.2 inspected. Its matrix
   theorem assumes joint spectral radius at most one and a vertex meeting
   every cycle in each strongly connected component. These are additional
   hypotheses, absent from the original question. The comparison below
   explicitly shows that our proposed examples fail them; no correctness
   audit or Lean replay of that preprint was attempted.

6. Andrew Ryzhikov, *Mortality and Synchronization of Unambiguous Finite
   Automata*, WORDS 2019, 299--311,
   [DOI 10.1007/978-3-030-28796-2_24](https://link.springer.com/chapter/10.1007/978-3-030-28796-2_24).
   Publisher abstract inspected: polynomial minimum-rank bounds are for
   unambiguous automata; the lower-bound examples mentioned there are
   deterministic. The full chapter was not available from that page.
   Our automata for k>=2 are explicitly ambiguous, as witnessed below.

7. The public exploratory repository *Agentic Conjectures*,
   [problems/nfa-mortal-words/README.md](https://github.com/umaia1234/agentic-conjectures/blob/main/problems/nfa-mortal-words/README.md),
   was encountered through the exact-terminology search. Its own scope is
   finite binary 2-image-bounded enumeration at up to four states and a
   five-state lower-bound witness; it explicitly leaves the asymptotic
   hierarchy unanswered. These computational claims were not independently
   checked or used in our proof. This is a primary record of that work's
   own claims, not a peer-reviewed resolution or a priority certificate.

## Exact separation from ordinary matrix/ambiguity restrictions

Let B be the 0--1 ordinary transition matrix of b in the proposed construction.
There are k distinct b^2 paths from p_0 back to p_0: one through each c_(i,0).
Thus the row vector e_(p_0) B^2 equals k e_(p_0), and by induction

    e_(p_0) B^(2r) = k^r e_(p_0).

For k>=2 the ordinary matrix semigroup is infinite and its joint spectral
radius is at least sqrt(k)>1. It is also not unambiguous or of finite path
width from p_0. Nevertheless all these paths merge into ONE endpoint, so the
global image bound remains k. Further, the underlying graph has the disjoint
a-cycles P,C_1,...,C_k. No single vertex meets every cycle. These direct
observations exclude the 2026 quadratic theorem's hypotheses. They also
explain why bounded ambiguity/tree width and bounded endpoint support cannot
be silently identified.

## Substantive delta proposed for fresh assessment

The queue and the idea of charging repeated delays are known. We claim no
novelty for those pieces, for CRT alone, for k=1, or for the upper bound.
The proposed new construction realizes an L=lcm(ell_i) delay with only
sum_i ell_i clock states and one k-element packet, and forces m+1 such
delays while preserving the GLOBAL endpoint bound under all words.
The injective queue action avoids merging distinct queue states, while
failed clock attempts return only to the separate port p_0. The exact
potential in research-proof.md proves that neither a failed reset nor a
simultaneous new fork can avoid paying a full L for each unit decrease.

A deterministic physical tail of length L has L states, so the cited
tail theorem alone yields only quadratic order in the resulting total
state count. A disjoint CRT packet alone yields only order n^k. The present
packet invariant plus queue potential proves the additional linear factor
without copying the clocks per queue state. The explicit pairwise-coprime
parameter choice supplies all fixed k and every sufficiently large n.
This is a new lower-bound construction and proof relative to the inspected
results, rather than an application of a quoted deterministic theorem whose
hypotheses already contain the desired fixed-k examples.

The proposed mathematical payoff is to determine the optimal polynomial
exponent at EVERY level of the frozen hierarchy, even under a binary alphabet
and strong connectivity. That payoff warrants a fresh correctness and value
review; elementary methods by themselves do not establish or refute
publication significance. No STOC suitability or acceptance is asserted.

## Search scope and access limits

Searches covered exact source title, k-image-bounded mortality/tightness,
image-bounded NFAs lower bounds, bounded image mortality, bounded
nondeterminism mortality, bounded width mortal automata, bounded row-support
semigroups, and queue/clock variants. Only primary records above support the
attributions. No equivalent full hierarchy resolution was found in these
checked sources on 2026-11-01. This finite screen cannot establish exhaustive
novelty; a referee should repeat a focused equivalent-terminology check.

Three direct Python network downloads failed with URLError under the execution
environment, although the cited HTML/README contents were accessible and
inspected with the web tool. evidence/research-source-receipts.json preserves
those failed requests; no nonexistent local download is offered as evidence.
Two initial web link-click calls also failed before the same links were opened
successfully using their page reference IDs. These operational failures have
no mathematical meaning and do not erase any research counter or failure.
