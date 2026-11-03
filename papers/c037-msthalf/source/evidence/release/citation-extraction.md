# Fixed extraction — pass 1

Job: c037-msthalf-release-aff0d39d4223. Extracted from the complete manuscript before claim-by-claim verification. Definitions, hypotheticals, methodology and acknowledgments excluded as instructed. Mathematical assertions are grouped by their complete lemma/proof paragraph and verified for transcription/scope against the accepted packet; this is not a new mathematical referee.

The user requested one bounded autonomous RELEASE job with JSON-only return and designated this skill advisory; interactive extraction confirmation is therefore omitted under that explicit workflow. No claim is added during pass 2.

[C01] | For every fixed 0<=p<1/2 the explicit finite no-query procedure has expected true cost at most C_p max(1,ln n) MST(d), for all n>=2 and all metrics and post-mask adversaries. | Existence | Abstract; Theorem 1.1
[C02] | Anand et al. prove O_p(log n) under arbitrary replacements for p<1/4. | Attribution + Comparative | Abstract; Context paragraph
[C03] | Anand et al. prove a linear obstruction for p>=1/2. | Attribution | Abstract; Context; Boundary
[C04] | Bateni et al. study the strong/weak distance-oracle model. | Attribution | Context paragraph 1
[C05] | Bateni et al. Theorem 4 gives no-strong-query O(sqrt(log n)) MST approximation assuming metric weak observations. | Attribution | Context paragraph 1
[C06] | Bateni et al. Appendix F.2.2 Theorem 32 gives a logarithmic obstruction for arbitrary corruptions at p=1/3. | Attribution | Context paragraph 1
[C07] | Anand et al. Theorems 1.4/5.3 are the closest checked arbitrary-corruption upper bound; the present result closes their quarter-to-half gap, relative to cited versions. | Attribution + Comparative | Context paragraph 2
[C08] | At p=1/3 the present upper bound has the order of the cited logarithmic obstruction. | Comparative | Context paragraph 2
[C09] | Repair benchmark, certificate minimization and preorder output build on Anand et al. Lemma 3.2 and Section 5. | Attribution | Context paragraph 3; Section 3
[C10] | The common-good-neighbor argument of Anand et al. Lemma 5.6 needs a good-pair fraction exceeding one half. | Attribution | Context paragraph 3
[C11] | Positive density in every large disjoint rectangle plus order domination implies sum D_i <= (320r/eta)W+(8r/eta)M. | Existence | Lemma 2.1
[C12] | Hereditary rectangle density gives a star with r leaves in any 2 ceil(2r/eta) vertex set. | Existence | Lemma 2.1 proof, first paragraph
[C13] | Cheap path edges sum to at most 64W; each expensive-edge interval has length D_i/32 with both endpoints within D_i/32 of each point it covers. | Existence | Lemma 2.1 proof
[C14] | A matching of short and long overlapping edges creates an empty r-by-r rectangle, so overlap is at most 8r/eta. | Existence | Lemma 2.1 proof
[C15] | Integrating overlap controls all scales with D_max<=M, including the vacuous 2r>n case. | Existence | Lemma 2.1 final paragraphs
[C16] | The credited repair has failure <=(n-1) beta^(n-2) and unconditional E[X]<=2(1+4/alpha)M, alpha=(1-p)^2. | Existence + Attribution | Lemma 3.1
[C17] | Fixed-p rational parameters and finite tree/rectangle enumeration give an observable deterministic algorithm, even with zeros or vacuous rectangles. | Existence | Section 4
[C18] | The uniform mask event has failure at most n^-12, uniformly over subsequent adversarial values and selected tree. | Existence | Equation (9), Section 5
[C19] | On E intersect F the repair tree qualifies and minimum observed cost is at most X; analysis graph density is at least eta. | Existence | Section 5
[C20] | The selected preorder has W<=2X and H-edge domination, yielding Y<=(320r/eta)(2X+M). | Existence | Section 5
[C21] | The good-event expectation is at most (320r/eta)(2B_p+1)M. | Existence | Equation (10)
[C22] | Every output has true cost <=(n-1)M, giving complementary expectation <=(1+2/alpha^3)M. | Existence | Equation (11)
[C23] | The explicit C_p is finite for fixed p<1/2, independent of aspect ratio and replacement magnitudes; averaging covers randomized adversaries. | Existence | Section 5 final paragraphs
[C24] | The standard positive-distance two-cluster regularization preserves Anand et al. half-boundary obstruction, with expected crossing count 2ab/n and optimum 1+(n-2)delta. | Attribution + Existence | Boundary paragraph
[C25] | Taking delta=n^-2 yields Omega(n) obstruction. | Existence | Boundary paragraph
[C26] | Exact checks covered 160 integer metrics at n=8,12,16,24 including nonuniform weights and zeros. | Statistic | Computation paragraph
[C27] | Exact checks covered 2,802,752 disjoint rectangles. | Statistic | Computation paragraph
[C28] | Exhaustive checks covered 33,866 pair masks for n=2,...,6 and p in {0,1/3,2/5,49/100}. | Statistic | Computation paragraph
[C29] | A separate model context reconstructed the proof and recomputed finite checks using a different implementation. | Attribution | Computation paragraph
[C30] | No polynomial/quasi-polynomial runtime or further application is established; constants deteriorate near one half. | Existence | Limitations
[C31] | The Anand reference has the five listed authors, title, 2026 arXiv 2610.40594v1, 29 October, DOI 10.48550/arXiv.2610.40594. | Attribution + Temporal | References [1]
[C32] | The Bateni reference has the four listed authors, title, COLT 2024, PMLR 247, pages 498-550, editors Agrawal and Roth. | Attribution + Temporal | References [2]
