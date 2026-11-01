# User-requested revision after two referee reports

The latest user instruction is: “第一篇的审稿人意见共两个,请你参考并逐一修改后再进行下面的”. Finish this first paper's substantive revision before advancing the four additional papers. Retain the official downloaded ACM acmart template, the user-specified five-author list in requirements.md, non-anonymous STOC 2027 policy, and <=12 TOTAL PDF pages (cover and references included).

Both supplied reports say they found no mathematical error in the original theorem but criticize insufficient significance, missing foundational citations, weak motivation, repetitive scope disclaimers and sparse exposition. Their claims are review inputs to verify, not mathematical evidence or external peer-review certification. Do not use their favorable statements as proof. Do not invent a statement that the revised result meets STOC's acceptance standard.

## Reviewer 1: numbered actionable points to answer individually

R1.1 Novelty: the color resampling upper bound, alpha_k constant and Cartesian coverage family are known ingredients; the incremental content is the within-block collision bound. Explain that contribution precisely and make the obstacle concrete.
R1.2 Proof organization: collapse the four class equalities using B_k subset C_k and D_eq subset D_up_delta. Prove one upper-error finite bound and derive the equality bound by inclusion, instead of parallel redundant proofs. Define “normalized” explicitly (for this witness: f(empty)=0, f(V)=1, 0<=f<=1).
R1.3 Perturbations: state the delta_m=o(m) consequence; treat additive upper moment errors epsilon_m with bound alpha_k+(k-1)/(2k)*(1/m+m epsilon_m), so epsilon_m=o(1/m) suffices. Explain the absolute scale of multiplicative errors.
R1.4 Missing literature: verify and cite Agrawal--Ding--Saberi--Ye correlation gap, Calinescu--Chekuri--Pal--Vondrak submodular/matroid work, Ramachandra--Natarajan ORL 60 (2025), article 107255, and the 2026 five-element counterexample. Verify Udwani--Wajc arXiv:2610.16060 without treating indexing delay as nonexistence. Distinguish classical mutual-independence dimension constants from pairwise-independent bounds; do not repeat a review's conflation.
R1.5 Consequence: prove a nonasymptotic all-pairs/full t-wise corollary from the same witness. K_n imposes every within-block constraint; adding constraints lowers the optimized denominator. With k,m->infinity the ratio tends to e/(e-1), recovering the already known asymptotic statement with a short explicit bound. Credit Ramachandra 2026 for the prior theorem and family. Do not call the asymptotic theorem new.
R1.6 Significance: add meaningful fixed-graph structure or additive tolerance / algorithmic implication. Mandatory corrections include the additive-tolerance bound and exact finite matching example below. Consider further fixed-graph progress only if proved and independently reviewed. Do not pad pages or promise a general submodular extension. Describe graph-dependent refinements as open questions if unresolved.
R1.7 Motivation and narrative: lead with an O(n)-pair versus all-pairs moment-information question, illustrate whole-block selection and why within-block collisions constrain it. Probability constraints are not a statistical testing/sample-complexity theorem. Use a succinct positive contribution statement and discuss related work by logical relationship.
R1.8 Presentation: add a simple scientific construction/proof-roadmap figure (e.g. 3 disjoint 3-cliques, one transversal feature, and whole-block draw), plus an exact table for k=2,...,6 of alpha_k, its inverse and finite bound coefficient. Fix paragraph page breaks, remove arbitrary newpages except the required title-page boundary, and tidy URL line breaks.
R1.9 Style: delete search dates/process language and repetitive “not claimed” prose from the paper. Keep essential hypotheses in theorem statements and define the class-supremum scope once. Replace “Scope and assistance” with “Consequences and open questions” or similar. Compress the AI methodology to truthful 1--2 sentences at the end; the mandatory disclosure remains. Avoid exaggerated title claims and formulaic contrast sentences.

## Reviewer 2: numbered actionable points to answer individually

R2.1 Preserve the verified core proof, but make its sparse-moment obstacle and conceptual payoff clear before the full formal statement.
R2.2 Recompute the supplied finite LP observations independently: (k,m)=(2,2) 7/8, (2,3) 5/6, (3,2) 5/6, (3,3) 65/81 under equality; (3,3), upper model delta=1 is reported as approximately 0.901235. Numerical observations require exact certificates if included as exact values. Package scripts/inputs instead of claiming an invisible computation pipeline.
R2.3 Keep class supremum versus fixed graph, multiplicative versus additive error, and sufficient versus necessary edge count precise. State these positively and succinctly rather than repeating disclaimers.
R2.4 Add missing original 2025 framework and 2026 counterexample citations; compare the k-group resampling ingredient to the STOC 2025 two-group bound. Provide a concrete theory/optimization consequence beyond a general significance assertion.
R2.5 Reorder exposition: motivating moment-information question; main theorem with k=2 example and prior-work comparison; two complementary proof ingredients; rigorous proof; consequences/open questions.
R2.6 Check official format and actual rendered pages; use the official ACM template and correct five authors, single column/11pt/Letter/1-inch margins. Add a useful construction/roadmap figure, not a fictitious systems architecture.
R2.7 Reduce defensive language, remove search timestamps, state that the witness has k^m explicit features but is efficiently evaluable from block counts, and shorten accurate AI disclosure.
R2.8 Prove the exact finite k=2 witness formula for all m>=1 and delta>=0:
 f_up=3/4+(1/4) min{1,(1+delta)/m};
 f_eq=3/4+1/(4m), ratio=4m/(3m+1).
 Handle m=1 separately. This is the specified witness, not every matching with arbitrary marginals/coverage function. Add its simple two-type coupling proof.
R2.9 State delta_m=o(m) convergence and the additive analogue with precise quantifiers. Do not claim arbitrary growing errors preserve the limit.
R2.10 Author metadata: replace previous default everywhere in the paper and current deliverables with the exact five-author list; no ORCID or personal verification claim is invented. Video/HotCRP tasks are outside this local-file request.

## Required revision artifacts

1. A fresh research proof dossier and revised claim covering any added mathematical statement, then a fresh mathematical referee; prior mathematical acceptance does not certify added claims.
2. Revised paper <=12 total pages in official acmart manuscript format, with five specified authors, complete proofs, checked literature, figure, table and concise mandatory AI disclosure.
3. A separate Markdown point-by-point response containing every ID R1.1--R1.9 and R2.1--R2.10. For each, give the actual change and section/theorem reference, or a specific reason for a partial/deferred response. Do not claim an unresolved general fixed-graph characterization or general submodular theorem is solved.
4. New citation/build/every-page visual audits and release gate. No external submission. Preserve historical files as noncurrent evidence, and replace current deliverables only after the revised release passes.
