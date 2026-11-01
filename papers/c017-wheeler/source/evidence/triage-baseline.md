# Exact routine checks; no original resolution

Job `c017-wheeler-triage-b86cccc47ffc`, 2026-11-01. These arguments validate
the intake and controls. They are not claimed as new mathematical contributions.

## The literal input-order condition is decidable

For each q, the given transition graph with q as sole accepting state recognizes
I_q. Reversing its edges, exchanging initial/final states, gives an effective
NFA for rev(I_q). Determinize if desired. For two states p,q, compare all pairs
of words in these reversed regular languages using a synchronous padded product:
padding starts only after the corresponding word ends, and a finite comparator
records the first differing letter or a proper-prefix comparison. Intersect
with the pair of regular languages. Emptiness for the accepting comparison
"left >=lex right" holds exactly when every original p-word precedes every
q-word in colex order. Thus p <in q is decidable. Test both directions for
each distinct pair. Nonempty reaching languages give transitivity and exclude
both directions holding. These are finite subset/product/reachability
constructions on regular languages, not unrestricted rational relations.

This procedure follows the frozen definition even if edges enter s or several
input letters enter a single state. In particular, a complete one-state machine
passes this condition vacuously, as in the current primary complement example.
Older graph-recognition hypotheses must not silently replace this test.

## Complete one-state homomorphisms

Let h:Sigma* -> Gamma* be a monoid morphism, with the sole state final. Then
h is piecewise colex monotone iff it is globally weakly nondecreasing.

The reverse implication is immediate. For the forward implication, suppose
u <co v but h(u) >co h(v). Then h is not all-erasing; fix a with h(a) nonempty.
For each suffix z, the cylinder C_z={xz:x in Sigma*} is convex: after reversal
it is the set of words with prefix rev(z). The descending pair uz,vz stays
strictly descending in output, because right concatenation of the same word
preserves colex comparison. Inside that same cylinder,

    z <co az <co a^2 z <co ...

has strictly increasing outputs h(z),h(a)h(z),h(a)^2h(z),..., since these are
successive proper suffix extensions. Hence h is monotone in neither direction
on C_z. For at least two distinct input letters b,c, the suffixes z_j=bc^j,
j>=0, are pairwise suffix-incomparable, giving infinitely many pairwise
disjoint convex cylinders. A partition into k ordered convex pieces can split
at most k-1 such disjoint cylinders. Each cylinder would have to be split, a
contradiction. For unary input, all outputs are powers of a fixed word and
already nondecreasing; the empty-alphabet case is trivial.

This also explains effective checking of this restricted baseline. Reverse
all words and define the morphism g(a)=rev(h(a)), so
g(rev(w))=rev(h(w)). Put H=g(Sigma*), an effectively regular language. A
proper-prefix input pair never decreases under g. Every other lex comparison
has a common prefix followed by distinct letters a<b; cancelling the common
output prefix reduces the check to whether every word in g(a)H is <=lex every
word in g(b)H. A regular-language padded comparator as above decides this for
each letter pair, including erasing images. This establishes only the morphism
case, not arbitrary state-dependent transducers.

## Infinite controls, rather than extrapolated finite tests

Identity and all-erasing maps are weakly nondecreasing. The variable-length
code h(0)=0,h(1)=11 is also nondecreasing: the two reversed codewords are
prefix-incomparable and correctly ordered, and proper-prefix comparisons stay
prefix comparisons. Thus all three have one monotone piece.

Complement has a descending pair 0<1 with outputs 1>0. Length-only coding
h(0)=h(1)=0 has the descending pair 00<co 1, with outputs 00>co 0.
The preceding exact cylinder argument proves that these two complete
homomorphisms have no finite monotone convex partition. This agrees with the
primary complement example. It does not generalize to arbitrary states.

Existing `intake/pretest-results.json` reports finite controls only (length
at most 10 and 1092 DP checks); they were inspected and preserved without
rerunning or extending the finite-length search. No new computational coverage
is claimed in this triage.
