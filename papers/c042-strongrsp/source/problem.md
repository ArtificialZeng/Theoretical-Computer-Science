# Precise reading of the frozen problem

The immutable statement is `source.md` (SHA-256 93e36d243f9b6fec1df5dda18aacab258ad91c62c8465d0a010fddadbb319aa7). This file explains that statement; it does not replace or restrict it.

## Objects, definitions and quantifiers

For every finite directed adjacency-list graph G=(V,E), n=|V|>=2, m=|E|, source s in V, edge functions ell,c:E -> finite nonnegative reals, budget C>0, and rational 0<epsilon<=1/2, define ell(P) and c(P) as the sums of the corresponding edge quantities. OPT_C(t) is the minimum ell(P) over s-to-t paths with c(P)<=C, and is +infinity if there is no such path. The empty s-to-s path is allowed. Nonnegative cycles may be erased without worsening either quantity, so every finite optimum is achieved by a simple path. This observation does not authorize enumeration of all paths.

The assertion asks for universal constants K,a,b>0 and one explicit uniform deterministic classical algorithm A. On every such input, preprocessing and space must each be bounded by K(m+n) log(n+2)^a epsilon^(-b), with an immaterial universal adjustment of K for space. The representation has a finite length bound for every represented target and compact witnesses. For every target with OPT_C(t)<infinity it must represent t and deterministically return a genuine path P_t with c(P_t)<=(1+epsilon)C and ell(P_t)<=(1+epsilon)OPT_C(t), respecting its actual reported bounds. Witness queries take polynomial time in n, log(n+2), 1/epsilon plus output size, independent of numerical aspects/precision. Query work is not preprocessing work, and n separate static preprocessing runs do not meet the asserted total bound.

When OPT_C(t)=+infinity, unavailable is permitted; a returned genuine path must satisfy the relaxed cost guarantee. Unavailable cannot be used for a truly C-feasible target. Unreachable targets receive no fabricated witness. This is not an exact feasibility oracle for the original budget. In particular, feasibility hardness cannot be invoked by silently strengthening the output semantics.

Zero lengths/costs, OPT_C(t)=0, equal weights, disconnected graphs and every density/aspect are included. For OPT=0 the output length must be exactly zero. C=0 is outside the quantified main input and has the stated zero-cost-edge SSSP treatment. No simplicity or m<=n^2 assumption is added to rescue the query bound: the supplied graph conventions and any parallel-edge treatment must be accounted for explicitly.

## Computation model

Use the frozen exact real-arithmetic comparison RAM: charged +,-,*,/ and ordinary graph/control/index operations. No unit-cost logarithm or floor of arbitrary weights, digit extraction, exact exponential/Poisson oracle, randomness, unbounded advice or uncharged policy synthesis. Any approximation to probabilities requires a finite-cost construction and error proof. For rational encodings, intermediate rational representations must obey the frozen polynomial bit-length requirement; the arithmetic bound is not a constant-bit-time input-reading claim. Control indices have O(log(n+m+1/epsilon)) bits up to a constant. All numerical magnitudes, ratios and precision are excluded from the operation bound.

## Nearest prior result and the proposed delta

Ashvinkumar, arXiv:2610.18337v2 (29 October 2026), Theorem 1, printed p.3: deterministic all-target bicriteria RSP in Otilde(m log(nW)/epsilon^9), with W the positive-length aspect ratio. Theorem 2 keeps the aspect dependence for a fixed number of resources. The immediately following paragraph explicitly leaves strongly polynomial all-target near-linear (even sub-mn) time open, while distinguishing the known single-target consequence. Section 4 uses a fixed-length two-clock DP; Section 6 supplies deterministic witness extraction. The text's zero-resource bookkeeping and probability truncation statements are obligations to verify in a new algorithm, not substitutes for its proof.

ABK25, arXiv:2410.17179v1, printed p.42 open problems and p.46 Lemma C.1, isolates the same aspect dependence and the single-target bottleneck reduction. Appendix D handles zero-length optima. A separate bottleneck interval per target does not yield a near-linear all-target algorithm automatically.

Gorkiewicz--Karczmarz, arXiv:2502.10348v1, Theorem 1.3 and Section 6 (the supplied preprint numbering), gives offline approximate ordinary SSSP; Algorithm 4 and Lemma 6.1 use additive path suffixes. It is not an offline affine/stochastic DP theorem. Liu, arXiv:2506.19207v1, Theorem 1, has an online ordinary-SSSP m^(1+o(1)) log W guarantee, which supplies neither the constrained-path semantics nor the frozen complexity.

Proposed full delta: remove all numerical-aspect dependence while preserving deterministic near-linear all-target bicriteria preprocessing, witnesses and the stated numerical model. A possible method is edge-local scale events plus a boundary-compatible offline monotone two-clock DP. It remains unproved. A generic first-hit comparison alone, a subsidiary counterexample, a special family, sub-mn time, a per-target n factor or an m^(1+o(1)) overhead does not resolve this statement.

## Triage status and decisive first test

Source status: open-supported in the primary sources checked on 2026-11-03; this is a bounded literature assessment, not a priority certificate. Original mathematical status: unresolved. Admission: advance, with no candidate or manuscript. A complete algorithm would remove an explicit classical constrained-path efficiency barrier and might introduce a reusable offline control-system method. STOC competitiveness remains unassessed and conditional on a substantive full solution.

First research test: formalize the actual DP restricted to an active state set with inactive endpoint upper labels. Establish the correct probabilistic fixed point (nontermination is failure), a first-hit multiplicative boundary comparison, compatibility with tick monotonicity/clipping, and a deterministic static solve charged to active states and incident transitions only, or produce an exact rational counterexample to that contract. This test decides whether the proposed full-program engine is viable; it does not replace the full target. Later indispensable steps are aggregate offline event/edge work, scale coverage, rounding/precision, completeness/soundness and compact deterministic witnesses.
