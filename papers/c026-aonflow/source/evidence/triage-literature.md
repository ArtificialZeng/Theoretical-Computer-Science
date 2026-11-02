# Triage source and suitability validation

Job: c026-aonflow-triage-83e920793ea7. Checked 2026-11-02 UTC.
Decision: advance to bounded research; original unresolved; no candidate.

## Original and nearest verified baseline

Bansal, Jambulapati and Saranurak, *Expander Decomposition with Almost Optimal Overhead*, arXiv:2602.15015v2 (28 April 2026), Section 5, printed p.13; official ICALP 2026 article 22, Section 5, Conjecture 5.1. Inspected the supplied full text, official publisher HTML, and live arXiv version history. The question is precisely maximum-cardinality splittable unit-demand admission on undirected unit-edge-capacity graphs with congestion 1. It asks for a polynomial-time log^(1+o(1)) k approximation. Section 5 identifies O(log^2 k) as the baseline and explicitly warns that concurrent-flow decomposition does not automatically handle the interleaved maximum-throughput computations.

Primary URLs: https://arxiv.org/abs/2602.15015v2 and https://drops.dagstuhl.de/storage/00lipics/lipics-vol374-icalp2026/html/LIPIcs.ICALP.2026.22/LIPIcs.ICALP.2026.22.html

Chekuri, Khanna and Shepherd, *Multicommodity Flow, Well-linked Terminals, and Routing Problems*, STOC 2005, pp.183–192: supplied full text, Theorems 2.1 and 3.2, plus the proof of 2.1, inspected. Theorem 3.2 states O(log^2 k) for general edge-capacitated AON. Theorem 2.1 preserves paired terminal weights and total weight Omega(LP/(beta log LP)). Its proof charges deleted edges to lost paths from a FIXED initial fractional path decomposition; this is a useful constraint on any proposed replacement using changing masses. Leaf-terminal normalization handles repeated endpoints without capacity augmentation. Primary: https://chekuri.cs.illinois.edu/papers/well-linked.pdf

CKS, *The All-or-Nothing Multicommodity Flow Problem*, SIAM J. Comput.42(4),1467–1493 (2013), DOI10.1137/100796820: supplied abstract, Section1.2 and Theorems1.2–1.3 inspected. This is the older foundational AON treatment, not the O(log^2 k) improvement. Its online correction concerns augmented-capacity online claims; do not transfer online guarantees to this target. Primary: https://chekuri.cs.illinois.edu/papers/anflow-sicomp.pdf

## Fresh follow-up that changes the proposed toolkit

Aditya Anand, *Greedy Region Growing: Improved Approximations for Cutwidth, Pathwidth, Flow-Expander Decomposition, and More*, arXiv:2610.17237v1, 12 October 2026. Live abstract, Theorems1.4–1.5 and5.1, and AppendixC heading/introduction inspected. The paper states an O(log n log log n) decomposition overhead. Theorem5.1 states a node-mass version; its rational nonnegative extension instead uses log n, not automatically log k. The full HTML search for “all-or” returned no match. No AON resolution was located. These are inspected theorem statements, not an independent proof audit. This is now a closer tool than the intake baseline, but its fixed-weight decomposition still leaves admission, paired masses and exact capacities to be proved.

Primary: https://arxiv.org/abs/2610.17237v1 and https://arxiv.org/html/2610.17237v1 (Sections1.4,5; AppendixC).

A further title match, Chaturvedi et al., *Improved Throughput for All-or-Nothing Multicommodity Flows with Arbitrary Demands*, was checked via the primary arXiv abstract, https://arxiv.org/abs/2005.04533. The advertised results are bicriteria with edge-capacity violation, so do not certify the congestion-1 target.

## Search coverage and limits

Live queries included “all-or-nothing flow” + 2026 + approximation; Conjecture5.1 + Bansal + flow; all-or-nothing + log +2025+Chekuri; and the arbitrary-demands title. Search hits were treated as leads; substantive comparisons above use primary content. Source status: open-supported in inspected 2026 primary sources; no equivalent resolution found in this bounded search, not proof of priority or continued openness. No historical registry was supplied inside this project. No cross-project or transcript search was performed; registry-wide duplicate comparison remains unavailable to this worker.

## Admission and decisive next test

A full improvement from O(log^2 k) to log^(1+o(1)) k on the complete congestion-1 class would address a recent explicit approximation-algorithms conjecture; its payoff is plausibly substantive. Actual novelty, technical depth and STOC competitiveness require future fresh review of a completed theorem. Nothing is accepted here.

First research test: reconstruct CKS Theorem2.1 and its rounding, and write a single explicit interface lemma for replacing its loss accounting with the current node-weighted flow-expander tools. The lemma must specify preserved paired endpoint masses, a telescoping bound in k, polynomial bit complexity, and edge-by-edge capacity accounting for local grouping plus global routing. Check whether rational terminal weights introduce dependence on n or inverse minimum mass. Either prove this interface and connect it to the entire AON algorithm, or find an exact small-LP violation of its stated invariant and repair the program. A failed interface only rejects that method. No finite instance refutes existence of every approximation algorithm. No experiment or proof search was run in TRIAGE.
