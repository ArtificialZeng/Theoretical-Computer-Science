# Checkpoint

Job `c012-upcycles-research-456cb4499028`, RESEARCH pass 2, 2026-11-01.
Decision: **candidate**, kind **resolution-paper**. Original status **proved**:
an affirmative existence witness for the full original question is proposed,
with fresh mathematical, novelty and significance review pending. Two research
passes consumed; one remains under the default ceiling. No acceptance,
manuscript/PDF, external submission, agents or background workers. Previous
checkpoint preserved as `evidence/research2-checkpoint-before.md`; every pass-1
attempt, certificate and usage entry remains in place.

## Immutable scope

The original asks whether ANY nontrivial finite-alphabet upcycle with d>=2
exists. A positive binary n12d3 witness suffices for the entire existential
question. We do not claim universal construction, minimality, d2 existence,
or a global negative theorem. `source.md` is unchanged, SHA256
`773f9e28946e0ee6f8def64bd988a0e6ae6f1a095968d275914978caa6ce2eac`.
`problem.md` retains the precise original reading and records the new candidate.

## Decisive evidence

The assigned guarded connectivity test succeeded. Target n12d3 period-four
rounds had 22,32,1 components, adding 488 then 496 guarded cuts. The final
selection contains 512 tiles in one component and yields one Euler word.
The three target solver calls totaled about 0.285 wall seconds, within
20 rounds/180 seconds and <=30 per call. All models, cut groups, CNFs, logs
and proof streams are retained in `evidence/research2-connectivity/`.

`evidence/research2-witness/witness.json` serializes the exact length-512 binary
word (word hash `c52b51a5317f1aa0080108366f9253d68e33e0723136a8ab261dadc8f5b73bb3`)
and its 128-octal-digit encoding. `evidence/research2-proof.md` supplies the
complete finite proof: all 130816 distinct pairs of cyclic windows have a
conflicting ordinary coordinate, so their eight-completion sets are disjoint;
their total size is 512*8=4096. Wildcards occur exactly at 0 mod 4, so every
12-window has d=3, including the boundary. Nontriviality and length identity hold.

The standalone verifier `evidence/research2_verify_witness.py` imports no solver
or old builder/checker and directly tests ALL 4096 total words against ALL 512
starts. Every count is exactly one; the full inverse table and pair certificate
are in `evidence/research2-witness/`. The 11 wrapping starts uniquely cover 88
words. Its self-contained `minimal_check.py` reconstructs the printed encoding
and passes a second direct exhaustive coverage test. Source n4d1/n8d1 pass and
intentional n4/n12 bit flips and all-zero controls fail.

Guard soundness controls cover all 512 toy directed subgraphs. Pinned source
n4d1/n8d1 and unpinned n4d1 are connected SAT. Bad n4 and the known n8d2
period-four control are UNSAT, both with independently checked LRAT/RUP
certificates; the n8 control required two cut rounds. Full benchmarks, results,
usage and integrity records use the `evidence/research2-` prefix.

## Literature, limits and one next test

Rechecked current July 2026 publisher Question 9.2/Remark 6.6, latest arXiv
record (v3), the 2025 tori paper, an author's page and cited code repository.
Targeted current searches found no equivalent resolution in inspected sources;
this is not exhaustive priority verification. `evidence/research2-literature.md`
records the comparison. The proposed innovation is the explicit d3 existence
witness, not the elementary exact-cover/Euler tools. Its 12 not dividing 512
also realizes the source's adjacent nondivisibility regime. No new general
theorem about that regime is claimed.

No mathematical gap has been identified in the finite positive-witness proof;
fresh correctness, novelty and significance assessment is still required.
`claim.json` requests that review and binds `source.md` and `problem.md`.

Next test: fresh referee, using only the frozen claim packet, reconstructs the
word and independently recomputes unique coverage of all 4096 words, all
cyclic starts and every original hypothesis, then checks current primary
novelty and substantive theoretical significance. No further search or
manuscript/PDF before that gate.
