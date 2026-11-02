# Primary-source comparison, 2026-11-02

Job: c034-grouptri-research-d92d3d43a90d. Research proposal, not referee review.

Reopened the actual primary arXiv records during this pass:

* [Majdoddin, arXiv:2610.17420](https://arxiv.org/abs/2610.17420): submission
  history displays v1, 12 October 2026. Local unchanged full input:
  `intake/primary/2610.17420v1.pdf` and its extracted text. Inspected again
  Theorem 21.3 and its complete proof, the Corollary 9.1 statement/proof and
  H instantiation; Section 19 Model; Remark 21.8; Propositions 21.9--21.10;
  Open Problem 21.12. The elementary backend has the stated saving 0.0055;
  the nearest non-elementary results require few quotient-zero triangles or
  small incident residue degree. Neither covers the full original. This pass
  relies on the stated prior theorem and does not claim a fresh independent
  audit of every matrix dependency in its 130-page input.
* [Chan--Vassilevska Williams--Xu, arXiv:2303.14572](https://arxiv.org/abs/2303.14572):
  submission history displays v1, 25 March 2023. Local full input:
  `intake/primary/2303.14572-primary.pdf` and extracted text. Reread the full
  Theorem 5.1 construction and correctness/update argument, plus relevant
  Section 5 applications. Its fresh-input construction initially sorts all
  middle sums in cubic time; its fast update charge is insufficient here.
  The frequency construction already supplies the identities used in our
  gauge. The decomposition and those identities are attributed prior tools.
* [Sheffield--Vassilevska Williams--Xi, arXiv:2608.19092](https://arxiv.org/abs/2608.19092):
  submission history displays v1, 19 August 2026. Inspected abstract and the
  introduction/reduction context again; pass 1 inspected Section 2.3. Generic
  detection/all-edge/listing relationships and losses are established prior
  work. Our deliberately conservative capped-listing tool is not proposed as
  novel. This work concerns generic reductions, not an all-exponent abelian
  extension algorithm in the inspected passages.

Live exact-phrase searches in this pass included:

    "Exact Triangle" "bounded exponent" group algorithm
    "triangle decomposition" "abelian" kernel quotient
    "Exact Triangle" "group extension"
    "Exact Triangle" "bounded-exponent" algorithm
    "Exact Triangle" "quotient" "decomposition"
    "triangle decomposition" "finite abelian groups"
    "exact triangle" "finite abelian" algorithm decomposition
    "Exact Triangle" "kernel" "group"
    "Zero-Triangles" "group" decomposition
    "bounded exponent" "subcubic" triangle

No equivalent full closure theorem was located by these bounded searches.
Most unrelated results concern exact triangles in algebraic geometry and were
not used. Secondary mirrors/snippets were not evidence for theorem status.
The integer Exact Triangle formalization/repository hits do not by their titles
or search snippets settle torsion-group scope; no such inference was made.
The current author repository was already inspected at the pinned commit in
the intake/pass-1 record; this pass does not claim a new repository build.

Proposed mathematical delta: replace cubic quotient preprocessing by legal
capped lists, produce the gauge-bearing quotient pieces, cancel lift carries
using explicit vertex potentials, and charge all materialized complete kernel
instances in a finite induction through every fixed exponent. The complete
algorithm covers the full bounded-exponent question, with a saving independent
of the dimension constant. A potential reusable method is this closure step,
not a stronger generic listing reduction or a new matrix primitive.

Adverse novelty/value question for the fresh referee: are these steps a
substantive extension principle, or an elementary routine consequence of the
listed prior tools that does not meet this project's publication standard?
An explicit open-problem label and finite tests do not answer that question.
The saving is extremely small and no practical running-time benefit is claimed.
No global priority certificate or STOC competitiveness verdict is asserted.
