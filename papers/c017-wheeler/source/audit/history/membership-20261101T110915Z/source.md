# Frozen original question: membership in the current Wheeler-transducer class

Primary source: Giovanna D'Agostino and Andrea Paradiso, Finite-State Transducers
in the Wheeler Setting, arXiv:2606.29405v3 (13 August2026), Section4, p16.
https://arxiv.org/pdf/2606.29405v3
Original question excerpt: “The most immediate is the decidability of membership
of a transducer in the class of Wheeler transducers”.

Selected original is this decidability question, before research; the separate
questions about equivalent realization, minimization and optimal complexity are
not the frozen question. A finite complexity upper bound for a proposed algorithm
must be justified. No one-state-only or nonerasing-only substitute resolves it.

Precise current-v3 meaning (Definitions4/5 and Section2.1): input is any finite
trimmed deterministic one-way subsequential transducer
T=(Q,s,Sigma,Gamma,delta,omega,F,t), with finite ordered input/output alphabets,
partial deterministic input transition delta, explicit output words omega on
exactly its domain (empty words allowed), and terminal output words t. Trimmed
means every state is accessible and can reach a final state. Input and output
string order is colexicographic, equivalently lexicographic order after reversal;
a proper suffix precedes its strict extensions. Let I_q be all words reaching q.
Let p<q mean every word of I_p precedes every word of I_q, for distinct states.
Definition5 requires (i) that these reaching languages are totally ordered and
(ii) for each q, alpha -> omega(s,alpha) on I_q admits a finite partition into
convex sets on each of which it is weakly nondecreasing or weakly nonincreasing.
The orientation and number of pieces may depend on q. Test accumulated transition
output, not the terminal-output function. Trim-empty degeneracies can be decided
separately without changing the nonempty instance question.

Full target: decide whether this membership property has an effective terminating
algorithm on ALL such finite inputs, with a complete proof of such an algorithm,
or prove that no algorithm exists by a valid undecidability reduction. A finite
collection of oscillating examples, an algorithm restricted to a subclass, or an
unproved pumping characterization does not resolve the target.

The v1 condition was monotonicity on a single piece and is superseded. Current
v3 Definition4 permits finitely many pieces. The old-v2 third-party criticism of
transitivity is not a resolution of this current question. Source-supported open
status is bounded by current exact/equivalent-term searches; fresh triage must
recheck relevant existing algorithms before mathematical novelty is claimed.
