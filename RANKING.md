> Historical comparison of an earlier snapshot. For current manuscript categories and versions, use [the unified index](README.md). This older comparison neither ranks every current topic nor determines submission_ready status.

# Comparative STOC prospects and resolved-problem size

[English](RANKING.md) · [中文](RANKING.zh-CN.md)

The four priorities for external review and a possible STOC attempt are **c015-imagebound, c017-wheeler, c009-cycle2, c002-coverage**. This is a relative assessment of the current pool; none can responsibly be called a safe acceptance. Other strong topic matches are stoc3, stoc4, stoc1 and stoc5, but topic fit does not establish novelty.

The ordering concerns achieved results, not ambitious original prompts, titles, page count or code volume. There are no calibration data for credible numerical acceptance percentages; prospects are ordinal editorial judgments. Adjacent ranks within a tier are weak distinctions. This comparison reads manuscripts and existing source/review records and replays the new artifacts; it is not a new complete mathematical audit or external peer review.

## Relative STOC prospects, highest first

| Rank | Manuscript | Problem-size rank | Relative tier | Reason and risk |
|---:|---|---:|---|---|
| 1 | [c015-imagebound: Automata mortality hierarchy](papers/c015-imagebound/paper.pdf) | 2 | Priority review | Matches the n^(k+1) exponent for every fixed k≥2, with binary strong connectivity; the queue/clock invariant is a substantive construction. Its remaining risk is the specialized extremal-automata scope. |
| 2 | [c017-wheeler: Wheeler transducer decision problems](papers/c017-wheeler/paper.pdf) | 1 | Priority review | Decides the full current membership model and constructive realizability, including erasure and unbounded finite partitions. The O(S^13) algorithm needs a broad, independently checked explanation of the new SCC criterion. |
| 3 | [c009-cycle2: Global Sidorenko inequality for a cycle family](papers/c009-cycle2/paper.pdf) | 4 | Second priority | Resolves the full infinite family globally, beyond the source local question, with equality and optimal-exponent forcing. Strong mathematical technique, but broader algorithmic impact is less immediate. |
| 4 | [c002-coverage: Size-independent nonlinear discrepancy](papers/c002-coverage/paper.pdf) | 3 | Second priority | Removes item-count dependence for the whole sparse-coverage model via a constructive nonlinear-to-linear bridge. The O(t³k³) parameter dependence is coarse and the general influence-sparse problem remains open. |
| 5 | [stoc3: Quadratic structural-subtyping barrier](conversations/stoc3/paper.pdf) | 5 | Low, novelty-dependent | Fine-grained complexity and representation sensitivity fit STOC very well. The source itself credits the OV automata hardness; the added semantic encoding must justify an independent main-conference contribution. |
| 6 | [stoc4: Dynamic interprocedural dataflow](conversations/stoc4/paper.pdf) | 8 | Low, novelty-dependent | Dynamic algorithms and the path-procedure OMv obstruction are natural. Positive bounds charge affected circuit gates and restrict calls/decompositions; the general target is not fully resolved and earlier RSM update machinery is close. |
| 7 | [stoc1: Grammar-constrained decoding](conversations/stoc1/paper.pdf) | 10 | Low, novelty-dependent | A timely theoretical problem with careful parameter accounting. General LR(1) acceleration is missing, stack annotations are classical, and novelty against online NFA simulation is unresolved. |
| 8 | [coverage-sparse: Graph-constrained correlation gaps](papers/coverage-sparse/paper.pdf) | 6 | Low | An exact graph-class hierarchy and clean collision inequality, but much of the construction/constants comes from prior work. The new technique is short and significance remains the main obstacle. |
| 9 | [stoc5: Octagon/APSP exponent equivalence](conversations/stoc5/paper.pdf) | 9 | Low | Very good fine-grained topic fit, but reductions and classical normalization carry most of the result. The imported October 2026 APSP exponents are other authors' reported algorithms, not a new breakthrough of this manuscript. |
| 10 | [stoc2: Marked-palindrome language edit distance](conversations/stoc2/paper.pdf) | 11 | Low | A scoped matching upper/lower picture with witnesses, but limited to a narrow deterministic grammar subclass and built around Landau–Vishkin/LCE ideas. The general LR(1) target remains open. |
| 11 | [advice-matching: Advice/robustness on degree-two matching](papers/advice-matching/paper.pdf) | 7 | Low | Exact consistency–robustness frontiers have clear online-algorithm meaning. Degree-two and cycle restrictions make the advance small compared with general matching questions. |
| 12 | [c012-upcycles: A three-wildcard universal partial cycle](papers/c012-upcycles/paper.pdf) | 12 | Very low for current STOC package | A complete, exactly checkable existence witness to the stated question. The present contribution is one finite 512-cycle rather than a general construction, algorithmic framework or broad classification. |
| 13 | [curvature-noise: Curvature under persistent noise](papers/curvature-noise/paper.pdf) | 13 | Very low; partial original scope | Matching asymptotics in a specified sparse-cardinality regime, not the unrestricted original. Limited parameter regime and significance dominate the risk. |
| 14 | [robust-stopping: Certified robust ski-rental optimization](papers/robust-stopping/paper.pdf) | 14 | Very low; partial original scope | Exact certificates and reproducibility are useful, but the broader target is unresolved and numerical-b polynomial time is not polynomial in log b. No major new online principle is established. |
| 15 | [privacy-interpolation: Privacy-constrained probability paths](papers/privacy-interpolation/paper.pdf) | 15 | Very low; partial original scope | Precise three-outcome excursion formulas, but the general problem is unresolved and the present result is the most specialized of this pool. |

