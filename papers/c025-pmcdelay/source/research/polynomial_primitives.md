# Polynomial primitive contracts and actual source checks

Research job c025-pmcdelay-research-338d67d18097, 2026-11-01 UTC.

## Minimal separators: an actual finite-state polynomial-delay primitive

Use the Berry–Bordat–Cogis queue scheme referred to by BLS Lemma 1, not the root finite checker's subset oracle. For a connected noncomplete input, maintain a binary trie of seen separators and a linked queue. During initialization, for every v, find the components C of G-N[v] and insert each N(C). Then, while the queue is nonempty: dequeue and emit one separator S; for each x in S find the components C of G-(S union N(x)) and insert each N(C). Only unseen sets are enqueued. Optionally check the two-full-components criterion before inserting each candidate, as the targeted code does; this costs polynomial time and cannot exclude a minimal separator. The BBC correctness theorem supplies completeness of this scheme. BLS Lemma 1 explicitly supplies the polynomial-delay theorem.

There are at most n component searches and n^2 candidate sets in initialization, and at most n component searches and n^2 candidates in one queue expansion. A candidate's full-component validation and trie operations are polynomial. Emit on **dequeue**, before expanding the separator: initialization is polynomial; between emissions one expansion and one dequeue are polynomial; after the last emission its one expansion and empty-queue check are polynomial. There is no long final scan of previously output separators and no bulk deallocation. If no separator exists the initialization and empty check are polynomial. The old igraph implementation's linear scans over its answer list are NOT used for the mathematical worst-case bound: replace them with tries.

The official igraph source was opened at
https://raw.githubusercontent.com/igraph/igraph/main/src/connectivity/separators.c
on 2026-11-01 UTC. Its initialization/generation loops (lines 524–583 in the returned source) instantiate the BBC component-neighborhood recipe; this is an implementation comparison, not an independent theorem. The primary BBC publisher record was opened:
https://link.springer.com/chapter/10.1007/3-540-46784-X_17 .
The older chapter full text was not downloaded in this pass; BLS's actual local primary Lemma 1 is the theorem-level dependency. The alternative Takata primary publisher abstract confirms polynomial delay for fixed-pair minimal separators, but its second result is cumulative delay for all minimal vertex separators; those two statements must not be conflated. Takata is not needed by this proof.

The targeted checker implements this queue scheme and verifies its COMPLETE distinct separator set against an exhaustive full-component oracle on 29 specified graphs. Python sets are used in that finite diagnostic; the mathematical algorithm replaces them by tries. Successful finite comparison does not establish completeness on arbitrary inputs; that assertion is the cited BBC theorem.

## Minimal triangulations and maximal cliques

The actual local primary MCS-M input has SHA-256
67a62a4231c26f2b6b09da46d8bf3cfee32fd597d893546409d234d58e30b9c7.
The text has SHA-256
81385fd380438135c402fff92c5c11e05775b81eba1d5bc7d0801f0ebf4edae5.
Theorem 4.4 p.294 states minimal triangulation in the inclusion-minimal sense (defined on p.287). Pseudocode p.291: assign initial zero weights; choose a maximum-weight unnumbered vertex v; for each unnumbered u test whether uv is an edge or has an unnumbered path whose internal vertices have weight less than w(u); increment all selected weights and add the corresponding fill edges; number v. All weights of a step are tested before that step's increments. Fixed label order breaks ties.

One can implement those path tests naively by adjacency-matrix BFS, at most n^2 times, for a plainly polynomial bound without relying on the optimized O(nm) implementation discussed on p.297. The resulting ordering is a perfect elimination ordering of the triangulation. Every maximal clique is some vertex together with its later neighbors, so list at most n candidates and remove nonmaximal ones by pairwise subset checks. These are all polynomial operations. The helper calls this on at most n saturated blocks, each of size at most n.

## Recognition and neighborhood

Use BLS Theorem 4 / Lemma 7 and the explicit full-component/nonedge criterion in research/streaming_proof.md. It is implemented in the retained intake/pmc_atom_neighborhood.py and used only as a recognition routine, not an all-output oracle in the generator. The new generator in research/targeted_streaming_check.py enumerates neighbors by graph searches with the endpoint guard, with no exponential list of candidate PMCs. The finite EXPECTED-output checker separately tests all subsets for n<=10. Source structural dependencies and the endpoint transfer proof are identified in the proof dossier.

## Reproduction and operational limits

Run `/opt/anaconda3/bin/python3 research/targeted_streaming_check.py` from this project. It uses existing NetworkX for MCS-M only, not for enumeration of minimal separators or PMCs. Result: 29 cases, every complete PMC and separator set matched, no duplicate output, helper witness/fiber and recursive lift/queue counts checked. Inputs/outputs are serialized in evidence/pass1-targeted-streaming.json. Cases were chosen for boundary/structured behavior and eight new seeded n=9 random instances; no atlas sweep was rerun. This is same-worker finite evidence, not an independent audit.

The initial invocation with PATH python3 failed because that interpreter lacked NetworkX. The available explicit Anaconda interpreter ran the test successfully. Both outcomes are retained in evidence/pass1-operational-log.md. Neither dependency access nor finite runtime is used as mathematical evidence for an asymptotic theorem.
