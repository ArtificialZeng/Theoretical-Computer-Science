# Frozen original source question — c032-dspdag

Title: Break the n^(k+1) barrier for fixed-k disjoint shortest paths on DAGs

Primary source: Akmal–Vassilevska Williams–Wein, arXiv:2404.15916v2, Section7, printed41; ICALP2024 DOI10.4230/LIPIcs.ICALP.2024.9.
Exact source PDF SHA256: 709ca7a232602574ae96baa89509fbcb3534242a3a7fdacbc76fd3c3d0b5dd99
Source inspected on 2026-11-02T11:01:59.474887+00:00. The following quotation preserves the pdftotext extraction, including its mathematical typography limitations; normalized meaning follows separately.

```text
Open Problem 3. Is there a ﬁxed integer k ≥ 3 and constant δ > 0 such that k-DSP in DAGs
can be solved in O(nk+1−δ ) time? Or does some popular hypothesis rule out such an algorithm?
```

## Fixed precise reading

Exactly AVW Open Problem3: there exist a fixed integer k>=3 and a constant delta>0 with a uniform O(n^(k+1-delta)) algorithm for every weighted DAG under the source model, or a standard-hypothesis lower bound ruling out the existential improvement. Detection suffices; do not add a reporting requirement. An arbitrary-layer-width restriction, zero-weight toy regime, shaving only logs, or improving one sparse subclass is not a full positive answer. A negative result for only one k does not rule out existence for another k.

The input is a weighted graph on n vertices and m edges with the specified source–target pairs. Each returned path must be globally shortest for its own designated pair in the ORIGINAL graph. Distinct path terminal pairing is prescribed. Internal vertex disjointness follows the original source convention, not edge disjointness or unspecified pairing. Preserve the source's computational model and account for all preprocessing; characterize any source ambiguity before research, rather than silently changing the question. Positive weights/cycle promise rule out the trivial zero-weight NP-hard reduction. Unit-cost field operations are governed by the stated Word-RAM, not arbitrary bit-cost exact arithmetic for free.

## Nearest verified statements and current-status scope

AVW2404.15916v2 Theorems1–3 give randomized linear 2-DSP detection in DAGs/undirected graphs, O(mn) search, and an existing Baur–Strassen derivative step. AVW Section5 and introduction give the standard O(m n^(k-1)) DAG routine. CKS ITCS2026 Theorem1.1 gives directed O(mn log n) detection and O(mn^2 log n) reporting; full2509.14588v2 adds Min-2-DSP details. ESA2017 Bérczi–Kobayashi has polynomial directed two-pair algorithms (including multiple paths for only two terminal pairs), which is not the three-general-pair question. Current planar FPT and variable-k approximation hardness concern different quantifiers. Bounded exact/equivalent searches on2026-11-02 found no complete resolution of this selected target; this is provisional open-supported status, not a priority certificate. TRIAGE must inspect any newer claimed proof instead of treating lack of review/formalization as openness.

## Decisive first test

Reconstruct the O(m n^(k-1)) ordered-frontier recurrence for k=3, then derive an exact batched Boolean/matrix multiplication transition preserving all three collision/endpoint constraints. Compare the transition table against exhaustive disjoint paths on tiny DAGs and bound total products over the actual topological blocks. The decisive test is a proof and charged O(n^(4-delta)) schedule or a named violated batching invariant, not a guessed FMM speedup.

## Scientific publication condition

The goal is a complete positive algorithm/structural method or an important full lower-bound resolution serving STOC. Counterexamples to an intermediate technique remain diagnostics. Only complete resolution of this unchanged original, substantive innovation and actual fresh correctness/novelty/value acceptance permit manuscript writing. Preserve failed routes and at most3 accumulated research passes; no renamed retry. No manuscript/PDF for partial/known/routine outcomes. A fresh uncertain STOC assessment means working_paper, never submission_ready. Sole future author Zijian Zeng, UCSI University, 1002266693@ucsiuniversity.edu.my; max12 total pages and truthful AI disclosure. No external upload/submission/contact.
