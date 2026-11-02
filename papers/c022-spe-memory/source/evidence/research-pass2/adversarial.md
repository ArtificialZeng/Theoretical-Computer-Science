# Adverse checks of the revised scope

Job `c022-spe-memory-research-776ae007899c`. Research evidence only.

**Existence scope:** tested the potentially decisive mismatch between finite
or countable actions and arbitrary set-sized arenas. The actual Flesch
Definition 2.1/footnote 2 allows infinite sets, and Remark 2.1 permits whole-
history feasible actions. Its subgame definition retains the prefix. Boolean
Reach has an open winning set even for an uncountable discrete alphabet.
Epsilon=1/2 rules out every strict Boolean improvement. Neither compactness
nor finite branching nor a measurability restriction is needed in this
application. The old theorem gives unrestricted strategies; only the new
compression supplies finite memory.

**Polynomial strengthening:** disproved by the complete binomial lower-bound
family, not by failure of a scheduling implementation. Every qualifying SPE
is covered, and only one player's victory is required, so allowing additional
winners cannot evade the lower bound. The argument freezes an arbitrary
profile and allows A all its phase choices; it does not presuppose the
profile's strategy for A. Every later check uses SPE at an actual legal
history. This is why an initial-NE check alone would be insufficient.

**Checker subtlety corrected before claim:** because all C_i target the same
terminal a, an unsatisfied checker need not exit immediately: a later checker
might do so and give it one. The proof uses only the valid conclusion that
an SPE cannot end at e while any index is missing. At a missing checker's
actual history on such an e-outcome, moving directly to a is profitable.
No stronger invalid immediate-exit assertion is used.

**Collision quantifier:** E's incoming memory states at the SAME actual
first response vertex must distinguish every r-subset. Remaining vertices
are determined by E and forced edges, so other players cannot signal their
memories during the response. Counted states cannot be replaced by an
uncounted previous-vertex register or an unobservable full history. The
lower bound applies to any vertex-dependent tables and unlimited memories
for the other players. It proves no exact optimal exponential base.

**All-history existence:** the explicit canonical E strategy wins after a
correct response prefix. Following a wrong inclusion/exclusion, the fixed
quota makes completion impossible, so E has no profitable repair. A has no
further choices and all checkers either are satisfied or can exit. Histories
that skipped an unsatisfied checker off profile are covered: that player's
past decision cannot be changed in the resulting subgame. Thus existence
does not rely on an incorrect claim that the whole prescribed initial
outcome is followed in every subgame.

**Reproducible checks:** `python3 code/check_subset_memory.py` checks seven
canonical family profiles after every legal history, 15,787 product states,
using exact reverse best-response reachability for every player. It also
exhausts allowed W,U pairs for k=1..12. A forgetful E control is rejected
at k=2 even though its initial outcome is E-winning; an actual profitable
A deviation is serialized. No finite range is substituted for the all-k
injectivity proof. The old upper-bound proof, code and finite checks are
unchanged; their previous failed variants remain preserved.

**Novelty attack:** the 2023 primary survey already says exponential SPE
branching memory is necessary. The lower bound therefore does not establish
an independent qualitative novelty. Flesch existence and finite-arena FPT
are also old. The remaining substantive claim is the full-scope uniform
upper-bound construction, which must be reassessed freshly rather than
certified by this record. No third research pass is requested just to chase
a stronger label. No manuscript/PDF or fresh referee verdict was created.