## Size of the actual resolved problem, highest first

1. [c017-wheeler: Wheeler transducer decision problems](papers/c017-wheeler/paper.pdf)
2. [c015-imagebound: Automata mortality hierarchy](papers/c015-imagebound/paper.pdf)
3. [c002-coverage: Size-independent nonlinear discrepancy](papers/c002-coverage/paper.pdf)
4. [c009-cycle2: Global Sidorenko inequality for a cycle family](papers/c009-cycle2/paper.pdf)
5. [stoc3: Quadratic structural-subtyping barrier](conversations/stoc3/paper.pdf)
6. [coverage-sparse: Graph-constrained correlation gaps](papers/coverage-sparse/paper.pdf)
7. [advice-matching: Advice/robustness on degree-two matching](papers/advice-matching/paper.pdf)
8. [stoc4: Dynamic interprocedural dataflow](conversations/stoc4/paper.pdf)
9. [stoc5: Octagon/APSP exponent equivalence](conversations/stoc5/paper.pdf)
10. [stoc1: Grammar-constrained decoding](conversations/stoc1/paper.pdf)
11. [stoc2: Marked-palindrome language edit distance](conversations/stoc2/paper.pdf)
12. [c012-upcycles: A three-wildcard universal partial cycle](papers/c012-upcycles/paper.pdf)
13. [curvature-noise: Curvature under persistent noise](papers/curvature-noise/paper.pdf)
14. [robust-stopping: Certified robust ski-rental optimization](papers/robust-stopping/paper.pdf)
15. [privacy-interpolation: Privacy-constrained probability paths](papers/privacy-interpolation/paper.pdf)

## Readiness and scope

stoc1–stoc5 are existing manuscripts from other conversations and retain their original PDF/source bytes and author lists. They have not passed this continuous project's full-original-resolution gate. stoc6–stoc8 contain templates only. Legacy partial results and method-obstruction notes are not relabeled as new full resolutions.

stoc2 currently uses an anonymous two-column format and needs review-format correction. stoc3 has18 pages and stoc5 has19: these exceed the earlier personal12-total-page preference, while the official submission has no total page cap. This synchronization does not edit the original papers.

The [official STOC2027 CFP](https://acm-stoc.org/stoc2027/stoc2027-cfp.html) calls for original theory contributions, verifiable full proofs and an accessible account of importance in the opening12 pages after the title page. Submissions are identified, single-column, and limited to five per author. Prioritize expert review of the first four; stoc3 is a fifth option only if its semantic transfer clears a serious independent-novelty review.

Missing systems benchmarks are not an automatic objection to a theory paper. Imported October2026 APSP/SSSP guarantees are reported prior algorithms, not a new APSP solution by stoc5; their complete external proofs were not re-audited here. Executable logs support only their stated finite scope.

Synchronization validation: all five new PDFs clean-build with matching normalized text; stoc2–stoc5 replay checks pass. Both stoc1 checking entrypoints depend on the Rust library and were not rerun because rustc was unavailable (exit127 retained). A missing compiler is not mathematical counterevidence.
