# TRIAGE evidence and decision

Job: c042-strongrsp-triage-931c32b4b93a. Date: 2026-11-03 UTC.
Actual dispatch: 03:19:38. First real clock read: 03:21:42.
Main source/model validation and elementary check completed by 03:23:26, before the 03:23:37.999914 main-test deadline. Subsequent work only records and validates artifacts.

## Inspected primary evidence

- [Current Ashvinkumar record](https://arxiv.org/abs/2610.18337): retrieved live; identifies v2, revised 29 October 2026 at 16:10:41 UTC. [Primary v2 HTML](https://arxiv.org/html/2610.18337v2), Theorems 1--2 and following paragraph, HTML lines 69--79 / printed p.3, was read live and compared with `intake/primary/2610.18337.txt` lines 107--139. The all-target numerical-aspect dependence and explicit open paragraph are present. Section 4 and Section 6 were inspected at the level needed to identify static DP and deterministic witness interfaces, not fully audited. The version-specific abstract URL returned a cache miss; the current abstract and version-specific primary HTML succeeded. No scientific conclusion is drawn from the failed fetch.
- [ABK primary HTML](https://arxiv.org/html/2410.17179v1), open-problem paragraph lines 1222--1224 and Lemma C.1 lines 1300--1306, together with `intake/primary/2410.17179.txt` printed pp.42,46 and Appendix D: confirms the all-target/single-target distinction and zero-length preprocessing. The [current abstract](https://arxiv.org/abs/2410.17179) was also refreshed.
- [Gorkiewicz--Karczmarz](https://arxiv.org/abs/2502.10348): current primary abstract refreshed; supplied primary text Theorem 1.3 and Section 6 / Algorithm 4 / Lemma 6.1 were read. Its additive SSSP suffix argument does not establish a generalized stochastic boundary solver. The preprint theorem numbering differs from the intake's reference to the conference Theorem 3; no equivalence beyond the inspected preprint statement is assumed here.
- [Liu](https://arxiv.org/abs/2506.19207): current primary abstract refreshed and supplied text Theorem 1 read. Its m^(1+o(1)) log W bound concerns online ordinary shortest paths, not this target.

Live search strings included `"restricted shortest paths" "strongly polynomial" "all" 2026 Ashvinkumar`, `site.arxiv.org "restricted shortest paths" "strongly polynomial" "2026"`, and `site.arxiv.org "restricted shortest paths" "aspect ratio"`. No inspected primary result from this bounded refresh resolves the full target. Third-party summaries were treated only as pointers; they are not status evidence. This search is not exhaustive and certifies no priority or absence of future equivalent work.

## Cheapest discriminating check

`evidence/triage-common-scale-check.json` records an exact Fraction-arithmetic check of a three-vertex star: edges s->u and s->v have respective lengths 1 and 16 and both cost 1; C=1. The two feasible optima are 1 and 16. A common gamma placing both in [gamma,3 gamma] would require 16/3<=gamma<=1, impossible. This confirms a stated limitation of the known per-target bottleneck reduction. It is elementary prior-compatible evidence, not new mathematical value, not a lower bound against batching, and not a disproof of algorithm existence. No research proof search or exhaustive experiment was performed.

## Comparison, payoff, obstacles

`intake/screening.md` reports a historical registry comparison; this worker did not rerun or certify its 566-record scan. Only local intake evidence was read. Mathematically this target has two edge resources and all-target bicriteria guarantees, whereas the described exhausted c041 target is unconstrained exact ordinary SSSP. No c041 counters/files were changed or reused as new research passes.

The target is precise and has plausible substantial payoff: removing arbitrary numerical-scale dependence at an explicit all-target directed constrained-path frontier, potentially through a reusable offline method. Its difficulty is concrete. The ordinary-SSSP offline theorem does not provide the required stochastic active-boundary oracle or aggregate work proof. Correct nontermination, arbitrary boundary labels, zero resources, finite-cost probability evaluation, edge-event coverage and the frozen witness bound all remain open obligations. Multigraph/query accounting must not be hidden behind m<=n^2. No current innovation or STOC-quality verdict exists.

## Decision and one next test

Advance to one bounded RESEARCH pass, within the unchanged maximum three accumulated 25-minute passes (currently 0 consumed). No candidate and no manuscript/PDF.

Test the actual two-clock DP inactive-boundary contract: for regularized values X=V+rho, establish correct failure/properness semantics, first-hit multiplicative comparison under arbitrary valid inactive upper labels, tick-monotone closure and a static active-state/incident-transition work bound; attack the same contract with tiny exact rational systems containing closed p00=1 classes, small exit probabilities and multiple boundary rewards. A proof or a concrete failure changes a named core method claim. It does not resolve the original question by itself.
