# Fresh mathematical review

Job: c029-vftfast-referee-95ddbe77df2f.
Frozen snapshot: b1495a4cbeb794181b64a2bc9a00b637d90f0a7a7fdf654844a24036b4029e66.
Verdict: **accept**, resolution-paper / proved, at the exact frozen scope.
Separate STOC assessment: **working_paper**.

This is an internal review of the supplied argument, not external peer review, a formal certificate, or a venue decision. I read the original source, precise problem, claim, snapshot and its listed proof/code/source inputs, together with the governing policies and primary literature. I did not consult checkpoint.md, state.json, earlier job transcripts, prior verdicts or an owner session. The history contained in the expressly authorized problem.md was not used as evidence of correctness. All 17 frozen file hashes and the canonical snapshot digest match. No frozen input was changed.

## Original scope

The accepted theorem is the complete deterministic uniform polynomial-time construction for each fixed rational delta in (0,1), on every explicit undirected unweighted simple graph and all integers f>=0,k>=1. It gives a subgraph with O_delta(sqrt(k)),O_delta(k) stretch simultaneously under every admissible vertex-fault set, and tilde-O_delta((f+1)^(1+delta) n^(1+1/k)) edges. The polynomial exponent depends only on delta. A smaller fixed rational exponent handles each real delta. The accepted statement is exactly source.md under problem.md, not an intermediate separator theorem, a fixed-parameter restriction or a disproof of a failed method.

## Reconstructed correctness and uniformity

**Representative paths.** For rank T=min(N,f+d+1), distinct Vandermonde columns over a prime field of size at least N represent the uniform matroid of rank T. An h-set avoiding Y, |Y|<=T-h, has nonzero exterior product with Y. Expanding its vector in a retained basis forces at least one retained actual set to avoid Y. This argument is exact in any chosen field with distinct vertex elements; it is not a randomized identity test. At stage i the DP retains paths representing avoidance of sets of size T-i-1. For an extension to v, the preceding forbidden set is Y union {v}, of size at most T-i, and the chosen parent therefore avoids repetition as well as Y. Reduction preserves the invariant. At the final stage a fault set disjoint from any d-path has size at most both f and N-d-1, so the T=N cap loses no required query. Orienting unordered pairs by the lesser endpoint is valid in an undirected graph.

The endpoint family size is at most binomial(T,h); L=max_(h<=d+1) binomial(T,h) is bounded by (f+d+1)^(d+1). All starts, path extensions, minor computations and field elimination fit N^O(1)(f+d+1)^O(d+1) with absolute O constants. Trial division to find a prime in [N,2N) and exact arithmetic of O(log N)-bit field elements are polynomial in the explicit graph size. No parameter-dependent exponent of N is concealed at this stage.

**Protected cut scan.** Every returned cut C is outside V(P), has size at most (r-1)f, and makes the current H distance exceed r. If a BFS path has no unprotected internal vertices, it survives every fault set outside P. Otherwise the f+1 short BFS paths on a rejection have pairwise disjoint nonempty unprotected parts, because each later path avoids all previously collected parts. No size-f cut disjoint from P can hit all of them. Thus rejection certifies that every such original-budget fault set has distance at most r. This proof protects the entire path, rather than just the endpoints. A returned witness causes at least one new edge to be inserted, since P itself would otherwise survive C with length d<=r.

Fix any final fault set F with |F|<=f and any original d-path avoiding F. A stored representative avoids F. Its insertion preserves a surviving d-path, while its rejection certified a surviving route of length <=r in an earlier graph. Monotonicity of H proves the final guarantee simultaneously, with no enumeration of F and no free oracle. Scanning each stored path once is sufficient.

**The critical packing transfer.** I checked the source's actual Lemma 4.12 induction and Appendix A, not just its theorem statement. The candidate's insertion sequence supplies H_i=union_(j<i)P_j, a disjoint witness C_i of size <=q and endpoint distance >r. Claim 4.3 supplies an s-critical edge whenever ds<=r. Its endpoints avoid C_i, and the edge is absent from H_i. Algorithm 2's update then uses only the current analytical path system, this edge, and C_i. I1--I7 and the path-exchange lemma use no omitted/rejected paths, completeness of the original scan, endpoint ordering or shortestness of P_i. The bounded-progress and neighbor-count arguments therefore remain valid for this sequence. This is a transfer of the source proof, not a false containment claim about two different greedy outputs.

Put a=sqrt(k), d=floor(a), t=ceil(a), R=ceil(a/eta), s=2R-1, with eta=min(delta/2,1/4), and r=ceil(12k/eta). These satisfy ds+2R<=4k/eta, 2R+d<=3a/eta and (2t-1)(2R+d)<=8k/eta for k>=4. For example R<=a/eta+1, d<=a, t<=a+1 and a>=2 give the first two inequalities; 2t-1<=2a+1<=8a/3 gives the third. Thus all the source's critical-edge and virtual-distance contradictions survive rounding and the larger radius.

