# Research pass 2: deciding equivalent Wheeler realizability

Job: `c017-wheeler-research-98a17f8eb2fd`; 2026-11-01. Research evidence,
not a manuscript or a fresh referee report. This is an explicit strengthened
claim generation. The original membership theorem, its immutable question,
and every old frozen evidence file remain unchanged. The combined scope below requires
a new freeze and a new actual correctness, novelty and significance review.

## Statement and dependencies

**Theorem.** In the precise finite trimmed deterministic subsequential model
of `source.md` and `problem.md`, equivalent Wheeler realizability is decidable.
On YES an equivalent finite Wheeler transducer over the same ordered alphabets
is effectively constructible. Empty transition outputs, partial transitions,
arbitrary terminal words and the prohibition on an initial output are respected.
The input domain is nonempty as follows from trimming in this model. A supplied
empty partial function, if admitted under a different encoding convention,
is a separate directly decidable degenerate case, not a premise used here.

The only nonstandard dependency is the complete original-scope membership
algorithm in `evidence/research-1-resolution.md`. That theorem, including its
O(S^13) bound for explicitly encoded machine membership and its disjoint-turn
certificates, is incorporated unchanged. No complexity bound is claimed for
the present realizability construction. It is not a minimization algorithm.

Classical onward normalization, residual merging, effective finite-automaton
Boolean operations/projection, and shortlex representatives of automatic
equivalences are standard ingredients, not new contributions. The separate
literature note records their primary sources. The substantive new core of
the combined claim remains the membership SCC criterion. The new consequence
connects that criterion to the related Section 4 realizability question without
assuming a finite convex refinement of the supplied, possibly redundant machine.
No source quotient theorem is needed as a correctness premise.

## 1. Exact normalization and canonical residual colors

Let T have state set Q, initial s, partial transitions p --a/w--> r, final
states F and terminal words t(p). Let f be its partial function and let
D=Pref(dom f). Trimming gives exactly D as the set of defined paths from s.
Write O_p(v) for the output on the path from p reading v followed by its
terminal output, when this continuation is accepted. Every O_p has nonempty
domain. Put

    lambda_p = LCP { O_p(v) : v in dom O_p }.

This is effectively a finite word: forgetting the input labels gives a finite
word-labeled output NFA with terminal paths. Find any accepted output y; among
its finitely many prefixes, test the longest one z such that the regular range
is contained in z Gamma*. This uses only regular-language inclusion and
computes lambda_p, including the empty-word case. The selected y is an upper
bound on prefix length, not an input-depth bound on the function.

For a defined edge p --a/w--> r, lambda_p is a prefix of w lambda_r. Indeed
lambda_p is a prefix of all words w O_r(v), whose LCP is w lambda_r. Likewise
lambda_p is a prefix of t(p) at a final p. Form the normalized machine N:

    edge output n(p,a) = lambda_p^(-1) (w lambda_r),
    terminal n_t(p)    = lambda_p^(-1) t(p).

Here prefix cancellation is literal deletion of a verified prefix. Induction
on continuation length gives the normalized residual function

    g_p(v) = lambda_p^(-1) O_p(v),

on exactly dom O_p. In particular the LCP of range(g_p) is epsilon.

Two normalized states have equal g-functions exactly when they lie in the
greatest finite relation requiring equal final flags and normalized terminals,
equal defined input letters, equal normalized edge words on each such letter,
and related successor states. To prove the nontrivial direction, if g_p=g_q,
then their continuation domains agree. Since all successors are coaccessible,
a letter is a defined edge precisely when that domain contains a word beginning
with the letter. The LCP of the g_p-outputs on a-beginning inputs is exactly
n(p,a), because the normalized target has LCP epsilon. Thus these edge words
agree. Left cancellation gives equality of successor residual functions.
Conversely any relation satisfying these finite conditions implies equality
on each finite continuation by induction. Iterative finite partition refinement
therefore computes exactly equality of normalized residuals; let [p] denote
the resulting class. There is no unproved finite search for function equivalence.

## 2. A canonical machine with no initial output

Construct a new initial state e, distinct from all classes [p], with no incoming
edge. It has terminal f(epsilon) exactly when epsilon is in dom f. For each
defined first edge s --a/w--> r of T, set

    e --a/(w lambda_r)--> [r].

All other edges and terminal words are the normalized quotient's. Remove
unreachable normalized classes after creating e. Call this machine C. It is
finite, deterministic and trimmed, and its initial output is absent.
Telescoping the normalization identity proves that C computes f on exactly
dom f. In particular, for every nonempty u in D, its accumulated output is

    A_C(u) = A_T(u) lambda_delta(s,u)
           = H(u) := LCP { f(uv) : uv in dom f }.                 (1)

