# Full-scope proposed proof: all-PMC polynomial delay

Proposer: c025-pmcdelay-research-338d67d18097. Research evidence, not a manuscript or an accepted review. This proof addresses the exact immutable source.md question. Standard results below are dependencies, not new claims. No polynomial-space assertion is made.

## Statement and computational conventions

There is a deterministic algorithm which, on every finite simple undirected graph G, enumerates every nonempty potential maximal clique (PMC) exactly once, and has polynomial initial, inter-output and final delay. The empty vertex graph terminates in polynomial time without output. Space may be exponential. Here minimal triangulation means inclusion-minimal chordal supergraph on the same vertex set.

Use an adjacency matrix, bit vectors, binary tries for discovered sets, and linked queues. All dictionary operations take polynomial worst-case time independent of the number of stored sets. Each trie has depth at most n. There are at most 2^n outputs per recursive level and n levels, so addresses and counters have polynomial bit length. The argument works in a pointer RAM with polynomial-length words; charging polynomial bit cost to each operation also retains a polynomial bound. Retain allocated memory until overall termination: do not perform an exponential teardown after the last output.

## Verified standard dependencies

Let BLS denote Berge, Limouzy and Schivre, arXiv:2610.19850v3 (20 October 2026), local input intake/primary/2610.19850v3-PMC.pdf and matching text.

1. BLS Theorem 4 / Lemma 7, pp.15: polynomial PMC recognition. Equivalently, a nonempty Omega is a PMC iff no component of G-Omega has neighborhood Omega and every nonadjacent pair in Omega belongs to the neighborhood of some component of G-Omega.
2. BLS Lemma 2, p.12: a minimal separator has two distinct full components, and this characterizes minimal separators.
3. BLS Lemmas 11 and 12, p.17: each child PMC X of G-a has a valid lift X or X+a; every PMC containing a is X+a for a child PMC X or S+a for a minimal separator S of G.
4. BLS Lemma 1, p.12: enumerate all distinct minimal separators with polynomial delay (O(n^3) in its statement), citing Berry–Bordat–Cogis, WG 1999, DOI 10.1007/3-540-46784-X_17. Use this known enumeration primitive with polynomial initialization/finalization, not an all-subsets oracle. An explicit queue implementation and endpoint accounting are given in research/polynomial_primitives.md. It suffices to use any fixed polynomial delay bound; no exponent improvement is claimed.
5. BLS Theorems 8–11 and Corollary 3, pp.32–42: all a-nice PMCs are reached from the non-a-nice PMCs by its polynomial neighborhood. Section below spells out the computational formula, resolving an endpoint wording inconsistency explicitly.
6. Berry–Blair–Heggernes–Peyton, Algorithmica 39 (2004), 287–298, DOI 10.1007/s00453-004-1084-3: MCS-M computes an inclusion-minimal triangulation (Theorem 4.4 p.294). Its pseudocode is on p.291 and polynomial O(nm) implementation discussed on p.297. A naive implementation testing each fill-path by graph search is also polynomial and is sufficient here. The supplied local primary PDF/text was inspected. A perfect elimination ordering lists all chordal maximal cliques in polynomial time: form each vertex plus its later neighbors and discard nonmaximal candidates.

## 1. Polynomial separator helper with a witnessed bounded fiber

For any minimal separator S of a connected G, choose two full components C,D of G-S by fixed label order. For every component C_i of G-S let B_i be G[S union C_i] with S made a clique, and compute a minimal triangulation T_i of B_i using deterministic MCS-M. Let T be their union. It is chordal: chordal graphs glued along a common clique remain chordal (an induced cycle visiting two pieces would have two nonconsecutive vertices in the common clique).

T is an inclusion-minimal triangulation of G. Indeed let G subset H subset T with H chordal. For a pair x,y in S whose edge is absent from H, there exist x-y paths with interiors in C and in D because each is originally connected and full. Choose shortest such paths in H restricted to each side plus x,y. Both paths are induced and have length at least two. Their interiors have no cross edges in T, and hence none in H. Together they give an induced cycle of length at least four, a contradiction. Consequently S is a clique in H. For every i, H[S union C_i] is a chordal supergraph of B_i contained in T_i, so it equals T_i by minimality. Thus H=T.

