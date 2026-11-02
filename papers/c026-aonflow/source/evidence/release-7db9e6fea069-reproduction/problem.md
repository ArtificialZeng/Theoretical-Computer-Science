# Precise interpretation of the immutable original

The original text is source.md, SHA256 7241936e887e814eebe18f891cfe9d90c883ee0298057dfc8bbdd2344501e29e, preserved byte for byte. This document interprets it; it does not replace it.

## Objects, feasibility and objective

An input is a finite undirected graph G=(V,E) with unit capacity on every edge and k specified terminal pairs (s_i,t_i), indexed by i in [k]. Endpoints can be shared; terminals need not have degree one. A solution selects I subset [k] and supplies, for each i in I, a nonnegative splittable flow of value exactly one from s_i to t_i. In a path formulation, variables f_(i,P)>=0 satisfy sum_(P in paths(s_i,t_i)) f_(i,P)=1 for i in I, and sum_(i in I,P containing e) f_(i,P)<=1 for every edge e. Finite polynomial-size edge-flow certificates suffice, so exponential path listing is unnecessary. Define OPT(G,P) as the largest cardinality of a feasible I. Unselected commodities receive no admission credit.

Disconnected graphs are allowed: distinct endpoints in separate components cannot be admitted. For k=0 output the empty solution; for k=1 decide connectivity. If coincident endpoints are permitted by input convention, they have a trivial zero-edge route and can be admitted separately. Indexed duplicate pairs, if allowed, remain separate unit demands. These conventions do not create a special graph-class restriction.

## Full quantified algorithmic target

There exist a single uniform polynomial-time algorithm, an absolute constant C, and a function eta(k)->0 such that for every input the algorithm returns a feasible solution of size at least OPT(G,P)/(C log(k+2)^(1+eta(k))). The exponent is an asymptotic guarantee of this one algorithm, not an independent family with superpolynomial dependence on a chosen accuracy parameter. Running time is polynomial in the explicit input bit length. The harmless k+2 convention avoids zero logarithms in small instances.

The source does not explicitly specify a randomized success convention in Conjecture5.1. A deterministic algorithm suffices. A proposed randomized resolution must state and prove its convention: polynomial running time, verifiable congestion-1 feasibility, and at least constant success probability for the cardinality guarantee (amplifiable). Randomized preprocessing occurs in CKS2005, so randomness is not excluded by the surrounding literature, but no success theorem is inferred from the conjecture wording. An expected fractional LP objective is not itself a feasible subset guarantee.

Congestion augmentation, routing less than one for an admitted commodity, planar-only or bounded-degree-only algorithms without a valid reduction, and parameter dependence solely on n instead of k do not resolve the original. A stronger LP-relative guarantee would suffice, but the original asks only approximation relative to OPT. A counterexample to an intermediate lemma, or a large gap for a chosen relaxation, does not disprove existence of the requested algorithm. Any negative resolution must address the full algorithmic assertion, with complexity assumptions explicit.

## Current source status and nearest comparisons

Source status is open-supported: the inspected Bansal–Jambulapati–Saranurak arXiv v2 and official ICALP2026 Section5 state Conjecture5.1, give O(log^2 k) as current AON baseline, and explain that maximum-throughput and concurrent-flow steps prevent a black-box transfer. Their Theorem3.1 is an integral-node-weight flow-expander decomposition theorem, not an AON approximation algorithm. CKS2005 Theorem3.2 is the O(log^2 k) edge-capacitated AON baseline; its Theorem2.1 proves paired weighted well-linked decomposition with Omega(LP/(beta log LP)) retained mass. CKS2013 is the older foundational journal treatment, with a correction to online claims, not the later O(log^2 k) theorem's journal version.

Fresh follow-up: Aditya Anand, arXiv:2610.17237v1 (12 October2026), Theorems1.4–1.5 and5.1, states improved flow-expander overhead O(log n log log n) and node-weighted extensions. The rational-weight extension uses n in its logarithms. These theorem statements do not supply the AON admission and rounding interface. No equivalent full resolution was located in the bounded current primary-source search. This is not a comprehensive priority finding. URLs and precise inspected positions are in evidence/triage-literature.md; original source-input hashes are checked in evidence/triage-integrity.json.

## Proposed delta and one bounded first test

Nearest prior X: CKS2005 O(log^2 k) AON and the 2026 node-weighted flow-expander tools. Proposed delta Y: one complete polynomial-time congestion-1 AON approximation with factor log^(1+o(1)) k for the entire original class. Verification Z: a full algorithm, proof of paired admission and objective retention, exact load analysis and polynomial arithmetic, then fresh correctness/novelty/significance review.

First RESEARCH pass (at most25 minutes; at most3 accumulated passes): reconstruct the CKS2.1-to-3.2 reduction and formulate a composition/potential lemma that simultaneously preserves paired fractional terminal mass, bounds cumulative loss by log^(1+o(1)) k, and pays for local grouping PLUS global flow within edge capacity1. Explicitly test whether the current rational-weight theorem replaces k by n or introduces inverse-mass dependence. Seek a proof first, and use small rational LP instances to falsify a precisely stated interface if needed. The changed-mass interface is the unresolved kernel; a constant-congestion composition is insufficient. Diagnostic counterexamples only redirect this program. No new proof search or exhaustive diagnostic was performed during TRIAGE.

A full resolution would improve a recent explicit approximation-algorithm conjecture, a plausible substantive payoff. This is admission evidence, not a STOC-readiness assessment. Unresolved or partial work receives no manuscript/PDF. Only complete substantively innovative original-scope resolution may become a resolution-paper candidate; actual fresh mathematical and venue-level review remain required.

## Research-pass-1 refinement of the sufficient interface

See evidence/research-1-interface.md. A support-normalized integer domination
reduction for the BJS integral-weight theorem removes n and minimum-mass
dependence from a fixed-weight decomposition. Deleting its cut edges from a
fixed initial path flow retains paired masses with the stated objective bound,
without recomputing the maximum-throughput LP. The unresolved sufficient kernel
is now NR: nonuniform paired congestion-1 rounding from all-demand flow expansion,
with the full CKS pseudocenter/tagging construction and explicit mass ownership.
No full original-scope resolution or innovation qualification is asserted.

## Research-pass-2 full-target proposal (pending fresh review)

The original target and quantifiers above are unchanged. The new proof proposal
in evidence/research-2-uniform-copy-resolution.md bypasses nonuniform NR, which
remains unproved, by retaining uniform epsilon path copies and old unit terminal
occurrence bridges. One BJS integral-node-weight decomposition and the corrected
prior CKS uniform congestion-1 rounding then give the complete original-scope
log^(1+o(1)) k algorithm. A small-k exact branch controls the n-versus-k issue.
The randomized convention is strict polynomial time and bits, always feasible
output, and at least 3/4 probability of the approximation guarantee. The
researcher proposes kind=resolution-paper and original_status=proved in
claim.json; this requests a fresh correctness/novelty/significance review and
is not acceptance or a venue-readiness judgment. No PDF/manuscript is created.
Current primary comparisons, prior-tool credits and access limitations are
recorded in evidence/research-2-literature.md. Earlier unresolved statements
remain preserved as the history of the previous research stage.