With D=ceil(12 C' s^3 q^(1+eta) N^(1/k)), the local count is O(NDs). The actual sampling probability in Lemma A.1, not its tilde notation, bounds the centers by

    |S| <= 22 M q^(-eta R) N^(1-R/k),
    M=log(100*2^(R+2)*D^R*N).

Indeed 10C'sq/D <= (5/(6s^2))q^(-eta)N^(-1/k). Dropping the factor (5/(6s^2))^R only increases the bound. If the probability is capped at one, the uncapped expression is at least one, which yields the same upper bound for N centers. For q<N and k=O(log N), log D=O_eta(log(N+2)) and M=O_eta((log(N+2))^(3/2)). Thus an exponential-in-sqrt(k) positive constant is not being hidden in a logarithmic factor.

The source's spread-family and robust-sunflower arguments require only the same witnesses and spreadness; every virtual edge's vertex list avoids C_i, its realizing route is in H_(i+1), and its earlier virtual distance is >2t-1. Theorem 5.15 gives O(w q^w |S|^(1+1/t)) global rounds, w=d+1. The two exponents obey

    w-eta R(1+1/t) <= 1,
    (1-R/k)(1+1/t) <= 1.

The first follows from eta R>=a>=d; the second from R/k>=1/(t+1). Only a bounded power, <=3/2, is applied to M. Multiplying by d edges per round proves the claimed polylogarithmic size bound. If q>=N, the simple-graph bound N^2<=qN suffices directly. For f=0 take q=1; empty insertion witnesses still satisfy all the source assumptions with this larger analysis budget. For f>=1 take q=(r-1)f. These checks remove the principal potential gap in the candidate.

**Pendant scales and faults.** In each augmented graph J_ell the original fault set F is itself a permitted augmented fault set. If a surviving base distance is d-ell, appending the private ell-chain gives distance exactly d. A simple surviving route to the pendant tip must reach its base vertex and traverse that chain, with no useful excursions into other chains. Projection therefore supplies the required surviving base route. Segmenting a shortest G-F path into d-edge geodesic segments and one remainder gives distance <=(r/d)dist_(G-F)+r. The union remains a subgraph of G. At most d graphs of at most dn vertices are used, which costs only a polynomial in k in size.

**All parameters and the switch.** For n<=2 the whole graph fits. Capping f at n-2 loses no distinct surviving pair; larger fault sets have at most one surviving vertex. Capping k at K=ceil(log_2(n+2)) changes n^(1+1/k) by at most a factor two and improves the stretch parameters. Reading and capping binary integers costs polynomial input time. The bounded k<=3 DR branch satisfies 2k-1<=3sqrt(k), with no dense-graph shortcut for f=0.

For k>=4 and f^(eta d)>=n, DR with parameter d has size

    O(d f^(1-1/d) n^(1+1/d))
      <= O(d f^(1+eta-1/d)n),

which fits the target with logarithmic slack, and stretch at most 2sqrt(k). Its stated worst-case runtime is polynomial for capped f,d. In the complementary regime,

    (d+1)log(f+d+1)
      <= (d+1)log(f+1)+(d+1)log(d+1)
      = O_eta(log(n+2)).

Here log f<log n/(eta d) when f>=1, and (d+1)log(d+1)<=2d^2<=2K; f=0 is immediate. Thus the otherwise expensive representative DP is polynomial uniformly over the entire remaining regime, even in the augmented graphs. Every other factor in d,r,k and scale count is polylogarithmic. The resulting size has fault exponent 1+eta<=1+delta, and r/d=O_delta(sqrt(k)), r=O_delta(k). No expectation, random failure event or runtime tail remains.

## Independent checks actually performed

I wrote audit/referee_checks.py without importing any researcher module. It computes minor vectors by permutation determinants over F_11, uses a separate basis implementation, and compares against DFS path enumeration and BFS distances. It checked 84 graphs (all labeled n=2,3,4 graphs and ten explicit n=5 masks), 2,012 representative instances, 22,712 avoidance comparisons, 1,636 scans, 3,638 insertion witnesses, 5,866 rejection/fault comparisons, 15,624 all-length-path distance tests and 1,078 mixed-distance tests after pendant projection. All passed; augmented N<=10. The full machine-readable scope is audit/referee-checks.json. The frozen research finite-check files were inspected as supporting evidence, not rerun into their frozen output paths. These experiments do not prove asymptotic sparsity or the infinite theorem. Those conclusions depend on the reconstructed argument and the stated primary results.

## Novelty, substantive value and limits

The primary comparisons and fresh searches are in audit/literature.md. PPT Theorem 1.4 supplies the identical size/stretch tradeoff and the deep packing analysis, but its stated construction enumerates short paths and takes about f*n^sqrt(k) time. DR and BDR supply polynomial multiplicative spanners; they cannot alone meet this target's density exponent and O(sqrt(k)) stretch in every regime. FLPS already supplies the exterior-basis and path-DP technique. Karthik--Parter and the 2026 RPC papers further establish the general short-path/fault-covering idea. Accordingly I do not credit the candidate with a new representative primitive, cut approximation, packing theorem or pendant reduction.

The substantive new contribution is the complete uniform algorithmic theorem obtained by arranging these tools so that the f-dependent exponent is paid only where it is polynomial, with the complementary density paid by the multiplicative construction. The preservation of PPT's witness-sequence sparsity is necessary and has been verified. Neither selecting a fixed k/f, applying the usual black-box fault-sampling size bound, nor simply invoking the multiplicative theorem establishes this conclusion. The result crosses from a quasi-polynomial construction to deterministic polynomial time for the full recent mixed-stretch tradeoff. This is a meaningful construction benefit and clears the resolution-only innovation gate, despite the standard constituents. No equivalent combined theorem was found in the bounded current primary-source search; this is not an exhaustive priority guarantee.

The contribution is narrower than a new sparsity/stretch frontier or a new broadly applicable combinatorial tool. Its runtime exponent is not optimized and may be large as delta shrinks. The record does not demonstrate an additional algorithmic application or a strong broad STOC impact case. Those are venue-level weaknesses, recorded separately as working_paper; they are not missing mathematical hypotheses. No mathematical gap or required substantive revision remains identified in this frozen candidate. No manuscript or PDF was created in this job.
