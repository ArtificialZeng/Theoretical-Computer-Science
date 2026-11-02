# Triage checkpoint

Job: c029-vftfast-triage-c8f458fcdb95; 2026-11-02 UTC. Decision: advance.
Original status: unresolved; candidate_kind: none. No manuscript/PDF, candidate,
acceptance or venue classification. Prior initial state was unresolved with no
research passes; runner state still records research_passes=0 and revisions=0.
No counters, usage records, frozen inputs or scheduling state were modified.

Read source.md, prior problem/checkpoint, AGENTS.md, publication-policy.json,
outer-root-note.md, intake/root-handoff.md, source-inputs manifest, skill/triage
reference and the shared STOC standard. Source bytes match the existing runner
digest; all six primary inputs match their manifest. Evidence is in
evidence/triage-integrity.json and evidence/triage-sources.md.

The live arXiv record still presents 2610.33934v1 (24 October 2026).
Theorem 1.4 and printed pp.4--5 establish the target existential tradeoff and
explicitly leave its running-time improvement open. Bounded current searches
found no equivalent full polynomial-time realization: status open-supported,
not exhaustive novelty clearance. The original question is a precise uniform
polynomial-time target selected from that challenge. A wider historical
registry was not supplied here and was not inspected.

Nearest comparisons: source Theorem 1.3/Corollary 3.20 lose more in f;
Dinitz--Robelle 2020 Theorems 2/4 and Bodwin--Dinitz--Robelle 2021 Theorem 1.3
give efficient purely multiplicative VFT constructions and cut relaxations.
Their statements do not imply the frozen O(sqrt(k)),O(k) tradeoff uniformly in k.
Potential substantive payoff is making the new near-linear-fault frontier
algorithmically usable. Actual novelty/depth/STOC competitiveness remain unjudged.

Obstacle: source Algorithm 1 must find both a short path P and a fault witness
F avoiding every vertex of P. Speeding up the fixed-path fault-cut decision
alone leaves n^sqrt(k) enumeration. No separator or proof was established;
there were no failed mathematical experiments in this triage pass. Existing
intake caveats are retained. An intermediate-method failure is not a negative
answer to the original problem.

One next test (first bounded RESEARCH pass, at most 25 minutes): prove or
diagnose the joint gap separator precisely specified in problem.md: for
d<=sqrt(k), r=O_delta(k), find a path P and compatible cut of size O(r*f), or
certify absence of any witness of size f, in 2^O(d)*poly(n,f,r) time. Check
path protection, completeness, all required scales, and transfer of the source
packing analysis. A valid separator plus transfer could eliminate enumeration;
a failed route must be recorded without weakening the immutable target.
There remain at most three accumulated research passes under the existing cap.
