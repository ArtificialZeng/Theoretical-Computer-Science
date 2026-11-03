# Current primary comparison and a remaining positive structural kernel

Root supporting record, 2026-11-03 UTC. No original resolution, candidate,
innovation claim, or fresh review is asserted. This compares actual primary
content, not a new topic intake.

Primary: Hoppenworth, Saranurak and Wang, *Near-Optimal Fault-Tolerant Strong
Connectivity Preservers*, FOCS 2025, arXiv:2510.02562v1.
https://arxiv.org/html/2510.02562v1
https://arxiv.org/pdf/2510.02562v1
Downloaded PDF SHA256:
706ec470fd7afaa5f8247535cfc966ea23c942d5f9c5998b92d2e67cfc731fbd.
Theorem 1.1 and the Section 2.1 overview were inspected in actual full text.

## Verified scope

Theorem 1.1 preserves the SCC partition after every at-most-k edge fault set.
Its existential bound is O(k 4^k n log n); its polynomial-in-2^k n construction
has O(8^k n log^(5/2) n) edges. The latter justifies the actual algorithmic
size used in the R1 sampled-return-edge reduction. Strong connectivity here
means mutual reachability. The theorem does not preserve every one-way
reachability relation between different resulting SCCs. In a DAG, SCC
preservation alone places no restriction on retaining its directed edges.

Consequently the new theorem does not by itself resolve c049. R1 correctly
adds selected return edges to make a specific original cut edge necessary for
an SCC preserver. Its unproved high-beta remainder must still be counted.

## A positive bound within unbreakable sets

The first sparse-unbreakable-graph argument in Section 2.1 applies more
generally to the critical-edge cut characterization already proved for c049.
This is a routine adaptation of that exact argument, not a new contribution.

Let (G,P) be edge-critical under two edge faults, and let U be a vertex set
such that every directed cut with at most 3 outgoing edges has at most q
vertices of U on one of its two sides. Then

    |E(G[U])| <= 2(q+3)|U|.

Proof. For each e=(u,v) in G[U], criticality supplies a cut A with u in A,
v outside A, and at most 3 outgoing edges. If u has more than q+3
out-neighbors in U, more than q are inside A. If v has more than q+3
in-neighbors in U, more than q are outside A. Both statements together
contradict the stipulated unbreakability. Therefore charge e to u when its
out-degree within U is at most q+3, and otherwise to v, whose in-degree within
U must be at most q+3. Each vertex receives at most q+3 charges in each
role. This proves the inequality without an assumption that G[U] itself is
critical or that witness paths stay within U.

For q=O(sqrt(p)), this pays the desired budget inside every such block.
The missing global step concerns directed edges between the blocks. The HSW
hierarchy controls those edges using mutual connectivity; simply deleting
condensation-DAG edges is invalid for the original directed demand problem.
A proposed extension must count those edges and preserve all original fault
queries, rather than silently reducing to SCCs or induced subgraphs.

## Why a constant-fault universal selector cannot supply that missing step

HSW Lemma 2.3 (proved in Section 6.1 using the single-source preserver)
states: if one root can be made to reach exactly the i-th of r distinct
terminals using at most f edge failures, for every i, then r<=2^f.

Suppose a proposed return-edge gadget has distinct input/output pairs and,
after at most f designated failures for index i, its only surviving
input-to-output relation is input_i to output_i. Attach a new super-source
to every input, and do not fail these new arcs. After the i-th fault set,
the super-source reaches exactly output_i. The cited anti-isolation lemma
gives r<=2^f. Thus a gadget promising this strict global isolation for
unboundedly many demands cannot use a constant number of failures, regardless
of how many auxiliary vertices it adds. This is a known-lemma consequence,
not a lower bound on all possible SCC reductions or on c049 itself.

These facts sharpen which additional structural work is needed. They neither
certify the high-beta degeneracy conjecture nor substitute a weaker original.
