# Frozen original: near-optimal pairwise reachability preservers under two faults

## Primary question and precise benchmark normalization

Chakraborty--Chatterjee--Choudhary, *Pairwise Reachability Oracles and Preservers
under Failures*, arXiv2110.11613v1, introduction printed p.3 after Theorem1.7:
“We pose closing this embarrassing gap as an interesting open question.”
The gap is between their actual-subgraph size upper bound in Theorem1.5 and
lower bound in Theorem1.6, not the already settled oracle-size question.
Primary full version: https://arxiv.org/abs/2110.11613 . Official ICALP2022:
https://doi.org/10.4230/LIPIcs.ICALP.2022.35 . Full PDF SHA-256:
`b7fc4f50c38ff1b1c6264959bbad56f6342d0eaba9e77db14f761935c4c86821`.

The statement below normalizes their open frontier as a near-optimal explicit
construction. It is OUR precise benchmark, not a verbatim author conjecture
with these resource/probability constants. No theorem resolving it is known
in the inspected current primary sources; this is bounded open-supported
evidence, not a priority guarantee.

## Complete unchanged assertion

There exist a single uniform randomized ordinary word-RAM algorithm A,
absolute constants C>=1 and an integer c>=0, with the following properties.
For EVERY finite simple directed graph G=(V,E), n=|V|, m=|E|, and EVERY set
P subset V x V of p distinct ordered demand pairs, A on every random tape:

1. Halts within (n+m+p+2)^C ordinary word operations and memory words, where
   words have O(log(n+m+p+2)) bits. Input, preprocessing, randomness, auxiliary
   constructions, correctness checks and explicit output are all charged.
   No free reachability, min-cut, oracle, transitive closure or advice is allowed.
2. Outputs a SUBGRAPH H=(V,E_H) of G. For EVERY set F subset V union E with
   |F|<=2, simultaneously, and for EVERY (s,t) in P, s reaches t in H-F if
   and only if s reaches t in G-F. F may mix edge and vertex faults. Deleting
   a vertex deletes all incident edges; a pair with a failed endpoint is
   unreachable by convention. A surviving vertex reaches itself by zero hops.
3. With probability at least 1-(n+2)^(-10), the same H also satisfies

       |E_H| <= C (n+n sqrt(p)) log(n+2)^c.

For p=0, the algorithm may return the empty edge set. Empty/disconnected graphs,
cycles, unreachable demand pairs and isolated vertices are in scope. A simple
graph is the declared input domain; no multigraph/weighted exact-distance
extension is required. On a failed random tape returning all of G is valid,
but all tapes must satisfy the fixed polynomial cap and reachability correctness.
Verification of all failure sets is polynomial for the fixed fault count and
may be used at its actual cost. The high-probability size bound may be obtained
by a Las Vegas polynomial-expectation construction plus justified truncation
and a correctness-preserving fallback, with all constants/bit costs explicit.

This is preservation by ORIGINAL INPUT EDGES. A compact Boolean oracle,
Steiner graph, shortcut graph, sourcewise-only preserver, additive/multiplicative
distance approximation, or only single-failure guarantee does not resolve it.
An existence statement with no polynomial construction is insufficient for
this frozen algorithmic benchmark. A local short-core lemma is only a route.

## Nearest verified primary results

- CCC arXiv2110.11613v1 Theorem1.5 / Section6: polynomial-time actual subgraph
  of O(n^(4/3) p^(1/3)) edges, plus the independent O(np) single-pair baseline.
  Theorem1.6 / Section8.1 gives Omega(n sqrt(p)) necessary edges in worst cases.
  Their Theorem1.1 ALREADY gives an O(n sqrt(p))-size dual-fault Boolean oracle;
  its stored information need not be graph edges.
- Chatterjee's current May2026 thesis arXiv2605.20897v1, abstract and Chapter2,
  retains the same actual-subgraph upper bound. It does not claim the desired
  improvement. Its concluding open-problems chapter concerns clustering;
  do not misattribute a new preserver conjecture to that chapter.
- Single-source fixed-fault reachability preservers of O(2^f n) edges are
  already known (Baswana--Choudhary--Roditty, STOC2016; CCC Theorem2.1).
  Taking p separate certificates costs O(np), which is too large.
- Color-fault distance preservers (Parter--Petruschka, arXiv2504.17868v2,
  ICALP2026.146) preserve a different, restricted failure family. Their optimal
  colored size result does not settle arbitrary two-fault pairwise reachability.
- The fixed-p and index-sensitive nonadaptive fault-free preservers of
  Bodwin--Le (arXiv2410.20471v1/SODA2025) are also a different model.

For p=n the desired improvement is from n^(5/3) to tilde-O(n^(3/2)), closing
the polynomial gap to the matching preserver lower bound. It would distinguish
how much graph-edge realization costs beyond a compact reachability oracle,
and require a reusable method sharing two-fault certificates across demands.
A sequential polynomial construction is the entire target; no parallel-depth
or directed-Steiner competitive-ratio consequence is asserted without proof.

## Resolution discipline

The full quantified assertion is frozen. A negative resolution must refute
it, not just the short-core conjecture or one pruning rule. Preserve all
earlier projects and attempt limits; this differs from c048's all-pairs
shortcut-construction-time target, c026's undirected color-connectivity labels,
and the unadmitted all-fault-count exact-distance frontier. No scope replacement,
renaming reset, routine lemma PDF, or new manuscript is authorized unless this
complete original is resolved with substantive innovation and real fresh audits.
Future author: Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my.
