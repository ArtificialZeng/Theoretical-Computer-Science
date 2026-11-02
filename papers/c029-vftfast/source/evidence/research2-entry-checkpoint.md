# Research checkpoint — pass 1

Job: c029-vftfast-research-6281f7685c7a; 2026-11-02 UTC.
Decision: continue; candidate_kind none; original_status unresolved.
No candidate, acceptance, manuscript/PDF, or venue-readiness label is created.
Source SHA-256 remains
45828a099cc88bde52aee6450b298c8b73397e4367d3911585521595f94657b8.
The prior checkpoint is preserved verbatim in evidence/research1-entry-checkpoint.md.
This is assigned accumulated research pass 1 of at most 3; up to two further
passes remain subject to the runner. No scheduling, usage, failure or pass
counter was reset or hand-edited. Triage job c029-vftfast-triage-c8f458fcdb95
advanced the unresolved target; its evidence is retained.

Read the skill and assigned research reference, project/source-model inputs,
outer-root-note, handoff, manifest, policy and shared STOC standard. Current
primary recheck still finds the source's explicit running-time challenge, not
a full solution. Bounded searches establish no priority certificate. Details
and the generic induced-path hardness caveat: evidence/research1-sources.md.

New evidence: evidence/research1-separator.md gives three inspectable arguments.
(1) The DR2020 gap-cut test can protect an entire fixed path, returning a
compatible cut of size at most (r-1)f or correctly rejecting every protected
cut of size f. This is a routine adaptation, not an innovative contribution.
(2) A deterministic joint separator with O(r*f) witness inflation would imply
the full frozen construction: insertions add new edges, the source packing
argument uses insertion witnesses and permits adaptive order, and pendant-path
reductions supply every Appendix B scale. The long source packing theorem is
a cited dependency, not independently certified here. (3) A path list chosen
before seeing H can require binomial(f+d-1,d-1) supports even if compatible
output cuts have unlimited size. This proves a method-class obstruction, not
original construction hardness. The complement argument is elementary; no
independent novelty is claimed.

Exact finite checks passed: evidence/research1-checks.json records 1,002,072
protected-cut cases over all labeled H on 2..5 vertices, all terminal pairs
and protected sets, radii 1..4 and budgets 0..2, with zero failures. It also
records 8,540 support comparisons for p,f=1..4, with zero failures. Reproduction:
evidence/research1_checks.py. Small serialized witness:
evidence/research1-obstruction-witness.json. These checks supplement proofs;
they establish no general separator or full resolution.

Failed route and limits: the fault-oblivious representative-list approach has
a proved obstruction, but its witness has G-F distance 2 rather than d when
d>=3. It cannot defeat a separator complete only on shortest-distance-d
violations. Every shortest witness is induced in G, though inducedness alone
is insufficient. Simple-path color-coding and generic representative-set
bounds do not settle the joint step. No original counterexample, original
hardness reduction, or full algorithm is established. Significance and STOC
competitiveness remain unassessed. No publication gate is met.

One next test: construct or diagnose the weaker sufficient H-dependent
SHORTEST-VIOLATION separator now specified in problem.md. For d=floor(sqrt(k))
and r=O_delta(k), either return a length-d P and C avoiding P, |C|=O(r*f), with
H-C endpoint distance >r, or certify no |F|<=f with G-F distance exactly d
and H-F distance >r. Seek time 2^O(r+d*log(d+2))*poly(n,f,r), fixed polynomial
exponents, using H-dependent length-bounded-cut packings. This is polynomial
under the logarithmic k cap; n^d or f^d fails. A rule-level falsifier must be
a geodesic violation. The changed completeness target and transfer argument
support a second bounded positive-algorithm pass. Without further concrete
progress, retain this dossier and park; do not issue a manuscript.
