# Primary-source and equivalence screen for the proposed bound

Research job `curvature-noise-research-5a09759394ef`, inspected 2026-10-31
Asia/Shanghai. This is a bounded comparison, not a priority certificate or
fresh mathematical referee report. No equivalent sharp true-objective factor
was found in the inspected statements. The incremental contribution remains
subject to a referee's correctness and significance decision.

## Closest statements actually inspected

1. **Horel--Singer, NIPS 2016**, [official proceedings](https://proceedings.neurips.cc/paper_files/paper/2016/hash/81c8727c62e800be708dbf37c4695dff-Abstract.html),
   [original PDF](https://proceedings.neurips.cc/paper_files/paper/2016/file/81c8727c62e800be708dbf37c4695dff-Paper.pdf),
   [later deposited full text](https://arxiv.org/html/2411.10949v1).
   Re-read original extracted pp.1--6 and the later version's Section 2.1,
   equation (3), Theorem 3, and Appendix D, Lemma 12 / Proposition 8 proof.
   The optimized objective is F, the approximate function. Proposition 8's
   bound is (1-K)rho^2 for F. Its algorithm queries singletons and selects
   the largest k. Direct analysis against true f yields rho(1-K); this
   normalization and the elementary K/k refinement are credited baselines.
   Equation (3) already uses a modular hidden-set term plus a capped rank,
   with a common transcript and exceptional revealing queries. Theorem 3
   takes k=h=n^(1-beta/2), not sparse k=n^alpha with alpha<1/2, and does
   not assert a fixed-curvature calibrated lower bound. Neither the family
   pattern nor the indistinguishability method is proposed as new.

2. **Sviridenko--Vondrak--Ward**, [arXiv:1311.4728v3](https://arxiv.org/html/1311.4728v3),
   Sections 6.1 and 7. Re-read Theorems 6.1 and 7.1 and their proofs.
   Theorem 6.1 gives 1-K/exp(1)-O(tau), with high probability, from an
   exact value oracle under a matroid. Theorem 7.1 rules out a fixed
   additive improvement using polynomially many exact evaluations. Its
   proof explicitly adds ((1-K)/K)|S|p to tune curvature. Thus modular
   curvature tuning is prior work. These exact-oracle results are the
   noiseless comparison and do not state the noisy product factor.

3. **Hassidim--Singer, COLT 2017**, [primary PDF](https://proceedings.mlr.press/v65/hassidim17a/hassidim17a.pdf).
   Inspected Theorem 8 and Section 5, printed pp.17--19. The adversarial
   oracle impossibility already covers randomized algorithms and fixed
   error epsilon. Its displayed parameter choice is k=n^(1/2+delta),
   and it does not calibrate an exact curvature below one. Its switch
   oracle and hidden-instance indistinguishability are related prior methods.
   General adversarial-noise hardness is not this candidate's contribution.

4. **Bhawalkar--Cai--Feng--Liaw--Lin**, [arXiv:2510.21128](https://arxiv.org/html/2510.21128),
   Section 2, noisy value oracle. The stated contract requires persistence,
   unbiasedness and independence across distinct sets, with sub-exponential
   multipliers. The proposed adversarial g_H is only a fixed bounded-error
   map and need not satisfy unbiasedness or independence. Thus the cited
   stochastic meta-algorithm cannot be applied to these instances.

5. **Aggarwal**, [arXiv:2608.12134v2](https://arxiv.org/html/2608.12134v2),
   Section 5.6, Theorem 5.14. The primary theorem has a persistent controlled
   oracle with additive error xi, normalized range [0,1], and monotone
   objective guarantee (1-1/exp(1)-tau)OPT-8k xi. Multiplicative errors can
   be upper bounded additively by epsilon times a global range bound, but
   this loses a term proportional to k epsilon and does not yield a positive
   improvement in the admitted epsilon*k divergence regime. The theorem
   does not state the joint curvature lower bound; its internal correctness
   is not being audited here.

6. **Huang--Wang--Yang--Zhou**, [arXiv:2210.11992v1](https://arxiv.org/html/2210.11992),
   Section 2, Definition 2.4 and Problem 2.6. The multipliers are drawn
   independently and identically from a distribution, with additional
   distributional hypotheses. Its near 1-1/exp(1) cardinality guarantee
   addresses that model. Section 1.2 itself distinguishes arbitrary
   adversarial errors from the i.i.d. model used in the paper.

7. **Roughgarden--Talgam-Cohen--Vondrak**, [arXiv:1608.02402 PDF](https://arxiv.org/pdf/1608.02402),
   Section 4.1, Observation 3; Section 4.2, Theorem 4; Section 3,
   Proposition 5. A valuation of curvature K and approximate diminishing
   returns is pointwise close to linear. Their positive matroid result
   assumes approximate diminishing returns of the directly queried
   valuation. The hidden true f is submodular here, but the noisy queried g
   is not promised approximate diminishing returns. Their demand-query /
   welfare lower bound likewise does not state this cardinality-constrained
   true-f approximation factor. The author's Stanford PDF endpoint timed
   out; the arXiv PDF was successfully inspected instead.

8. **Chen--Kuhnle**, [arXiv:2605.07902v1](https://arxiv.org/html/2605.07902v1).
   Inspected the primary abstract and text-search occurrences of noise.
   This concerns extending curvature to negative / non-monotone objectives;
   the noise occurrences found concern statistical example objectives.
   No adversarial value-oracle theorem was located by this limited screen.
   The full proof collection was not audited.

## Algebraic comparison with the known curvature shift

For the normalized capped-rank family

    U_H(S)=(1-K)|S|+K[|S intersect H|+min(|S outside H|,r)],

all singletons equal 1, curvature is exactly K when n-k>r, and OPT=k.
Every k-set has U_H value at least (1-K)k. Thus this PARTICULAR uniform
modular shift cannot witness an upper bound below 1-K, however its value
oracle is corrupted. This is an algebraic limitation of that specified
family, not a no-go theorem for all curvature reductions.

For the candidate family, good singletons are 1 and bad singletons rho;
their noise intervals touch. Bad full-set marginals are rho(1-K), so the
curvature remains exactly K while the residual baseline is rho(1-K)k.
This extra calibration is what supplies the fixed-epsilon product factor.
For epsilon bounded away from zero and one, the difference from 1-K is
a fixed constant when K<1. For epsilon->0, only the limiting 1-K barrier
survives. The exact finite theorem also keeps the query leakage and output
terms explicit, permits all query sizes, and handles fixed oracles with
private-seed expectations. The proposed result is a sharpened parameter
statement using known methods, not a new algorithm or hardness paradigm.

## Access limits and search coverage

The adjacent **Gong--Liu--Geng--Fang** paper,
[DOI 10.1007/s10878-023-01026-5](https://link.springer.com/article/10.1007/s10878-023-01026-5),
was checked at the primary publisher page. The abstract describes three
deterministic bicriteria algorithms for submodular-minus-modular objectives
under multiplicative noise, and no sharp curvature lower bound. Full theorem
text was not available in that page; exact-title and author/DOI searches did
not locate an accessible primary full text. This is an unresolved comparison
limitation, not evidence that the reference or any theorem is absent. No
claim about its exact guarantees or extra oracle information is made.

Searches included combinations of submodular, curvature, bounded curvature,
persistent, adversarial, multiplicative, approximately submodular, erroneous
oracle, lower bound, Horel, and close to linear, plus the adjacent exact
title and DOI. Search snippets and third-party summaries served only to find
primary sources. No secondary summary is used as mathematical evidence.
The screen is finite and may miss a differently phrased equivalent theorem.

## Candidate decision

The proof and finite checks support sending a **result-note candidate** to a
fresh referee with exact scope restricted to `evidence/research-proof.md`,
Sections 1--4. The mathematical payoff is a matching factor for fixed
curvature below one, sparse growing cardinality and epsilon*k->infinity,
including fixed noise and vanishing noise. The full original remains
unresolved. The referee must challenge correctness AND whether this
calibration/parameter conclusion is a substantive new bound beyond the
credited ingredients. No manuscript, PDF, accepted audit or priority claim
has been created by this research pass.