There is a maximal clique Gamma of T_C properly containing S. Here is a justification that does not assume this extension for arbitrary nonchordal graphs. Take a clique tree of the connected chordal graph T_C. The clique-tree subtrees for vertices of S intersect pairwise, so have a common node. Nodes whose cliques meet C form a connected subtree: for each c its containing nodes form a subtree, and adjacent vertices of the connected graph T_C[C] have intersecting subtrees. This latter subtree intersects each subtree for s in S because s has a neighbor in C. The Helly property for subtrees of a tree now gives a clique node containing S and at least one vertex of C. (The Helly property follows by rooting the tree and choosing the deepest of the closest-to-root vertices of the subtrees.) Hence a proper extension exists and is found among polynomially many chordal maximal cliques.

Gamma is maximal in all of T: no vertex in another C_i is adjacent to its vertex in C. Therefore Gamma is a PMC of G. Since Gamma subset S union C and contains S, the other full component D remains an entire component of G-Gamma and N_G(D)=S. Fix all choices deterministically. For a fixed image Gamma, every distinct preimage separator S is the neighborhood of a component of G-Gamma, of which there are at most n. Thus every fiber of S -> Gamma(S) has size at most n. The helper and witness are computed in polynomial time.

This extension construction has a prior analogue in IPEC 2025 article 21, Proposition 29, p.21:14. Neither extension alone nor the numerical inequality |Delta|<=n|PMC| is claimed new.

## 2. Endpoint-safe source neighborhood and seed completeness

For a PMC W and each ordered pair u,b in W with u != b, set X=W union N_G(u). Compute A, the b-component of G-(X minus {b}). Reject the pair if u lies in A union N_G(A). Otherwise compute U, the u-component of G-N_G(A), and S=N_G(U). Compute the b-component B of G-S and Z=X intersect (S union B). If Z is a nonempty PMC, retain Z as an out-neighbor. All steps use graph search and recognition, and there are at most n^2 pairs. The rejection condition ensures b and u survive and are separated by S: S subset N(A), b in A, u outside N[A], and S is the standard close (A,u)-separator. There is no undefined component search.

BLS Definition 12 literally assumes X minus {a} is an (a,b)-separator, which would exclude b from X; Definition 20 later chooses both endpoints in X. We do not silently rely on this inconsistent wording. The formula above is an explicit extension of its Lemma 4. It retains all the arcs actually used in BLS Theorems 9/10, as follows.

For an a-nice target Omega, put S0=N_G(C_G(a,Omega)), T0=Omega minus S0, and C_a=C_G(a,Omega). BLS Lemma 10 places T0 in a full component C_T of G-S0. Since N(C_a)=S0, C_a is itself a whole component of G-S0. Source Theorems 8–10 produce a predecessor W, a vertex u in W intersect C_a, and b in T0 subset W, with

    Omega subset X=W union N(u) subset Omega union C_a,

and either a in W or C_G(a,W) is a proper subset of C_a. For Theorem 9, u=a, W={a} union S_hat union T0, and the missing S0 vertices are adjacent to a. For Theorem 10, W=D union (Omega minus S_D) union S_D_prime, D subset C_a, u in D, and every missing S_D vertex is adjacent to u. These are the precise constructed witnesses in the cited proofs, not arbitrary arcs guessed from an informal definition.

For this witness, A lies in C_T and has no vertex or neighbor in C_a. Every s in S0 is in N(A): PMC visibility gives an edge b-s or a b-s path whose interior avoids Omega; since s separates C_T from C_a, the path interior lies in C_T and avoids X. Thus the graph search starting at b reaches a neighbor of every s. We have S0 subset N(A), and N(A) is disjoint from C_a. It follows that the u-component of G-N(A) is exactly C_a and the computed S is exactly S0. The rejection does not apply. Finally X intersect (S0 union C_T)=Omega, so the computed neighbor Z is exactly the target. This proves the transfer of the needed preimages to the explicit formula.

