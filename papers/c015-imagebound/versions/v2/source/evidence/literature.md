# Bounded primary literature check

Retrieved/inspected 2026-11-01 for job c015-imagebound-triage-104fc05d5d7d.
Scope is intake screening, not exhaustive novelty certification.

1. Stefan Kiefer and Andrew Ryzhikov, *The Complexity of Reachability Problems
   in Strongly Connected Finite Automata*, MFCS 2025, 62:1–19.
   DOI https://doi.org/10.4230/LIPIcs.MFCS.2025.62.
   Local original intake/primary.pdf and text intake/primary.txt inspected:
   Section 2 pp.62:2–3, Section 3 pp.62:5–6, Section 7 pp.62:14–15,
   Section 9 p.62:16. The last section poses tightness of n^(k+1);
   Section 7 explicitly warns that letter branching degree is insufficient.
   https://arxiv.org/abs/2504.13784 lists latest v2, 2025-07-23.

2. Andrew Ryzhikov, *On shortest products for nonnegative matrix mortality*,
   RP 2024, pp.104–119, DOI https://doi.org/10.1007/978-3-031-72621-7_8.
   Current https://arxiv.org/abs/2405.19622 lists v4, 2025-06-15.
   Inspected https://arxiv.org/html/2405.19622v4: Introduction,
   Section 2.2, Section 5. Arbitrary NFA bound 2^n-1 is attained;
   reductions replacing missing transitions by Q need not preserve fixed
   global k. Section 5 reports the tight partial-DFA n(n+1)/2 bound
   attributed there to Rystsov 1997, and gives a binary queue/excursion
   construction. The original Rystsov paper was not separately inspected.
   This calibrates k=1 and motivates, but does not settle, our extension.

3. Stefan Kiefer and Corto Mascle, *On Nonnegative Integer Matrices and
   Short Killing Words*, SIAM J. Discrete Math. 35(2):1252–1267 (2021),
   DOI https://doi.org/10.1137/19M1250893.
   https://arxiv.org/abs/1808.00940 (v4, 2021-02-26), abstract and scope
   inspected, also Oxford record https://ora.ox.ac.uk/objects/uuid:d8c464ff-cd44-4e65-98bf-b5ef4203acdb.
   Its n^5 killing-word bound assumes joint spectral radius at most one;
   we did not inspect a proof extending it to globally image-bounded NFAs.

4. Kiefer and Ryzhikov, *The Asymptotic Size of Finite Irreducible Semigroups
   of Rational Matrices*, STACS 2026, DOI
   https://doi.org/10.4230/LIPIcs.STACS.2026.60.
   Inspected Sections 1–2 and Theorem 29 in publisher HTML:
   https://drops.dagstuhl.de/storage/00lipics/lipics-vol364-stacs2026/html/LIPIcs.STACS.2026.60/LIPIcs.STACS.2026.60.html.
   Theorem 29 gives 3^(n^2) for finite rational matrix semigroups. It is
   neither a fixed-k polynomial improvement nor a theorem about all
   Boolean support semigroups interpreted as ordinary rational products.
   Author's current list https://sites.google.com/site/ryzandrew/research
   checked for relevant follow-ups; this 2026 paper was screened explicitly.

Hypothesis separation: on two states, the all-ones adjacency matrix J has
global row support <=2 under every word, while J^t=2^(t-1)J in ordinary
arithmetic. Adding a zero letter makes the automaton incomplete without
changing that image bound. Thus the promise implies neither finite ordinary
matrix semigroup nor joint spectral radius <=1. Boolean finiteness cannot
be silently substituted for ordinary matrix finiteness.

Searches covered: exact title; Kiefer Ryzhikov image-bounded mortality;
k-image-bounded mortal tight; automata bounded image mortality;
image-bounded automata 2026 mortal; nonnegative matrix mortality shortest
polynomial; finite rational semigroup mortality; short killing words.
Relevant inspected primary records above did not contain a resolution of
the fixed-k hierarchy. Search snippets and absence of hits are not proofs
of open status. An accidental malformed arXiv URL (1801.0000) failed to
fetch; no mathematical inference or literature claim uses it.

Duplicate check: c003-compress/source.md was read without modification.
It asks O(n) pair merging for a distinguished state of a complete,
strongly connected synchronizing DFA. Here total DFAs cannot even be
mortal, and we ask global annihilation in incomplete bounded-image NFAs.
No registry-named file was found at the research/queue roots; a full
historical registry comparison remains unverified.
