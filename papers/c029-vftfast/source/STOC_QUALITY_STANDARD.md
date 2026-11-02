# STOC competitiveness and artifact labels

User instruction received 2026-11-02 Asia/Shanghai: raise the research standard,
aim at acceptance by the 59th ACM STOC (2027), label weaker final PDFs
`working_paper` and genuinely competitive completed submissions
`submission_ready`. This supplements, and does not weaken, the resolution-only
policy in CONTINUOUS_RESEARCH.md. An unresolved question, conjecture, routine
corollary, rediscovery or result without substantive innovation still receives
no new manuscript/PDF.

The user's further clarification is proof-oriented: research must not become
a stream of subsidiary counterexamples. Prioritize complete positive theorems,
algorithms, structural characterizations, meaningful lower bounds and new methods
that support a competitive STOC paper. Use counterexamples to test and redirect
those proof programs. A counterexample to an intermediate lemma is not the
research endpoint, not a paper-count achievement, and not a substitute for the
full original problem. A substantive full disproof of an original conjecture
can still be valuable; its significance must pass the same high standard.

## Two separate judgments

At intake, prioritize the size and significance of a successful resolution,
not merely how likely a quick proof seems. Inspect why the source community
cares, the obstacle to known methods, and the consequence of settling the full
question. Do not fill an admission quota with weak variants or easy isolated
examples. A bounded decisive test may clarify an uncertain high-value route;
it does not justify writing a marginal manuscript to increase paper count.

Mathematical correctness, original-scope resolution, substantive novelty and
artifact checks remain necessary. Passing those gates alone does not establish
STOC competitiveness. The latter requires a fresh, critical internal assessment
of the strongest result against its nearest verified prior work and broad TCS
interests. This is a judgment, not a venue decision or a calibrated acceptance
probability. Do not use numerical acceptance percentages.

Use exactly these labels on delivered PDF filenames and manifests:

- `working_paper`: a fully resolved, substantively innovative result that passed
  the existing mathematical and artifact gates, but whose STOC significance,
  technical depth, breadth/consequence, or presentation is weak or uncertain,
  or has not yet received the new explicit fresh venue-level assessment.
- `submission_ready`: all existing gates pass AND a fresh assessment supports a
  strong, concrete case for competitive STOC submission. An important, difficult
  original problem or a conceptual/technical advance with substantial consequences
  must be explained, not inferred from a problem's being open or a paper's length.

Default conservatively to `working_paper` when the record is insufficient.
Do not upgrade merely because an internal referee accepted correctness/novelty,
because the format matches STOC, or because a PDF compiles. Do not inflate a
special case, several routine corollaries, a small computational example or
an isolated neat inequality into a general breakthrough. A short proof can
qualify when the actual advance is important; page count is not a quality score.

## Fresh referee assessment, alongside mathematical review

Read the exact original source, frozen claim/proof, nearest primary results and
their subsequent developments. In addition to the standard math/innovation
reports, write `audit/stoc-assessment.json` with:

```json
{
  "job_id": "the actual injected MATH_JOB_ID",
  "snapshot_digest": "the actual frozen mathematical snapshot digest",
  "review_type": "fresh_internal_stoc_assessment",
  "verdict": "working_paper or submission_ready",
  "strongest_result": "precise strongest theorem and its original scope",
  "nearest_comparisons": ["precise primary result and substantive difference"],
  "criteria": {
    "importance": {"judgment": "strong, uncertain, or weak", "reason": "specific evidence"},
    "novelty": {"judgment": "strong, uncertain, or weak", "reason": "specific evidence"},
    "technical_depth": {"judgment": "strong, uncertain, or weak", "reason": "specific evidence"},
    "breadth_or_consequence": {"judgment": "strong, uncertain, or weak", "reason": "specific evidence"},
    "exposition_and_verifiability": {"judgment": "strong, uncertain, or weak", "reason": "specific evidence"}
  },
  "case_for_stoc": "A critical argument using the concrete theorem, its obstacle, and why the community should care.",
  "remaining_weaknesses": ["real weaknesses or uncertainties, if any"],
  "label_is_not_a_venue_decision": true
}
```

`submission_ready` requires every criterion to be `strong`, supported by actual
arguments and sources; real uncertainty about competitiveness means
`working_paper`. A narrow result needs an unusually strong significance case.
Explain the hardest genuinely new step, why known methods do not give it, the
size of the resolved problem, and an important consequence or broad structural
insight. Distinguish an attractive research topic from the actual theorem proved.
Retain an honest `working_paper` assessment rather than engineering a passing
score. An unsupported strong score is not a substitute for review.

The referee may accept a complete, innovative mathematical result while marking
it `working_paper`. An unoriginal/insignificant mathematical result is still
rejected under the earlier publication gate, not rescued by this label.

Before delivery, bind the classification to the actual accepted mathematical
snapshot, run all existing clean-build/citation/every-page/ZIP-reproduction
checks, and disclose remaining citation-access limits. An optional publisher
metadata refresh failure alone does not determine scientific quality or veto
a clean artifact. Actual submission also requires the author's video and other
conference-system information; no external submission/contact is authorized.

## Historical and currently running work

Do not alter frozen mathematical packets or overwrite past reviews. Existing
accepted work without this fresh explicit assessment is provisionally
`working_paper`, not retroactively certified `submission_ready`. Add separate
classification records and labelled copies/filenames, preserving original
PDF/ZIP bytes and author lists. The completed GitHub snapshot remains historical;
new labels do not authorize automatic future public uploads.

Inject this standard into future runner contexts after the current owner drains.
Do not start a second owner or reset resource/pass history to apply the policy.
