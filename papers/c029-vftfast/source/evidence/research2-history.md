# Valid geodesic histories do not by themselves remove the separator barrier

Job c029-vftfast-research-36ff17e1eeb1. Method diagnosis only; no original
construction hardness, novelty claim, independent audit or manuscript.

## Exact new lemma and proof

Take any loopless multigraph on a core vertex set, subdividing each edge into
a private-internal-vertex path of length L>d. Distinct parallel edges have
disjoint internal vertices. Call the resulting simple graph H. Let G contain
H and any additional edges between core vertices. Then H is the union of a
polynomially explicit sequence of length-d paths P_i with singleton witnesses
F_i disjoint from P_i, such that

    dist_(G-F_i)(endpoints(P_i))=d,
    dist_(H_i-F_i)(endpoints(P_i))=infinity,
    H_i=union_(j<i) P_j.

This holds for every radius r>=d, and every budget f>=1.

Process subdivided edges one at a time. Orient a chain v_0=a,...,v_L=b.
Use length-d windows starting at 0,d,2d,... while their starts are <=L-d;
if necessary append one final window starting at L-d. There are ceil(L/d)
windows; their union covers the chain. Before the final window the installed
chain edges are a prefix and b is not yet reached. For every nonfinal window
use F_i={b}. Its far endpoint is a new internal vertex, isolated in H_i.
In G-b, all chain internal vertices lie on a pendant chain attached only at a;
there is no alternative simple route between the window endpoints. Thus its
G-b distance is exactly d. For the final window use F_i={a}. Since L>d, it
avoids a. In H_i-a its initial vertex belongs to the isolated installed prefix,
which is disconnected from b. In G-a the relevant chain is pendant at b, so
again the endpoint distance is d. Previous completed chains and arbitrary
ambient core shortcuts do not affect either argument. Each window adds at
least one edge. This proves the lemma, with total construction time polynomial
in the explicit subdivided graph size.

Apply it to every short and backup bundle of the root separator reduction.
All lengths are >d, all internal vertices are private, and the extra spine
edges join core vertices. Hence the H used in that reduction comes with an
explicit valid insertion history, even with geodesic singleton witnesses.
Combining this with the root's all-endpoint soundness/completeness argument
extends that conditional separator barrier to algorithms supplied with such
a valid adaptive history. It still does NOT establish that H is a prefix of
the exact source's fully prescribed grouped scan; earlier scans might insert
spine edges. It does not exclude a constructor that enforces a stronger
path-selection discipline or preprocesses sparse regions. There is no reverse
reduction to the full original spanner construction.

The root reduction was read critically: a length-d path cannot traverse a
complete H bundle, so any non-H output has at most two partial bundles and
a nonempty spine subpath. Its attachment pair other than xy is neutralized
by a surviving backup of length r-d, because the partial lengths sum to at
most d-1. Attachment pair xy forces the entire monotone spine. A forbidden
A-B pair then yields B+1 internally disjoint protected-terminal routes of
length 3(d+1)<=r. Conversely a clique deletes all unselected core choices;
no <=d route traverses a bundle, and no <=r route can use a backup plus even
one short bundle. These checks support the method argument, not a fresh
referee verdict. Original status stays unresolved.

## New finite evidence (not a rerun of supplied exhaustive diagnostics)

research2_history_checks.py verifies the constructed history directly with
unweighted BFS in both G-F_i and H_i-F_i before EVERY insertion. Its boundary
suite uses d=1..8, L=d+1..3d+2, repeated chains and complete ambient core
shortcuts. It also builds the two full expanded root graphs with 45,854 and
42,934 vertices and all 73 paths per bundle. Total: 24,982 insertions,
49,964 exact BFS checks, zero failures. These are tests of the NEW history
lemma; no arbitrary-fault enumeration or full construction test is claimed.

## Positive redirection

The generic F(d)poly(n,f) separator is stronger than necessary. The actual
positive route in research2-positive-kernel.md accepts f^O(d) work only below
a threshold, and uses known multiplicative spanners above it. This avoids
the parameterized barrier rather than inferring original impossibility.
