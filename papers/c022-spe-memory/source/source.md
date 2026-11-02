# Frozen original: arena-independent memory for reachability SPEs

Primary question3: James C.A.Main, Automata Exchange25.26, July1,2025:
https://automata.exchange/25.26-memory-requirements-of-subgame-perfect-equilibria-in-reachability-games/
Exact source question (verbatim): “Can we provide memory bounds that are independent of the arena size for SPEs (satisfying a given subset of objectives) in reachability games?”

Precise full reading: does there exist F:N_{>=1}->N such that for EVERY
finite-player turn-based directed arena without dead ends (possibly infinite,
with no finite-branching hypothesis), initial vertex v0, qualitative Boolean
reachability target sets T_1,...,T_n and required winner subset S, whenever
there exists a pure subgame-perfect equilibrium whose outcome visits T_i
for all i in S, there exists such an SPE in which each player uses at most
F(n) memory states? F is independent of vertex/edge cardinality, target size
and branching. Do not restrict to finite arenas or bounded degree for a
positive answer. Negative fixed-player finite-arena families with unbounded
REQUIRED memory suffice to disprove this quantified statement, provided
no other SPE satisfying S evades the lower bound. Winning players outside
S may be added; ruling out one exact payoff alone is not sufficient.

The memory model is the source's VERTEX-UPDATE convention. A strategy is
encoded by finite M, initial m0, up:M x V->M and next_i:M x V_i->V;
at history h v it chooses next_i(up*(m0,h),v). Do not hide the previous
vertex in uncounted memory or replace this by an edge-update machine.
Arbitrary vertex-dependent functions are permitted in the possibly infinite
model; finite memory concerns |M|, not computable encoding of infinite tables.
SPE means no profitable unilateral deviation after EVERY legal history from
v0, not only histories consistent with the profile. A target visited before
the subgame remains satisfied. Objectives are qualitative reachability,
not quantitative arrival-time costs, Buchi, or safety objectives.

Primary comparisons: Brihaye/Bruyere/Goeminne/Raskin, I&C278(2021)104594,
related full version arXiv1806.05544, Proposition9 proves weak SPE=SPE for
Boolean reachability and uses the same vertex-memory model. Main's2026
I&C309(2026)105425 gives arena-independent NASH bounds; those do not imply
subgame perfection. Its author full text Remark1 distinguishes vertex and
edge memory, and Example34 gives a Buchi control showing why an overgeneral
memory claim is false. CONCUR2025paper12 addresses SPE rational synthesis;
Section4/Remark21 does not directly supply the above universal memory bound.
Source status: open-supported by the original author question and bounded
current primary comparison, not an exhaustive priority claim. Any newer
proof or counterexample must be read and reclassify the question.
