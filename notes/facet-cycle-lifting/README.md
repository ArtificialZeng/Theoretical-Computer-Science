# A limitation of deletion-cycle lifting

This is an obstruction to a proposed proof method. The original graph-associahedron facet-Hamiltonicity question remains unresolved. This note makes no priority claim.

Let H be a connected graph with at least three vertices, and obtain G by
adding a universal vertex v. For a tubing of G, define its deletion projection
by replacing each tube t with the connected components of H[t minus {v}],
discarding empty/full-H sets and duplicates. Consider a proposed induction
which produces a facet-Hamiltonian cycle of G whose projected states all
belong to the vertex set of one facet-Hamiltonian cycle of H. Even allowing
arbitrary order, stutters and repeated laps, this requirement is impossible
when the number of maximal independent sets of H exceeds its number of
proper connected tubes.

Proof. For every maximal independent set I of H, the set {v} union I is a
proper connected tube of G. It is proper since a connected nontrivial H is
not independent. A facet-Hamiltonian cycle of G visits that facet, so at
some visited tubing its deletion projection contains all singleton tubes
{i}, i in I. If two distinct maximal independent sets I,J could be served
by the same projected tubing, I union J would be independent by singleton
compatibility. This contradicts maximality of I and I != J. Thus the
projection visits at least as many distinct H vertices as there are maximal
independent sets. A facet-Hamiltonian cycle of H has exactly as many vertices
as H has proper connected tubes, since no tube is a universal facet. The
claimed obstruction follows. This necessary counting argument does not
require a general deletion-projection theorem.

Take H=P19. Its proper connected tubes are its nonempty intervals other
than the full path: 19*20/2-1=189. Let a_n count maximal independent sets
of P_n. The initial values are a_0=1,a_1=1,a_2=2, and
a_n=a_(n-2)+a_(n-3) for n>=3: either vertex1 is chosen and vertex2 excluded,
or vertex1 is excluded and vertex2 chosen (forcing vertex3 excluded).
These cases leave arbitrary maximal independent sets on the remaining
shorter paths. Hence a_19=200>189. The same strict inequality holds for
every n>=19, by checking n=19,20,21 and using
f_(n-2)+f_(n-3)-f_n=(n*n-9*n+6)/2>0 for n>=9, where
f_n=n(n+1)/2-1.

`facet-projection-MIS-obstruction.json` additionally checks all 524288 masks
of P19 directly for independence and domination, obtaining exactly200
maximal independent sets. It checks all19900 distinct pairs have a
nonindependent union. These are exact finite count checks, not a fresh model
review. The elementary argument above supplies the quantified method scope.

The extension G is a fan, whose facet-Hamiltonian cycle existence is already
known from [Akitaya et al., arXiv:2411.02172v1](https://arxiv.org/abs/2411.02172v1), Theorem 4 / Section 5.5. Thus this
is not an original-conjecture counterexample. It does not invalidate their
Lemma4, which uses a path and additional states rather than requiring all
projected vertices to lie on one base facet-Hamiltonian cycle.


## Reproduce

From the repository root, with Python 3.10+ (standard library only):

```sh
python3 notes/facet-cycle-lifting/verify_facet_projection_mis.py
```