Repeatedly take these source predecessors. Until a predecessor is non-a-nice, the nonempty a-component strictly decreases; hence the process stops within n steps. Reversing the resulting sequence shows all a-nice PMCs are reachable from the family of non-a-nice PMCs using the endpoint-safe neighborhood. Source structural Theorems 8–10 are used as established prior results; they are not being reproved or claimed new.

## 3. Streaming generator with exact pauses

For a connected nonempty graph H, construct A(H) as a coroutine. If H is complete, emit its vertex set once and halt. Otherwise choose a vertex a whose deletion leaves H connected. A leaf of any spanning tree suffices. Maintain an initially empty trie Seen and linked queue L. Insert(Z) checks Seen; if Z is new it stores Z, appends Z to L, and immediately emits Z, pausing at that exact point before further work. No bulk copies of lists are needed at phase transitions.

I. Run A(H-a) until its next distinct child emission X, at which point the child is suspended. Test both X and X union {a} as PMCs of H and Insert every valid lift, in fixed order. Resume the child only after these tests and any emissions have completed. Continue through the child's final halt.

II. Start the fixed polynomial-delay separator enumerator on H. For each distinct separator S emitted, pause it and compute Gamma(S), Insert(Gamma(S)), then test S union {a} and Insert it if valid. Resume the separator enumerator after processing this separator, and continue through its halt.

III. While L is nonempty, pop its first vertex W, compute its at most n^2 candidate neighbors by the explicit formula above in fixed order, and Insert all valid unseen PMCs. Queue entries are popped only once. Finish and halt when L is empty. L already contains all discoveries in phases I–II, so there is no exponential queue-initialization step.

Every emitted set is a valid PMC, and the trie prevents repetitions. Distinct child PMCs give distinct root lifts, because deleting a from a lift recovers exactly the child set. Lemma 11 ensures at least one valid lift for each child. Phase I therefore supplies every PMC of H that is also a PMC of H-a. Lemma 12 and phase II supply all PMCs containing a. These are exactly the non-a-nice PMCs. The transfer result in section 2 proves that phase III discovers all remaining PMCs. Extra helper seeds do not remove any reachable vertices. Thus the generator is correct and terminates.

## 4. Simultaneous emission and termination bounds

For a connected nonempty H let K=|PMC(H)|>=1 and K_c=|PMC(H-a)|. Choose a nondecreasing, fixed computable polynomial p(n)>=1 bounding initialization, base-case work, processing one child output, one separator gap and its helper/lift processing, one full neighborhood expansion, and the constant number of phase/finalization operations. Include all trie, queue, coroutine, serialization and bit-operation costs. All primitive descriptions above justify such a polynomial; its coefficients can be fixed once from these fixed implementations. No measured runtime or exponential subset oracle is used. Set Q(1) sufficiently large and

    Q(n)=Q(n-1)+(n+10)p(n).

In particular Q is a fixed, computable polynomial bound (or use the explicit polynomial upper bound Q(1)+(n+1)(n+10)p(n)). Prove together:

(E) for 1<=j<=K, the j-th distinct emission occurs by Q(n)j steps;
(T) the full generator halts by Q(n)K steps.

The complete-graph base cases satisfy both by the choice of p and Q. For a noncomplete connected H, write D=|Delta(H)|. The lift injection gives K_c<=K; the helper fiber gives D<=nK. At most K queue entries are popped. The child's full cost is at most Q(n-1)K_c by T. All parent costs together are at most p(n)(K_c+D+K+5). As K>=1, this is at most (n+7)p(n)K. This proves T at dimension n without multiplying Q(n-1) by any factor exceeding one.

For E, classify the j-th emission by its phase.

I: If it occurs during processing child emission r, each of the preceding r-1 child outputs already supplied a distinct lift. Thus r<=j. The suspended child's cost is at most Q(n-1)r by E, and all parent costs so far are at most p(n)(r+2)<=3p(n)j. The emission is by Q(n)j. An emission between two lift tests does not resume the child and causes no extra recursive work.

