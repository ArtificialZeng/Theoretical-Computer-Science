# Precise original problem

Immutable input: `source.md`, SHA-256 d45cd6730fe3f8685cb796b9d75ebe8e7926c1584021d045a282021749e45128. This is a newly inferred threshold question, not an author-stated conjecture. No scope correction is proposed.

Let X=[n], n>=2. A metric d has finite real entries, d(u,v)=d(v,u)>0 for u!=v, d(u,u)=0, and satisfies the triangle inequality. A spanning tree has vertex set X and n-1 edges. Define c_d(T)=sum_{uv in E(T)}d(u,v) and MST(d)=min_T c_d(T).

For each fixed real p in [0,1/2), independently put each unordered pair into S with probability p. After seeing all of d and S, an adversary chooses arbitrary finite replacement values on S. The symmetric observation matrix y equals d outside S and those replacements on S. The adversary need not be oblivious and y need not be a metric. Negative observations may be clipped to zero: unmarked metric entries are unaffected and clipped observations are still admissible replacements.

The question is whether

    for every fixed p<1/2 there exist an explicit finite procedure A_p
    and a finite constant C_p such that for every n>=2, every metric d,
    and every admissible adversary,
    E[c_d(A_p(y,n,p))] <= C_p max(1,log n) MST(d).

A_p receives no true-distance oracle or mask. Its private randomness is independent of the marking. The expectation is over these random choices; the guarantee must hold uniformly over adversarial replacement rules (and hence their mixtures). C_p may depend on p, not n, aspect ratio, metric or adversary. Computational efficiency is not requested. Distances are interpreted in the same exact-arithmetic mathematical model as the source; no new bit-complexity restriction is imposed.

A full negative resolution must negate these quantifiers: at one fixed p<1/2, every permitted A and every finite C must fail on some n, metric and admissible adversary. A failed reconstruction certificate, a finite bad example for one algorithm, or hardness of polynomial computation is insufficient. A positive proof only for p<1/4 or a restricted metric family is also insufficient.

# Nearest verified prior and current status

Anand, Gupta, Jayaram, Lee and Vakilian, *Approximating Minimum Spanning Trees in Metrics under Semi-Random Corruptions*, arXiv:2610.40594v1 (29 October 2026), Definitions 2.1-2.3 and Theorems 1.4-1.5 match the mask/adversary/true-cost model: an O_p(log n) bound for p<1/4 and an n/4 lower bound for p>=1/2. The current arXiv abstract page inspected on 2 November 2026 lists only v1. No equivalent full-gap resolution was identified in the bounded searches recorded in evidence/triage-literature.md. Thus status is open-supported as an inferred gap, not certified priority or an explicit author conjecture.

Proposed delta: resolve the whole interval below one half with a robust metric/tree method, or a full information-theoretic lower bound below one half. This would determine the general-corruption threshold and is plausibly substantive. No result or venue-quality acceptance has occurred.

# First research test and obstacles

Lemma 5.6's charging argument uses good pairs that are simultaneously uncorrupted and dominating. Its union bound gives bad-pair density at most 2p+2epsilon; a common-neighbor charging contradiction needs this below 1/2. This explains the quarter threshold of that route, without proving a general obstruction.

Test a replacement certificate using agreement on large disjoint rectangles A x B, rather than induced-set density alone. For epsilon=(1/2-p)/4, ask a candidate metric rho to disagree with y on at most (p+epsilon)|A||B| pairs whenever |A||B| >= K_p(|A|+|B|)log n. First derive the uniform mask event by a union bound; then test the deterministic claim that a minimum-MST such candidate, with an explicitly defined tree extraction/shortcut, gives an O_p(log n) true-cost bound relative to MST(d). This is a proposed route, not an established algorithm or lemma.

A bounded falsification stage should examine 2-6 cluster metrics with symbolic intercluster scale M, unequal cluster sizes, p=1/3, 2/5, 49/100, and adversarial observation patterns; use exact metric inequalities and leading powers of M to find a candidate/extraction failure. Fix the candidate tie rule in any claimed algorithm. Surviving these tests would require a general proof, data-dependent uniformity, feasibility/fallback control and conversion to expectation. Small sides omitted by the rectangle threshold and arbitrary aspect ratios are the central unresolved kernel. Failures test this route only and must not be called a disproof of the original.

# Pass-3 proposed resolution, pending fresh review

The original interpretation above is unchanged. Research pass 3 reconstructed
the new supervisor interval-packing input into an all-metric transfer theorem,
an explicit observable tree-enumeration/preorder procedure, and an all-n
expected true-cost proof for every fixed p<1/2. The complete proposed argument
is `evidence/research-pass3-full-proof.md`; the current primary comparison is
`evidence/research-pass3-literature.md`. This is a full-resolution candidate,
not a fresh mathematical/innovation/STOC acceptance. The earlier stronger
ultrametric B4 test remains unresolved and is unnecessary for this new proof.
No source quantifier, cost objective, adversary, metric hypothesis, or
information-theoretic algorithm scope has been narrowed.
