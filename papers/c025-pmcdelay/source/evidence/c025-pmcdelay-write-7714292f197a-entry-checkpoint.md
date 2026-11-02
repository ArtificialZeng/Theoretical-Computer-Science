# Checkpoint — research pass 1 completed

Job: c025-pmcdelay-research-338d67d18097. Outcome **candidate**;
candidate_kind **resolution-paper**; original_status **proved** is the
researcher's full-scope proposed result, awaiting fresh mathematical review.
No acceptance, venue assessment, manuscript/PDF or publication exists.

Immutable `source.md` is unchanged, SHA-256
30ba523462232346f8c2d671825d32d790edcd9362f00b8eec84a58e11d4e5cc.
The runner already records research_passes=1/3 and revisions=0; this worker
edited no scheduling counters. Entry problem/checkpoint copies are in
`evidence/c025-pmcdelay-research-338d67d18097-entry-{problem,checkpoint}.md`.
Earlier actual triage advanced an open-supported target; its artifacts and
verdict remain retained.

## Proposed resolution and new decisive evidence

`claim.json` binds the original, precise interpretation, complete proof,
primitive contracts, actual primary inputs and targeted test. The complete
algorithm/proof is `research/streaming_proof.md`. Its new substantive steps:

- A deterministic polynomial separator-to-PMC helper has an outside-component
  witness, so each image has at most n preimage separators. Clique-sum
  minimality is proved against every proper subtriangulation.
- The source's seed family is kept complete. An endpoint inconsistency in
  source Definitions 12/20 is explicitly disclosed; a graph-search formula
  and a transfer argument show that the structural predecessors actually used
  in source Theorems 9/10 remain arcs of this defined neighborhood.
- Streaming child emissions have injective lifts. Simultaneous bounds
  E(j)<=Q(n)j and T<=Q(n)K close with
  Q(n)=Q(n-1)+(n+10)p(n), avoiding a multiplicative recurrence.
- Standard buffering uses both E and T to cover first, intermediate and final
  waits, including when the emission rank exceeds the output count. Empty,
  complete and disconnected inputs are handled explicitly. No exponential
  cleanup is performed after final output; exponential storage is permitted.

`research/polynomial_primitives.md` specifies the graph-search BBC separator
queue primitive (emit on dequeue, use tries), explicit MCS-M fill-path tests,
and endpoint contracts. The source's actual Lemma 1 and actual MCS-M
pseudocode/Theorem 4.4/complexity were inspected. No exponential subset oracle
enters the proposed algorithm or its delay analysis.

New exact diagnostic: `evidence/pass1-targeted-streaming.json` records **29
specified graphs, n<=10, 471 total PMC outputs**, all complete output and
separator sets matching exhaustive finite oracles; no duplicate output, and
helper witness/fiber and recursive lift/queue checks passed. Generator code
is `research/targeted_streaming_check.py`; exhaustive subsets appear only in
its finite expected-output oracle. The 1036-case root sweep was not rerun.
Initial PATH-python invocation lacked NetworkX; the explicit existing Anaconda
interpreter succeeded. Both outcomes are in `evidence/pass1-operational-log.md`;
the dependency failure is not mathematical evidence.

## Prior work, limitations and preserved failed routes

`evidence/pass1-literature.md` records live primary histories and current
bounded searches. BLS v3 still gives total output-linear time; Kenig v1 gives
size-parameterized delay; IPEC 2025 covers triconnected planar graphs and
already uses the separator extension analogue. Capelli–Strozecki STACS 2023
and its July 2026 Computational Complexity follow-up make buffering a known
tool. No equivalent full all-size delay result was found in this bounded
search; no priority certificate is claimed. New value is the complete PMC
streaming conversion, not any individual known ingredient.

Known remaining proof gaps in the proposal: none beyond its named established
source dependencies. A fresh referee must still challenge correctness, source
transfer, current novelty and substantive value; STOC depth/breadth/importance
remain unassessed. The earlier single-seed/atom-neighborhood route failed on
18 retained root cases; it stays failed and never became a disproof of the
original. All intake files and earlier verdicts remain untouched.

One next test: **fresh referee** attacks the frozen full proof, especially the
endpoint-safe source-preimage transfer, helper minimality/fiber and simultaneous
emission/termination induction, independently checks current equivalents, and
assesses substantive innovation and STOC significance. Do not WRITE until
actual freeze/fresh-review/check-math gates pass.

Timing: first actual clock 23:05:24 UTC; proof and targeted test completed by
23:18:11 UTC, before the 23:20:21 main-test deadline. All records finalized
before the 23:23:21 finalization deadline. No agents, extra Codex processes,
background workers, external submission/contact or other-project edits.