II: The child has halted, with cost at most Q(n-1)K_c. Its valid lifts are already present, so K_c<=j. If the current separator has number r, the first r-1 separators have all produced a helper image among the preceding j-1 root outputs, whether newly discovered in phase II or earlier in phase I. The fiber bound gives r-1<=n(j-1), hence r<=nj. Parent work so far is at most p(n)(K_c+r+4)<=(n+5)p(n)j. This includes initialization and separator intervals, and establishes E.

III: Every separator helper is among the previously emitted PMCs, so D<=n(j-1). The number q of queue expansions begun through this emission is at most j, since each popped vertex was emitted earlier and popped once. Also K_c<=j. Child and local costs are at most Q(n-1)K_c+p(n)(K_c+D+q+5)<=[Q(n-1)+(n+7)p(n)]j. This proves E. Phase boundaries and all final cleanup are included in T. The simultaneous induction is complete.

The crucial strengthening over the existing total-time bound is a bound on each emission rank plus a separate bound on complete termination. Merely substituting a child prefix estimate with an extra +1 can introduce a spurious multiplicative recurrence; it is not used here.

## 5. Buffering with first and final delay

For connected nonempty H, let q=Q(n), rounded up to an integer. Simulate A(H) for blocks of q primitive steps, stopping early on its halt. Save each emitted PMC into a FIFO buffer. After each block return one buffered PMC; if the simulated generator has halted, drain its buffer with polynomial serialization cost per item and then terminate. Integrate the O(poly(n)) enqueue operation into each simulated emission cost; a step counter and simulation bookkeeping change the polynomial bound only by a polynomial factor.

There cannot be an empty buffer at the end of a block while the generator is running. At the end of block j, if j<=K, E guarantees at least j generated outputs, while only j-1 have been returned. If j>K, T guarantees the generator has already halted by qK<qj, contradiction. If it halts during the block, it has generated all K outputs, and any remaining unreturned output is already buffered. It has halted by the end of block K, so after the K-th output there is no residual simulation tail. The initial, inter-output and final waits are all polynomial. Using blocks of 2q as in the supplied proposal also works, but is unnecessary. The conversion is standard (Capelli–Strozecki STACS 2023 and Computational Complexity 2026); it is not claimed new.

## 6. Empty and disconnected inputs

A minimal triangulation of a disconnected G has no edge between its original connected components. Removing all such cross edges leaves a disjoint union of chordal induced subgraphs containing G, so inclusion-minimality forbids cross edges. Conversely the disjoint union of minimal triangulations of its components is minimal: a proper chordal subtriangulation would restrict to a proper subtriangulation of some component. Therefore the nonempty PMCs of G are exactly the disjoint union of the PMC families of its nonempty connected components, viewed on the original labels.

Find components in polynomial time. If none exist, halt without output. Otherwise run the buffered algorithm above on each component sequentially. Each component has at least one output; different components produce different nonempty sets. At a component boundary the final waiting of one plus the initial waiting of the next is polynomial in n. The first and last boundaries and all isolated/complete components obey the same bound. This proves the stated all-input theorem.

## Scope, contribution and review obligations

Known ingredients are PMC recognition/lifts/seed reachability, polynomial separator enumeration, minimal triangulation, separator extension, and amortized-to-delay buffering. The proposed additional contribution is the full streaming conversion: supply actual helper outputs with polynomial fibers during the separator phase, interleave recursive lifts at exact emissions, and prove simultaneous rank and termination estimates with an additive polynomial recurrence. This establishes a guarantee not supplied by total output-linear time alone. It does not improve the number of PMCs, establish polynomial space, or give an FPT bound for small PMCs. The full target is resolved by the argument above as a research proposal; no fresh correctness, innovation or STOC assessment has yet occurred.

Known unproved assertions within this proposed proof: none beyond the explicitly cited standard source theorems. Source dependence and the endpoint transfer are exposed for adversarial checking. A fresh referee must reject if these dependencies are invalid or if the conversion is already known or mathematically routine/value-insufficient. The older supplied finite checks and the targeted new primitive tests are only finite diagnostics and are not used to prove any universal complexity bound.
