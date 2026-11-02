# RESEARCH pass 2 checkpoint

Job: c025-incdec-research-5525eccf7fba. Decision: continue bounded research.
Original status unresolved; candidate kind none. Assigned pass 2 of cap 3;
runner owns actual counters. No counter, frozen packet, previous verdict,
source content, or other project was edited. Entry checkpoint is preserved at
evidence/research-pass-2/checkpoint-at-entry.md. Source SHA256 remains
12956c470e37f8a548f510c7eb1781eda7b961999c5fa1163df43b56513b45a4.

Full arbitrary unequal-total all-cardinality scope, C_struct<=C_poly, and the
polynomial-oracle requirement remain unchanged. Current primary refresh found
no full equivalent resolution; nearest original-scope bounds remain 2 and
1+e/(e-1). See evidence/research-pass-2/literature.md. No priority is claimed.

New analytic progress: evidence/research-pass-2/modular-side-lemma.md proves
that for actual-gain bidirectional greedy, if g is modular, every left state
(L,T) and comparator O satisfy

    f(O) <= f(L)+g(E)+|O intersect (T\L)| d,

where d is the current maximum available gain (0 if finished). For |O|=|L|=k,
nonincreasing gains give k d<=f(L)-g(E), hence every left boundary is 2-good.
If additionally h(E)>=g(E), right boundaries are 2-good from their h(E)
baseline, proving the complete order's ratio 2 on this restricted class.
The reversed statement holds for modular h with g(E)>=h(E). This does not
resolve arbitrary pairs or even all modular-g unequal-total orientations.
It is a researcher proof record, with no fresh acceptance or novelty verdict.

Exact failed routes: h(O)+G<=2f(L) and h(O)<=f(L)+k d are both false on a
six-item coverage/modular instance. A five-item coverage pair refutes the
tracked-comparator bound f(O)-f((O union L) intersect T)<=G, even at zero
cardinality excess. All traces are maximal-gain and tie-admissible; their
output orders still satisfy ratio 2. See obstructions.md, template-screen.json,
and comparator-screen.json under evidence/research-pass-2. A symbolic family
extends the first obstruction to all m>=5 and has algorithm ratio tending to
2. These are intermediate method diagnostics, not original disproofs.

Surviving full-class kernel: at each left boundary with |O|=|L|,

    f(O) <= f(L)+G+|O| d.

Together with nonincreasing gains and reversal this would prove the original
ratio-2 algorithm theorem. It is sufficient, not claimed equivalent to the
original question. Bounded screens made 4148 successful numerical LP calls
at n=3..7 and a separately seeded 239 calls at n=8 without a positive witness.
The n=7/n=8 regions are incomplete and numerical nonfindings are not proofs.
residual-dual.json gives a 12-term exact rational certificate for ONE six-item
trace/comparator, using future choices. No uniform identity was derived.
code/verify_pass2.py independently checks every pairwise input inequality,
trace choice, exact witness gap, compact coverage description, and the dual
coefficient identity without a numerical solver. Results are in
independent-verification.json. This is computation verification, not a fresh
mathematical referee.

One next test for the final permitted pass: extend the modular-side proof to
the displayed coupled kernel by deriving a telescoping submodular overlap
budget for D=O intersect (E\T) and L\O. Specifically, replace the modular
step c(D)+c(L\O)<=G by an exact combination of h/g submodularity and the
recorded maximal-gain comparisons that yields f(O)<=f(L)+G+k d. Attack any
proposed identity on the two exact witnesses and the held-out n=8 trace family
with rationally checked duals/counterexamples. A uniform general-n identity
settles this algorithm route; a restricted-cone failure does not refute the
original. One pass potentially remains, subject to runner accounting. Park
if the final pass supplies no full resolution; no manuscript/PDF for partial work.

No claim.json, acceptance/readiness metadata, manuscript, or PDF was created.
