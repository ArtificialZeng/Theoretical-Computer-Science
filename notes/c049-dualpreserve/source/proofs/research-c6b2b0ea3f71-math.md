# Research 2: the high-beta degeneracy route fails

Job `c049-dualpreserve-research-c6b2b0ea3f71`, assigned pass 2/3.
These are mathematical research records, not an accepted contribution or a
manuscript. The immutable source is unresolved. No novelty is certified.

## 1. Screening the actual 2020 lift

Suppose an undirected simple graph is the union of q edge-disjoint unique
shortest paths. Two distinct paths meet in at most one vertex: two common
vertices would have the same unique shortest subpath, contradicting edge
disjointness. Consider an induced h-vertex subgraph of minimum degree d>0,
and let a_i count its vertices on path i. Set S=sum a_i. Each vertex belongs
to at least d/2 paths, so S>=hd/2. No vertex pair belongs to two paths, hence
sum a_i(a_i-1)<=h(h-1). Cauchy gives S^2<=q(h(h-1)+S). Since x^2/(h(h-1)+x)
is increasing for x>0 and d<=h-1,

    q >= (hd/2)^2/(h(h-1)+hd/2) >= d^2/6.

Thus degeneracy is at most sqrt(6q). In ICALP2020 Section5 remove the private
terminals and side chains first, each with remaining degree at most3.
For central temporal copies, use the base degeneracy order, placing all
copies of a base vertex together. A central vertex then has at most twice
the base forward-neighbor count. The whole actual lift, with arbitrary K,
has degeneracy at most max(3,2 sqrt(6q)). Every edge subset, including its
high-beta subset, inherits this bound. This is a structural screening result,
not a proof of the proposed bound for arbitrary critical graphs.

## 2. An induced-matching selector with a dense compulsory core

Let B=(U,W,E_B) be a D-regular bipartite graph with |U|=|W|=t, whose edges
partition into t nonempty induced matchings M_i, each of size D. Order each
matching as (u_i,k,w_i,k), 1<=k<=D. Orient every core edge U->W.
For matching i create private vertices a_i,1,...,a_i,D and b_i,1,...,b_i,D,
with directed consecutive-chain edges. Add a_i,k->u_i,k and w_i,k->b_i,k.
Put s_i=a_i,1 and t_i=b_i,D. Concatenate all a-blocks in matching order:
a_i,D->a_i+1,1; connect the last block to a new hub h, and add h->t_j for
all j. Everything is simple and acyclic. There are

    n=2t+2tD+1 vertices and m=5tD edges.

All t^2 source-target pairs (s_i,t_j) are reachable, by the concatenated
left chain and hub. For any core edge in M_i at position k, fail the edge
immediately following a_i,k on that concatenated chain, and also fail
b_i,k-1->b_i,k if k>1. These are at most two edges. The surviving route
from s_i to t_i can enter the core only through matching positions <=k,
and leave it for target t_i only through positions >=k. Since M_i is
induced, the only possible core crossing is its kth edge. No W vertex
returns to any left block or core U vertex. Thus there is a UNIQUE surviving
s_i-to-t_i path, and that core edge is compulsory.

Moreover all private source prefixes and target suffixes are compulsory:
the witness for the last matching edge contains every private left-chain
edge, and the witness for the first contains every private right-chain
edge. Every attachment is also on its edge's unique witness path. The
connectors and hub edges need not be compulsory.

## 3. Forcing high beta using reachable demands only

Recall beta(e) is the minimum number of reverse demands across ANY valid
active outgoing cut of size at most3 witnessing e. We will lower-bound
reverse demands for EVERY outgoing cut of size<=3 containing any core edge;
therefore the internal-route requirement cannot weaken this conclusion.

Let A contain u and exclude w for a core edge (u,w). If D>=4, some neighbor
x of w lies outside A, because at most3 core edges leave A. Each of the D
matchings incident to x supplies a private s_i-to-x prefix. These D paths
are edge-disjoint (they share only x). At most3 of their sources can lie in
A. Hence at least D-3 original sources lie outside A. Similarly some
neighbor y of u lies inside A. Its D private y-to-t_j suffixes are
edge-disjoint, so at least D-3 original targets lie inside A.

Put k=D-3. Suppose k^2>=32t. Choose each source-target pair independently
with probability rho=32t/k^2, obtaining Q. For fixed sets S,T of at least
k source and target indices, the number of Q edges in S times T has mean
at least32t. Chernoff gives probability at most exp(-4t) that it is below
16t. There are at most4^t choices of (S,T), so the chance ANY such pair
fails is at most exp((ln4-4)t)<1/2 for t>=1. Markov bounds the chance
|Q|>64t^3/k^2 by at most1/2. Their sum is strictly less1; therefore a
simple set Q exists with BOTH properties. Add all original diagonal pairs,
and call this demand set P. Then

    p <= t+64t^3/k^2 <=65t^3/k^2,
    beta(e) >=16t for EVERY compulsory core edge.

