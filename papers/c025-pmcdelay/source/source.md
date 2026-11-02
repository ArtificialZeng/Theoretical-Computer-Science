# Frozen original: polynomial-delay enumeration of all potential maximal cliques

Primary: Pierre Berge, Vincent Limouzy and Nicolas Schivre, Output-linear time
enumeration of potential maximal cliques, arXiv:2610.19850v3,20October2026,
Section1.4, printedpage8. URL https://arxiv.org/abs/2610.19850v3
Original source wording: "finding a polynomial-delay enumeration algorithm for
PMCs remains an open challenge."

Full mathematical target: on EVERY finite simple undirected graph G, enumerate
all its nonempty potential maximal cliques exactly once, with a fixed polynomial
in |V(G)|+|E(G)| bounding the time before the first output, between consecutive
outputs, and after the final output until termination. A potential maximal
clique is a maximal clique of some inclusion-minimal chordal completion of G.
Disconnected inputs and complete graphs are included. No cardinality bound,
planarity, bounded width, promised atom, given triangulation or precomputed
exponential list is supplied. Exponential storage is allowed; polynomial space
is a distinct stronger open direction, not an unstated requirement here.

A full positive solution must give the algorithm and complete all-input and
worst-case delay proofs, including preprocessing and termination. A complete
negative solution would need to rule out this quantified algorithmic assertion
under clearly stated, justified complexity assumptions. Failure of a particular
neighborhood, finite testing, a polynomial total-output-time bound alone,
parameterized delay in maximum output size, or an easier graph class is not a
resolution. The statement is immutable throughout this project's attempt history.

Current nearest primary results:2610.19850v3 Theorem1 gives total
O(n^4 m |PMC(G)|) time, not polynomial delay.2610.24856v1 Theorem1.1 gives
2^{O(k^3)} n^4 log n delay for outputs of size<=k, not all-size polynomial
delay.2506.12635/IPEC2025.21 gives polynomial delay on triconnected planar
inputs. Read actual supplied PDFs/theorems and recheck current follow-ups;
no proof claim is ignored for lack of peer review or formalization.

This is a new still-open target, not preaccepted mathematics. A root streaming/
separator-charging proposal is supplied for attack in intake; it does not narrow
the original or constitute a fresh referee verdict. Only a full original
resolution plus substantive innovation and actual fresh review permits WRITE.
