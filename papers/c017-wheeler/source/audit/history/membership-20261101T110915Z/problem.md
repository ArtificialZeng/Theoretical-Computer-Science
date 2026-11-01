# Precise target: current-v3 Wheeler-transducer membership

Job: `c017-wheeler-triage-6041b64a3bbb`; phase: triage recovery; 2026-11-01.
Prior triage job timed out operationally; its records are retained without
retroactive completion. No research pass has been used.
The immutable statement is `source.md`, SHA-256
`40fc8e967aeefd233cb62ffd0f70d77e772fafbdeb6086724c4c2ab5f591106d`.

## Input, orders, and quantifiers

An input is a finite explicitly encoded trimmed deterministic one-way
subsequential transducer T=(Q,s,Sigma,Gamma,delta,omega,F,t). Both finite
alphabets have given total orders, which are part of the instance. The partial
map delta:Q x Sigma -> Q has no epsilon-input transitions; omega has exactly
the same domain and assigns arbitrary finite output words, including epsilon.
The terminal map t:F -> Gamma* is explicit. Every state is accessible from s
and can reach F. Empty-domain/empty-alphabet degeneracies are handled directly.
Undefined transitions are absent; no extra rejecting sink is silently added.

Write rev(w) for reversal. For input or output words, u <co v means
rev(u) <lex rev(v), with a proper prefix smaller in lex order. Thus a proper
suffix is smaller in colex order. Let

* D={w:delta(s,w) is defined}; trimming gives D=Pref(dom(||T||));
* I_q={w in D:delta(s,w)=q};
* f_q(w)=omega(s,w), obtained by concatenating transition outputs along w.

For distinct p,q, define p <in q iff EVERY u in I_p and v in I_q satisfy
u <co v. The first membership condition is that for every distinct p,q,
either p <in q or q <in p. Accessibility makes these reaching languages
nonempty, so this is a strict total state order.

The second condition is: for EVERY q there EXIST a positive integer k_q,
nonempty disjoint sets C_(q,1),...,C_(q,k_q) partitioning I_q, and an orientation
e_(q,i) in {+,-} for EACH piece, such that:

1. each C_(q,i) is convex RELATIVE TO I_q: if u,v are in it and
   u <co w <co v with w in I_q, then w is in it;
2. for all u <co v in this piece, f_q(u) <=co f_q(v) when e=+, and
   f_q(u) >=co f_q(v) when e=-.

There is no given bound on k_q and no assumption that the pieces or their
endpoints are regular or finitely presented. Different states and pieces may
have different orientations. Test f_q, without terminal outputs t. These are
Definitions 4 and 5 of the v3 primary paper (printed p.6), using Section 2.1.

## Full original question

Does there exist an effective algorithm that halts on EVERY such finite input
and answers yes exactly when BOTH conditions hold? A complete positive answer
needs a terminating algorithm and its correctness proof, including erasing
outputs and all states. A complete negative answer needs an undecidability
reduction respecting this model. Optimal complexity, semantic realizability by
another machine, and minimization are separate questions. A subclass decision
or a finite negative search does not answer this question.

## Prior work and proposed delta

Nearest source: G. D'Agostino and A. Paradiso, *Finite-State Transducers in the
Wheeler Setting*, arXiv:2606.29405v3, 2026-08-13,
<https://arxiv.org/pdf/2606.29405v3>, Definitions 4/5 p.6, Section 4 p.16.
The current arXiv version and explicit unresolved-membership statement were
rechecked on 2026-11-01. Status: **open-supported**, bounded by the sources
and searches documented in `evidence/triage-literature.md`.

Input order alone is effectively decidable by comparing reversed regular
reaching languages; see `evidence/triage-baseline.md`. Existing Wheeler DFA
and Wheeler-language algorithms address input structure, not the unbounded
number of output-monotonicity pieces. Classical graph definitions can additionally
require an initial state without incoming edges and input consistency. The
frozen v3 reaching-language definition must be followed literally; its own
one-state example is relevant. Do not transfer a graph theorem without checking
its hypotheses.

Proposed substantive delta: a complete membership algorithm (or a valid
undecidability proof) for arbitrary state-dependent erasing outputs. Verification
route: first settle a precise bounded pumping criterion for disjoint strict-turn
witnesses, then prove all required effective comparison/limitedness steps.
This is plausible payoff, not an established algorithm or contribution.
The exact first-test hypothesis is in `evidence/first-test.md`.
Auxiliary supervisor input now supplies a fixed-certificate Presburger
verification reduction (`intake/wheeler-fixed-certificate-verification.md`)
and an off-diagonal pair-component lemma (`intake/wheeler-pair-components.md`).
These are supporting inputs, without a fresh referee or novelty verdict.
The remaining first-test target is necessity plus a computable template bound;
the fixed-certificate verification gap in the old first-test note is superseded
by that auxiliary reduction, subject to checking its proof. Neither auxiliary
input decides membership or licenses narrowing the original question.

Publication policy: only a substantively new full original-scope resolution
may become a candidate. This triage creates no manuscript, PDF, or acceptance.

## Research pass 1 proposed resolution (awaiting fresh review)

Job `c017-wheeler-research-8ca2b0cef7a6` supplies a complete proposed membership
algorithm in `evidence/research-1-resolution.md`. The original reading above is
unchanged. Immediate incoming-transition blocks are convex; common output
right-concatenation preserves comparisons. Global monotonicity is decided by
regular-range seeds and input-graph reachability. Branching SCCs require global
monotonicity; simple cycles reduce to two adjacent-annular-copy tests and at
most two convex monotone pieces. Acyclic states inherit finite partitions.
The proof supplies single-pump necessity and a total computable template bound.
The conservative explicit implementation bound is O(S^13) bit operations.
This is a researcher proposal of full resolution, not a referee verdict,
acceptance, external peer review or a license to create a manuscript.
Current literature was rechecked in `evidence/research-1-literature.md`; no
inspected equivalent resolution was found within that bounded search.
