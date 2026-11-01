# Fresh referee: focused primary-source comparison

Job: `coverage-sparse-referee-20ee9a6fefc3`.
Frozen evidence digest: `639fb67b280db040c9a3c5059288d96a35e8cb02d493e698aaf573087cfca4e8`.

This review inspected the listed local primary sources and checked the relevant
arXiv texts online. It did not inspect earlier audits, owner checkpoint/state,
historical verdicts, job transcripts, or historical drafts. The descriptions
below concern source statements and their relationship to the frozen candidate;
they do not certify all other results in those papers.

1. **Ramachandra, arXiv:2609.02659v1.** Theorem 2 and Sections 4.1--4.2
   explicitly use the Cartesian family, identical marginals, uniform whole-block
   numerator law, and normalized product coverage formula. They state the known
   asymptotic all-pairs gap and its t-wise consequence. These are correctly
   credited prior results. The displayed reduced dual, equations (14)--(15), has
   separate within-block and cross-block coefficients. Its asymptotic proof uses
   a nonzero cross-block coefficient in equation (24). This does not supply the
   candidate's fixed block-size, within-block-only certificate or its finite
   nonnegative-error bound. Deleting constraints increases a maximized
   denominator, so the prior all-pairs extremal theorem alone cannot establish
   the sparse theorem. The candidate's finite proof is self-contained and does
   not depend on the source's asymptotic reduction or its separate n=4 proof.
   [Primary text](https://arxiv.org/html/2609.02659v1).

2. **Dütting et al., arXiv:2412.02492v1.** Section 3.2, Coverage Functions,
   compares jointly sampled two-group coverage with independently sampled
   coverage and derives the 3/4 factor from two hit probabilities and the union
   bound. This is the two-group ingredient of the color conversion. The
   candidate's k-group extension is elementary and should be presented as such;
   the sparse extremality certificate is the distinct step. The listed
   publisher-deposited Crossref record confirms STOC 2025, pages 1406--1417,
   DOI 10.1145/3717823.3718131.
   [Primary text](https://arxiv.org/html/2412.02492v1).

3. **Ramachandra--Natarajan 2025.** Section 1.1 defines F as the mutually
   independent expectation and places 27/19 at n=3 in that model. Definition 2
   introduces the pairwise-optimized extension; Theorem 5 gives its sharp 4/3
   bound for n=3. The frozen revision's correction is right. Its color parameter
   k is not the source's variable count n. The listed Crossref record confirms
   Operations Research Letters 60, article 107255 and DOI
   10.1016/j.orl.2025.107255.
   [Primary text](https://arxiv.org/html/2209.08563v3).

4. **Ramachandra--Natarajan 2026.** Section 2 displays a five-element coverage
   example with numerator 4 and pairwise denominator bounded above by 479/160,
   yielding 640/479 > 4/3. This is consistent with the revision's attribution.
   It concerns all-pairs constraints and does not contradict a bipartite tested
   graph bound. Its full certificate is background, not a dependency of the
   candidate's proof.
   [Primary text](https://arxiv.org/html/2606.19663v1).

5. **Udwani--Wajc 2026.** The listed arXiv record exists and identifies both
   authors, arXiv:2610.16060, and the comment “In FOCS 2026.” In the linked
   original text, Definition 3.1 and Lemma 3.4 give the probability-coverage
   interpretation and identical block-count polynomial; Corollary 3.6 and the
   subsequent explanation use the classical alpha_k constant. Their optimization
   model is online welfare, not the prescribed tested-pair moment polytope. This
   supports attribution of the family and constant, without supplying a
   bibliographic basis for invented proceedings details.
   [Primary record](https://arxiv.org/abs/2610.16060),
   [primary text](https://arxiv.org/html/2610.16060v1).

6. **Agrawal--Ding--Saberi--Ye 2012.** The listed PDF's Theorem 2 and
   Section 3.1 give the classical mutual-independence correlation-gap context
   and its submodular specialization. The listed Crossref record confirms
   Operations Research 60(1), 150--162, DOI 10.1287/opre.1110.1011. Its role here
   is foundational; the finite hierarchy sandwich can instead be derived
   directly from product feasibility, as the dossier does.

7. **Calinescu--Chekuri--Pál--Vondrák 2011.** The listed PDF's Theorem 1.1
   concerns the (1-1/e) approximation for a monotone submodular function under a
   matroid constraint, using continuous greedy and pipage rounding. Its
   multilinear-extension context is appropriate; it is a different feasibility
   model from tested pair moments. The listed Crossref record confirms SIAM
   Journal on Computing 40(6), 1740--1766, DOI 10.1137/080733991.

Additional live queries combined coverage/correlation gap with chromatic,
colorable, sparse pairwise independence, and matching moments. They returned no
additional primary theorem establishing the candidate's complete sparse
fixed-k hierarchy or exact matching-error formulas. Irrelevant and secondary
search results were not used as mathematical evidence. This is a limited
source comparison, not proof of priority or an exhaustive novelty claim.

The credible contribution is the finite collision certificate that works after
all cross-block pair tests are removed, yielding sharp fixed-k graph-class
values and explicit aggregate error control. The exact matching coupling
identifies a sharp perturbation threshold for that family. The finite t-wise
sandwich is a useful consequence and new short derivation of an already known
limit; it is not an independent claim to that limit. The sampler conversion
explains an optimization use conditional on access to an input law. This
supports the bounded contribution statement, with no conclusion about venue
acceptance.