At epsilon its accumulated output is epsilon, regardless of H(epsilon).
The new state's terminal word, when present, preserves the original value
f(epsilon). Thus a nonempty H(epsilon) is not silently installed as a forbidden
initial output. Even if the old initial state lies on cycles, all its nonempty
returns use normalized classes, not e.

For nonempty u, the C-state is exactly the normalized continuation

    R_u(v) = H(u)^(-1) f(uv),   dom R_u = u^(-1) dom f.

Indeed (1) identifies this function with g_delta(s,u), and Section 1 merges
exactly equal g-functions. Color epsilon by e and every other u by its C-state.
This is the canonical coloring used below; it is not the coloring of T's
unmerged states.

For ANY trimmed transducer W computing f, let J_p be its reaching language,
A_W(u) its accumulated output, and lambda'_p its residual-output LCP. Then

    H(u) = A_W(u) lambda'_p,    u in J_p,                         (2)

including epsilon as an identity for H (not as C's accumulated output there).
The statewise identity (2) and its colex monotonicity transfer are already
explicit in the source's Section 3.2, Remark 3; they are not claimed as new.
Consequently, for nonempty u in J_p the normalized continuation R_u is the
same function (lambda'_p)^(-1) O'_p at every such u. Thus each J_p minus
epsilon has a single canonical color. This proves the needed necessity even
when T contains redundant states or W uses a different output timing.

## 3. Effective maximal convex components

On D define E(u,v) by equal canonical color and the absence of a different-color
word z in D strictly between u and v in colex (in either endpoint direction).
Its classes are exactly the maximal convex components of the color classes.
For example, transitivity follows since the interval between two outer points
is contained in the union of the two intervals to a common point. Each E-class
is convex, and any convex monochromatic set meeting it is contained in it.

Encode every word by reversal; colex is then ordinary lex with a proper prefix
first. Each color language is regular: it is the reversal of a reaching
language of C. Equality, lex order, shortlex order and these finitely many
color predicates are synchronous regular on right-padded word tuples. For
lex order a finite comparator remembers the first unequal letter, treating
end-of-word as smaller than a genuine letter. For shortlex it first compares
the two lengths and, on equal lengths, the lex comparator. A finite ended bit
per track forbids genuine letters after padding.

Here is the precise effective closure needed; it does not assume closure of
arbitrary rational relations under intersection. Use convolutions allowing
trailing all-padding columns. Boolean operations on deterministic automata are
relative to the regular universe of valid padded tuples. To existentially
remove a track, nondeterministically guess its letter or padding in each
column, enforcing that track's ended bit. Project column labels, then
determinize. A witness can outlast every free word, so one must also allow a
suffix consisting entirely of padding on the free tracks. Take the regular
right quotient by all-padding*: equivalently mark a state final when a finite
all-padding path reaches a former final state. This has no length cap and
handles an empty free word. The resulting predicate is again padding-invariant.
Products/intersection, relative complement and this projection implement
each quantifier below exactly.

In particular the ternary relation

    z in D, color(z) != color(u),
    (u <co z <co v or v <co z <co u)

is synchronous regular. Existentially project z, complement, and intersect
with equal-color endpoints in D. This computes E. Define

    Rep(u) iff u in D and there is no v in D with E(u,v)
               and rev(v) shortlex-smaller than rev(u).           (3)

Applying the same operations computes its regular language. Shortlex over
finite words on a finite alphabet is a well-order, so (3) chooses exactly one
word from every E-class, even when the class has no least colex element.

A finite automaton decides whether Rep is finite: restrict to states both
reachable and able to reach a final state, and check for a directed cycle
carrying genuine letters. If finite, enumerate its words by traversing this
acyclic useful graph. Thus finiteness of the canonical convex refinement is
decided without an inferred template or state bound. Fixing a representative
in E and projecting the other coordinate gives that component as an effective
regular language if it is needed explicitly. If Rep is infinite, no finite
convex refinement of the coloring exists, since every monochromatic convex
piece lies inside a single E-class.

## 4. Right invariance and construction of the finite split

Suppose u E v. Their C-states agree, so for each letter a, ua is in D exactly
when va is in D. If defined, they have the same successor C-color. Suppose
u <co v; the reverse case is symmetric, and equality is immediate. Every
word z in D between ua and va ends in a: the entire suffix cylinder Sigma* a
is colex convex. Write z=wa. Prefix closure gives w in D, and cancellation of
the common last letter gives u <co w <co v. Hence w has u's color; determinism
then gives z the common successor color. Therefore ua E va. This proves
right invariance, including partial definedness. The epsilon class is a
singleton because the new initial color is unique.

When Rep is finite, form C_c with one state for every E-class and initial
state [epsilon]_E. For a chosen representative u of a component, inherit C's
defined a-edge, its output word and the component containing ua. Find that
target by testing E(ua,r) against the finite representative list; precisely
one matches. Inherit finality and terminal word from C's color. All choices
are independent of the representative: E refines C-colors, and the preceding
right-invariance proof makes the successor class constant.

Induction on input length proves that the state reached in C_c by w in D
is [w]_E, with exactly the accumulated output of C. Every undefined edge
agrees with C. The terminal output agrees too, so C_c computes exactly f.
Each component is nonempty and accessible. Each of its words has an accepted
continuation (because T is trimmed), which also runs in C_c; thus the split
is trimmed. Its reaching languages are exactly the convex components, so
they are totally separated in colex. No additional input-consistency or
initial-indegree convention has been imported into the literal source model.

## 5. Necessity from an arbitrary Wheeler realization

Suppose a finite Wheeler W computes f. Its reaching sets J_p are convex in
D: any intervening different state contradicts their pairwise total
separation. By Section 2, each J_p minus epsilon is canonically monochromatic.
Removing epsilon preserves convexity because epsilon is the least word in
D. Add it as a singleton. This is a finite convex refinement of the canonical
coloring, so Section 3's Rep language must be finite.

Now transfer the output property. Appending the same fixed word on the RIGHT
preserves and reflects every colex comparison: after reversal it is a common
left prefix, which cancels even for strict comparisons and empty words.
Equation (2) therefore transfers every weakly increasing or decreasing piece
of A_W on J_p minus epsilon to H on the same piece. Since there are finitely
many W-states and finitely many pieces at each, these pieces form a finite
convex piecewise-monotone partition of D minus epsilon. Add the singleton
epsilon with accumulated C-output epsilon. By (1), this is a finite convex
piecewise-monotone partition of A_C on all D. Intersect this partition with
each convex E-class: the nonempty intersections are finitely many convex
monotone pieces for C_c's accumulated output at that state. Its input order
was already proved in Section 4. Hence C_c is itself Wheeler.

## 6. Algorithm and both directions

1. Normalize, merge equal residuals, and construct C as in Sections 1-2.
2. Construct E and the regular representative language Rep; decide finiteness.
   If infinite, answer NO.
3. If finite, enumerate Rep, construct C_c, and run the full membership
   algorithm of research-1-resolution.md on C_c.
4. Answer YES exactly if that membership test accepts, returning C_c on YES.

All steps terminate. Step 2's NO is sound by the first part of Section 5.
Step 3's NO is sound by the rest of that section: every Wheeler realization
would force C_c to pass. A YES is sound because C_c is equivalent to f and
passes the exact class test. These arguments also prove completeness. No
statement is inferred from a finite input prefix, timeout or missing solver.

## 7. Adverse tests, known ingredients and limits

`research-2-check-realizability.py` implements onward merging, the automatic
ternary intervening-color relation, existential projection with padding
closure, E, shortlex representatives, exact regular-language finiteness,
the component transducer and the existing membership prototype. Its report
`research-2-realizability-check.json` is reproducible by running that script.

Thirteen named boundary controls and twenty held-out complete finite domains
pass. Constant-output unary parity states merge and yield a realization;
the unmerged parity shortcut has an exactly infinite representative language.
The source's unary floor-length function and a partial-terminal parity domain
also give exactly infinite representative languages after canonical merging.
The initial-cycle function f(a^n)=0^(n+1) has lambda_s=0, correctly retains
f(epsilon)=0, and emits 00 on its first edge in C_c without an initial output.
Binary identity and erasure pass; complement and length coding fail membership
despite finite canonical component languages. A finite domain requires five
convex components from three canonical states, checking that splitting is
actually performed. Empty input alphabet, a domain consisting only of epsilon,
partial terminal domains and variable terminal words are covered. Output
comparisons use precisely the literal source model.

The automatic projection explicitly passes an empty free word with a longer
existential witness. Trailing padding invariance is checked on relation calls.
For the complete finite domains every pair is compared to direct maximal
same-color runs, and the ENTIRE representative language is compared to the
independently computed shortest representatives. Direct infinite-control
input/output replays are bounded through length 7 and are only supplementary
finite evidence. The general theorem is the argument above, not these tests.

The root proposal supplied the route and normalization controls. The present
pass adds a self-contained completion, exact automatic quotient implementation,
the held-out relation tests and a current primary comparison. It introduces
no further conjectures, no complexity/minimality assertion for realizability,
and no independent publication for a routine normalization corollary. No
mathematical gap is presently identified by this researcher. That assessment
is a request for fresh scrutiny, not an acceptance or truth certificate.
