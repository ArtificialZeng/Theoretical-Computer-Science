# Current primary comparison, research pass 3

Job `c049-dualpreserve-research-2396269cbd5d`; checked 2026-11-03 UTC.
Bounded search only; no completeness or priority claim. Raw retrievals are
in this job's web JSON files. Secondary search hits were leads only.

- Chakraborty, Chatterjee, Choudhary, *Pairwise Reachability Oracles and
  Preservers under Failures*, https://arxiv.org/abs/2110.11613 : the current
  primary history still lists v1. The local actual full-text Section 6,
  Theorems 6.1/1.5 was read for the old pairwise subgraph bound and its
  path-frequency construction. Its oracle result has a different output
  object. No full-resolution claim was found in the inspected current hits.
- Chatterjee, *Creating Robust and Fair Graph Structures for Connectivity
  and Clustering*, https://arxiv.org/abs/2605.20897 : May 20, 2026, current
  history v1. Its actual abstract retains O(n^(4/3)|P|^(1/3)) edges for
  dual-fault pairwise reachability preservers. This supports the existing
  bounded open-status record, not a proof of absence of another result.
- Hoppenworth, Saranurak, Wang, *Near-Optimal Fault-Tolerant Strong
  Connectivity Preservers*, https://arxiv.org/abs/2510.02562 : current v1,
  FOCS 2025. The primary abstract preserves SCC partitions under edge
  failures. This is a different requirement from all specified one-way
  reachability demands; no inference settling source.md is justified.
- Borradaile, Iglesias, Migler, Ochoa, Wilfong, Zhang, *Egalitarian Graph
  Orientations*, JGAA 21(4) (2017), 687--708,
  https://doi.org/10.7155/jgaa.00435 , primary full text
  https://jgaa.info/index.php/jgaa/article/download/paper435/2532 .
  Directly inspected Section 2, Corollary 2 and Theorem 3. Path reversal
  optimizes convex indegree costs; the orientation solver here is known
  machinery, not an innovation or a solution to its missing graph bound.
- Frank and Murota, *Discrete Decreasing Minimization, Part I:
  Base-polyhedra with Applications in Network Optimization*,
  https://arxiv.org/abs/1808.07600 : current v3 (July 9, 2019). Primary
  abstract verifies prior square-sum optimality/min-max theory in a much
  more general framework. Only that scope is attributed here; no theorem
  about dual-fault pairwise critical graphs follows from it.

Searches included two-fault pairwise reachability/preserver bounds in
2025--2026 and minimum-square indegree orientation/path reversal. They did
not identify a full equivalent resolution. New generic orientation/density
calculations in math.md are conservative research reductions with no
substantive novelty certification, and do not satisfy the publication gate.