All these demands are reachable. This does not use unreachable padding.
If desired, apply paid greedy deletion to obtain an edge-critical graph H
for P. Every core edge, private prefix, private suffix and attachment remains
because each lies on a unique original witness path. Original reachability
and all fault queries for P remain preserved. The same disjoint-prefix and
suffix proof applies to every small cut in H. Hence the beta lower bound
holds in H itself, not only in a graph with disposable connectors.

## 4. A fully specified asymptotic base, without an unproved density premise

Fix dimension16 and an integer b tending to infinity. Among vectors in
{0,...,b-1}^16, choose a largest squared-norm sphere. It contains

    D >= b^16/(16(b-1)^2+1)

vectors. Encode the vectors in base2b to obtain A subset [0,(2b)^16).
There is no nontrivial integer 3-term progression in A: digit sums have no
carry; a midpoint in the same sphere forces equal endpoint vectors by
strict convexity of squared norm. Put t=2(2b)^16+1, an odd modulus. The
same assertion holds modulo t since |a+a'-2a''|<t.

Take U=W=Z_t and put an edge x->y exactly when y-x belongs to A modulo t.
This is D-regular. Color by z=x+y modulo t. For every color and every
a in A there is exactly one edge, since2 is invertible modulo t. Each
color is a matching. If two distinct edges of a color had a cross edge,
their differences a,a' and the cross difference c would satisfy
2c=a+a' modulo t. Progression-freeness forces a=a'=c and the two edges
to coincide. Thus the color classes are induced matchings of size D.
This is the standard progression-free/induced-matching mechanism; no
priority claim is made for that mechanism or the selector application.

Here D=Omega(t^(7/8)) and D<=t. For all sufficiently large b the sampling
condition holds, and the construction of Sections2--3 satisfies

    p=O(t^(5/4)),  sqrt(p)=O(t^(5/8)),
    beta(e)>=16t>ceil(sqrt(p)),
    degeneracy(B)=D=Omega(t^(7/8)).

Consequently the high-beta graph has degeneracy/sqrt(p)=Omega(t^(1/4)),
which also exceeds every fixed polylog(n), as n<=3t^2 for large t.
This refutes the proposed high-beta O(sqrt(p)) degeneracy assertion, even
for edge-critical acyclic graphs with every demand originally reachable.
It does NOT refute the immutable source: m=5tD=O(n) before pruning.
The dense core is paid for by the many private selector vertices.

## 5. Evidence, status, and surviving issue

The exact finite checker uses three declared sphere bases, tests every core
edge's <=2-edge failure witness and the unique surviving selector path,
checks every original source-target combination, and checks the source/target
counts on each witness cut. These finite checks support the implementation;
the infinite obstruction is the argument above, not extrapolation.
Results and coverage are in core-results.json. The dimension16 construction
and probabilistic terminal expansion are proved analytically, not enumerated.

The genuinely unresolved original kernel remains a GLOBAL total-edge bound
for every edge-critical graph. A hereditary/induced-core degree argument is
now ruled out; an argument may charge core edges to vertices outside that
core, as this construction demands. No full algorithm or disproof is known
here. No candidate, innovation acceptance, referee verdict or PDF is justified.

## 6. One concrete non-hereditary next test (unproved)

A replacement SUFFICIENT assertion, not an equivalence or a resolution:
for every edge-critical (G,P) with p>=1, the undirected multigraph with one
edge for each directed input edge has an orientation whose indegrees a_v obey

    min_orientation sum_v a_v^2 = O(n(p+1) polylog(n+2)).              (ENERGY)

Then m=sum a_v and Cauchy gives m^2<=n sum a_v^2, yielding the original
edge-count scale. The paid deletion and mixed-fault splitting reductions
already recorded would finish the algorithmic target if ENERGY were proved.
An orientation is an analysis certificate; its edges need not follow G's
original directions. Antiparallel input edges count separately.

Unlike degeneracy, ENERGY charges the whole ambient vertex set. The selector
above is consistent with ENERGY even BEFORE extra Q demands: orient as the
original DAG. Core vertices have indegree D, private/hub vertices have
indegree at most3. Hence its energy is at most2tD^2+9(2tD+1)=O(nt), with
t original matching demands. Deleting edges cannot increase that certificate's
energy. The 2022 r-chain family also has energy O(nr^2)=O(np) in its
original orientation. The actual 2020 lift admits an orientation with
indegree O(sqrt(p)+1) by Section1, so has energy O(n(p+1)). These are
analytical family screens, not a proof in general or evidence of novelty.

Next pass's decisive test: minimize this exact integer quadratic orientation
energy on critical graphs by a min-cost assignment (each input edge chooses
one endpoint, marginal load costs1,3,5,...), verify small optima independently,
and attack a global O(n(p+1)) or polylog bound using active <=3-edge cuts.
Try to refute it with a compulsory dense core whose selector vertices are
shared, rather than private. A family with energy/(n(p+1)) growing faster
than every polylog kills ENERGY without disproving source.md. Passing finite
checks is insufficient. This is one explicit changed sufficient route for
the final available pass, not a reset, candidate, or publication endpoint.
