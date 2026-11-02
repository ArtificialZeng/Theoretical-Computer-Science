# Research pass 1: primary-source recheck

Job: `c029-vftfast-research-6281f7685c7a`; checked 2026-11-02 UTC.

The new source's live [arXiv record](https://arxiv.org/abs/2610.33934) and
[v1 full text](https://arxiv.org/html/2610.33934v1) still present the 24 October
2026 version. The introduction expressly leaves the running-time improvement
open. The locally supplied immutable text was used for the detailed witness
conditions, source Theorem 5.4, Proposition 4.14 and its Appendix A proof,
the robust CLFT process in Section 5.4, and Appendix B. The transfer argument
in research1-separator.md identifies the actual source dependencies; it does
not replace the source's long proof by a script or claim to freshly referee it.

[Dinitz--Robelle, Efficient and Simple Algorithms for Fault Tolerant Spanners](https://arxiv.org/abs/2002.10889)
still gives v2, dated 24 May 2020. The version-specific URL initially returned
a cache miss, while the unversioned primary record succeeded. Theorem 4 and
Algorithm 2 were inspected in the manifest-verified local v2 text. The protected
variant in the new report is explicitly classified as a routine adaptation.

[Bodwin--Dinitz--Robelle, Optimal Vertex Fault-Tolerant Spanners in Polynomial Time](https://arxiv.org/abs/2007.08401v3)
is the 31 October 2020 v3. Its guarantee remains purely multiplicative; it is
not an equivalent of the frozen mixed-stretch target.

[Fomin--Lokshtanov--Panolan--Saurabh, Efficient Computation of Representative Sets with Applications in Parameterized and Exact Algorithms](https://arxiv.org/html/1304.4626v4),
Theorem 1 and Definition 3.1, provide the precise representative-set comparison:
the usual size bound contains binomial(p+q,p), with disjointness against q
additional elements. Thus a binomial-sized family is not an f-independent
single-exponential-in-d path-selection algorithm. The new report proves its
own narrower path-list obstruction directly; it claims no new general
representative-family theorem. The primary
[product-family paper](https://arxiv.org/abs/1402.3909) was also inspected at
the abstract/definition level; its faster product computation alone supplies
no protected-cut separator.

The geodesic restriction must not be sold as an easy induced-path algorithm.
[Dalirrooyfard--Vassilevska Williams, Induced Cycles and Paths Are Harder Than You Think](https://arxiv.org/html/2209.01873),
abstract and results overview, gives clique-based conditional lower bounds
for generic induced-path detection. This is an adverse comparison, not a
hardness reduction for our separator or the original construction problem.
An H-dependent gap separator can return nongeodesic paths and need only be
complete on actual shortest-distance violations, so those generic detection
results cannot simply be transferred.

Bounded current searches used the new title with polynomial-time terms,
arXiv number with algorithm/running-time terms, representative-family/fault
path terms, and induced-path parameter terms. No full uniform polynomial-time
realization was found in the inspected sources. This is a bounded recheck,
not an exhaustive novelty certificate. Source access limits are operational
records and are not mathematical evidence. No external contact occurred.
