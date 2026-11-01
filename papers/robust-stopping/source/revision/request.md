# User-authorized paper3 reviewer revision, 2026-10-31

Authoritative reviewed artifact is output/STOC2027/paper3/paper3_submission.pdf,
the seven-page robust ski-rental manuscript, not the unrelated stoc3/ compiler
paper. Full user report is reviewer-report-20261031.txt. Prior release and all
snapshot inputs were preserved in revision/history/pre-review-* before work.
This is new work requested after the earlier five-paper task was completed;
preserve all runner usage/counters. No external submissions, uploads or messages.

## Required scientific and editorial response

1. Address the valid generic-LP criticism directly. The old polynomial-in-
   numerical-b result alone is not a new complexity guarantee. Do not imply an
   asymptotic advantage over generic LP without a proved comparison. Research
   the explicit uniform-forecast frontier candidate below as a possible genuine
   structural addition, with a sharp necessary b+1-support family. It is an
   unaccepted seed, not a theorem or priority claim. Stop adding speculation
   once a coherent audited contribution is available.
2. Correct oracle-call versus total-arithmetic-operation terminology. Supply
   complete backward-elimination optimality and intermediate-bit-length proofs.
   Remove the arbitrary eight-chord implementation heuristic from the paper's
   main algorithm; a simple rigorous bisection algorithm suffices. Optional
   accelerator belongs in code documentation only.
3. Inspect KF26 arXiv:2603.29233v1 Appendix D.2 and the exact Water-Filling
   procedure, quote <=25 TOTAL words verbatim from this source, identify the
   exact claim/inference and faithfully trace or execute its algorithm on the
   b=3, R=3/2, p=(2/5,3/5) instance. Do not claim a unique implementation output
   when the published algorithm is ambiguous; distinguish the forced outcome
   of its support-threshold prescription from any unspecified code details.
   Keep real reproduction/trace code and output.
4. Substantiate the objective-normalization distinction with a small exact
   example, or remove it. Candidate: b=3,R=3/2,p1=p2=1/2. Expected-cost optimum
   f1=1/4,f3=3/4 has J=15/8; the expected-per-horizon-ratio optimum f2=f3=1/2
   has ratio=5/4, whereas the former has ratio=21/16. The latter has J=2.
   Check globally with exact certificates before including.
5. Write a real introduction: motivation, the separating example early, exact
   contribution, and honest LP comparison. Add classical ski rental, learning-
   augmented tradeoffs, distributional advice, Besbes--Ma--Mouchtaki 2025,
   moment-constrained and tail-risk literature after inspecting primary texts.
   Reviewer-provided author lists/years are leads, not authoritative BibTeX.
6. Unify notation: distinct dual value, dual slopes and raw support threshold;
   distinguish feasible-policy polytope from rational field. Add concise sweep
   and price-recovery pseudocode, a useful proof/algorithm pipeline, and a
   schematic lower-envelope diagram or the proved uniform frontier plot.
   No invented measurements. Give an exact result table and portable code;
   move JSON/implementation bookkeeping out of the paper.
7. Delete repetitive defensive sentences; include intuition at each stage and
   handle degeneracies once through precise definitions/proofs. Keep the
   factual AI disclosure short and BEFORE the final bibliography.
8. Check current OFFICIAL STOC2027 CFP. Prior CFP requires named authors and
   a separate cover; preserve these if verified, explaining why the review's
   suggested anonymization/cover deletion is not followed. Exact user-supplied
   five authors/affiliations/emails remain controlling. Fei Ding's user-given
   affiliation/email domain difference is not evidence of an error: do not
   invent a replacement affiliation or email, ORCID or author consent.
9. <=12 TOTAL PDF pages including cover/references, official unmodified acmart
   class, single column/single space/11pt/Letter/1in. Keep proposition and proof
   together where possible. Explain Table1 support maximum as the support-
   threshold objective. Provide response_to_reviews_zh.md with every distinct
   reviewer request addressed and exact final theorem/section references.

The review's LP coefficients<=b claim needs a precise correction: the moment
row has coefficient t-1, so S can contain a huge forecast horizon+1. Generic LP
still supplies polynomial bit time; Tardos arithmetic complexity depends on the
constraint matrix. Do not mistake arithmetic-operation independence for a bit
running time independent of the input length.

## Handoff and deliverables

RESEARCH: complete proofs/counterexample searches and current novelty checks.
New claim may include the accepted old optimizer plus any verified uniform
frontier/sharpness results, but original general-frontier question remains
unresolved unless actually settled. New freeze and fresh referee required.
WRITE: only accepted scope; full self-contained proofs <=12 pages, corrected
notation, figures/pseudocode, expanded real literature, exact KF trace, Chinese
point-by-point response and portable standard-library reproduction entry point.
RELEASE: fresh current citation/build/all-page visual audit, exact authors and
class provenance, actual source-ZIP rebuild/reproduction. Preserve old history.
Local publication only. Avoid generic priority or STOC-acceptance claims.
