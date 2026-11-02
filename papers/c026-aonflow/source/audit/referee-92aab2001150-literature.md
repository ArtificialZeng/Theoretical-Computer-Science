# Fresh primary-source comparison

Job: c026-aonflow-referee-92aab2001150. Date: 2026-11-02 UTC.
Snapshot: 573d5e72b132c0772447265073b14686ec1c85b65a6c5a6769030620d3e0eadd.

The review read the listed frozen primary texts, not prior audit verdicts or
checkpoint/state files. Fresh extraction from all three listed PDFs matches
their supplied text after whitespace normalization.

* Bansal--Jambulapati--Saranurak, *Expander Decomposition with Almost Optimal
  Overhead*, [arXiv v2](https://arxiv.org/abs/2602.15015v2), 28 April 2026;
  [official ICALP 2026 article](https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.22/LIPIcs.ICALP.2026.22.html).
  The live record still lists v2. Theorem 3.1 gives the integral-weight,
  total-weight-sensitive decomposition used here; Section 5 still states
  Conjecture 5.1 and the O(log^2 k) AON baseline. The new claim addresses its
  admission interface by a fixed prepared path family, rather than substituting
  a theorem for adaptive maximum-throughput recursion.
* Chekuri--Khanna--Shepherd, *Multicommodity Flow, Well-linked Terminals, and
  Routing Problems*, STOC 2005, 183--192, DOI 10.1145/1060590.1060618,
  [author PDF](https://chekuri.cs.illinois.edu/papers/well-linked.pdf).
  The live primary PDF was accessible. Theorem 3.1 (PDF page 7 of 10) states
  precisely the uniform edge-flow-linked matching rounding needed here;
  its footnote requires strengthened clustering. Theorem 3.2 supplies the
  O(log^2 k) baseline. Lemma 1.1 already supplies path uniformization and
  terminal duplication; these are not new contributions of this candidate.
* Chekuri--Khanna--Shepherd, *The All-or-Nothing Multicommodity Flow Problem*,
  SIAM J. Comput. 42(4), 1467--1493 (2013), DOI 10.1137/100796820.
  The frozen published PDF and text were inspected, especially Lemmas
  3.3--3.4 and Section 3.4, pp.1478--1483. Theorem 3.8 is formally for nice
  Raecke-tree instances; it must not be directly quoted as a theorem about
  arbitrary components. The dependency transfer is assessed explicitly in
  audit/math.md. The published PDF URL timed out; the alternate
  [author journal preprint](https://chekuri.cs.illinois.edu/papers/anflow-journal.pdf)
  was accessible and is dated 19 November 2012. It is not substituted for
  the frozen published version. DOI landing-page refreshes returned 403.
* Anand, *Greedy Region Growing: Improved Approximations for Cutwidth,
  Pathwidth, Flow-Expander Decomposition, and More*,
  [arXiv:2610.17237v1](https://arxiv.org/abs/2610.17237v1), 12 October 2026;
  [primary full text](https://arxiv.org/html/2610.17237v1).
  Theorems 1.4 and 5.1 improve flow-expander overhead; Appendix C allows
  nonnegative rational weights with n-sensitive logarithms. No all-or-nothing
  theorem was located in this full text. This result is a relevant improvement
  to a tool, not an equivalent original-scope admission algorithm.

Fresh searches included exact all-or-nothing flow with 2026 approximation,
the BJS conjecture, terminal copies and flow-linked rounding, and all-or-nothing
with flow-expander decomposition. Results examined against primary sources
did not reveal an equivalent full-target approximation. This is a bounded
comparison, not a proof of priority or an exhaustive literature certificate.
Unrelated traffic-assignment and statistical all-or-nothing results were not
used. No source-access failure is treated as mathematical evidence.
