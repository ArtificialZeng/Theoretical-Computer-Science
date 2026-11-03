# Fresh primary-source comparison

Job: c015-imagebound-referee-e7492ff4cfbd. Checked 2026-11-03 Asia/Shanghai
(2026-11-02 UTC). This is a bounded literature screen, not a priority certificate.

1. Stefan Kiefer and Andrew Ryzhikov, *The Complexity of Reachability Problems
   in Strongly Connected Finite Automata*, MFCS 2025, 62:1–19,
   DOI [10.4230/LIPIcs.MFCS.2025.62](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.62).
   The frozen primary text, Section 7, pp.62:14–15, defines the promise over
   every word, explicitly distinguishing endpoint support from path ambiguity.
   Section 9, p.62:16, states the n^(k+1) upper bound and asks tightness.
   The [current arXiv record](https://arxiv.org/abs/2504.13784) still displays
   v2, 2025-07-23. The exact all-k, every-large-n formulation is the user's
   frozen interpretation, not a fully quantified quotation from that paper.

2. Andrew Ryzhikov, *On shortest products for nonnegative matrix mortality*,
   RP 2024, pp.104–119, DOI 10.1007/978-3-031-72621-7_8;
   [arXiv:2405.19622v4, Section 4](https://arxiv.org/html/2405.19622v4).
   Verified the displayed two-block DFA transitions and the accompanying
   deterministic tail interpretation. Its queue action is the clear predecessor
   of the present queue. Its delay block is a physical partial deterministic
   path; it does not implement the present simultaneous clock packet. The
   cited sharp DFA bound is attributed there to Rystsov; the Rystsov original
   was not independently obtained and is not a proof dependency here.

3. D. S. Ananichev, *A new lower bound for reset threshold of synchronizing
   automata with sink state*,
   [arXiv:1701.07954v1, Section 2, Lemma 2.1](https://arxiv.org/pdf/1701.07954).
   Verified the definition of appending h additional tail states and the
   reset-threshold increase n h when h is a multiple of the permutation
   order. The text credits Vorel's earlier lemma. This proves that sequential
   delay amplification is prior work. It does not provide a compressed
   k-image packet, nor the all-word invariant needed here. The revised 2019
   coauthored journal text was not independently reviewed in this job.

4. Stefan Kiefer and Andrew Ryzhikov, *The Asymptotic Size of Finite
   Irreducible Semigroups of Rational Matrices*, STACS 2026, Theorem 29,
   DOI [10.4230/LIPIcs.STACS.2026.60](https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.60/LIPIcs.STACS.2026.60.html).
   The theorem bounds mortality by 3^(n^2) for a finite ordinary rational
   matrix semigroup. That finiteness hypothesis does not hold for these
   examples: the b matrix has k length-two returns from p_0 to itself, so its
   even powers have entry k^r there. Finiteness of Boolean supports is different.

5. Rahul Chandelkar and Samrath Singh Chadha, *Quadratic bounds for
   uncompletable words and matrix mortality*,
   [arXiv:2609.30817v2, Theorem 1.2](https://arxiv.org/html/2609.30817v2).
   Verified the stated joint-spectral-radius and cycle-hub hypotheses.
   Here rho(B)>=sqrt(k)>1 for k>=2 by the same exact b^2 calculation.
   Also the disjoint a-cycles preclude a common cycle hub. Thus this theorem
   does not subsume or contradict the candidate. No independent correctness
   review of that preprint or its formalization was performed.

6. The primary exploratory record
   [Agentic Conjectures, nfa-mortal-words](https://github.com/umaia1234/agentic-conjectures/blob/main/problems/nfa-mortal-words/README.md)
   explicitly limits its extremal claims to small binary automata. Its finite
   experiments are not an asymptotic hierarchy theorem. They were not reused
   or certified here.

Fresh searches covered the exact source title, k-image-bounded mortal-word
tightness/lower bounds, image-bounded mortality in 2026, bounded nondeterminism
and mortal words, and bounded row-support semigroups. The
[source author's research list](https://sites.google.com/site/ryzandrew/research)
was also inspected for relevant subsequent work. No equivalent full hierarchy
resolution appeared in the inspected primary sources. Searches with broader
terminology returned substantial irrelevant material; no inference is drawn
from that noise. This finite screen cannot exclude all unpublished or differently
indexed work.

The substantive comparison is precise: a physical delay of L states together
with a queue does not give n^(k+1) in the total number of states; an isolated
k-clock packet gives only one expensive event. The frozen construction shares
the same sum(ell_i) clock states across m+1 charged events. Compatibility of
that sharing with the global endpoint bound and the exact no-shortcut potential
is the new ingredient relative to the verified prior constructions.
