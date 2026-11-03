# A direct positive cover of all three-connected-demand critical edges

Root supporting proof, 2026-11-03 UTC. This is a routine application of the
path-frequency construction in Chakraborty--Choudhary ICALP2020 Section4.2
and the known single-source two-fault reachability preserver. It is not an
innovation claim or a complete resolution of c049. It can simplify the
flow-based program, whose additional sharing potential is not needed here.

Work in the edge-fault kernel; mixed vertex/edge faults are subsequently
handled by the already proved vertex-splitting reduction. For a digraph G and
its p distinct nonreflexive reachable demands, let P3 contain those demands
with at least three edge-disjoint source-to-target paths. Its size is q<=p.
If q=0 no construction is needed. Otherwise set h=ceil(sqrt(q)).

For each demand in P3, find three edge-disjoint simple directed paths by a
paid capped unit-capacity maxflow computation. There are exactly 3q paths in
the resulting indexed collection; coincident paths of different commodities
remain separately indexed. Repeatedly choose any vertex on at least h
remaining paths, add it to a set W, and remove every path containing it.
There are at most 3q/h selected vertices, since removed path indices are
never counted again. Include in H the remaining paths, and, for every root
in W, a known O(n)-edge two-fault single-source reachability preserver and
its reverse-graph single-target counterpart. All included edges are input
edges and all computations have polynomial work for fixed fault count.

The remaining path union has at most n(h-1) edges: each vertex is on fewer
than h remaining simple paths and consequently has fewer than h incoming
edges in that union. The root preservers add O(nq/h) edges. Hence

    |E(H)| = O(n(h+q/h)) = O(n+n sqrt(q)).

For any original fault set F of at most two edges and any demand in P3,
one of its three edge-disjoint chosen paths avoids F. If this path remains,
it is present in H-F. Otherwise it was removed at a selected root on that
same surviving path. Both its source-to-root prefix and root-to-target
suffix survive in G-F, so the two root preservers supply a source-to-target
walk in H-F. A path follows by removing cycles. False reachability cannot
be introduced because H is a subgraph. This proves the complete P3
two-fault guarantee, without any coordinate-optimal flow assumption.

Now suppose (G,P) is edge-critical for the full original P. Let E3 be all
edges having at least one criticality witness whose demand belongs to P3.
Every such edge lies in H: if e were omitted, the preserved route for its
demand under its witnessing fault set would be a route in G-F-e, contrary
to criticality. Therefore

    |E3| = O(n+n sqrt(p)).

This statement does NOT say that all edges in a chosen flow union are
critical, or that every other critical edge has zero flow load. It says
that a complete two-fault cover for three-connected demands already pays
the desired budget for every edge they can force. Any remaining critical
edge must have every witnessing demand of maximum flow one or two.

Together with the independently proved low-beta return-edge cover, a
sufficient remaining global theorem is a bound of tilde-O(n+n sqrt(p))
on the edges which have NO three-connected witnessing demand and for
which beta(e)>ceil(sqrt(p)). This is still unproved. The published layered
chain and induced-matching selector obstructions lie in the deficient-flow
regime and are not dismissed by this reduction. The original problem and
all accumulated research limits remain unchanged; no PDF is justified.
