# Additional primary comparison for the proposed algorithmic extension

Checked2026-11-01UTC. This is a bounded source comparison, not fresh acceptance,
an exhaustive priority assertion or a new open-problem admission.

The March11,2026 University of Warsaw seminar “Minimizing Cost Register
Automata over a Field,” Yahia Benalioua, describes a previous joint work:
https://mimuw.edu.pl/en/seminars/talk/minimizing-cost-register-automata-over-a-field/
The relevant original paper is Benalioua–Lhote–Reynier, MFCS2024, article23:
https://drops.dagstuhl.de/storage/00lipics/lipics-vol306-mfcs2024/LIPIcs.MFCS.2024.23/LIPIcs.MFCS.2024.23.pdf

The actual primary abstract and Sections1–2, printed pp.23:1–23:4, were read.
That work minimizes register count and joint state/register count for linear
and affine CRA over fields using linear/affine hull invariants. Register
updates may take general linear combinations; no global copyless-support
condition is part of that model. The stated bounds are2EXPTIME for register
minimization and NEXPTIME for joint minimization. Thus it does not directly
decide whether a scattered-pattern series has ANY equivalent polynomial
copyless CRA with arbitrary finite register count. This distinction must be
preserved; the standard weighted minimization tools themselves are known.

Queries copyless+unipotent, copyless+polynomial-series,
cost-register+scattered-subwords and register-minimization+field were also run.
They located the source STACS2026 paper and the above older minimization work,
but no equivalent of the proposed all-word-unipotent finite-control theorem
within the primary leads inspected. Search snippets and seminar dates were
not treated as proof of novelty or as new publication dates. The full current
source bodies and later follow-ups still require the actual revised referee's
own bounded comparison before incorporation.
