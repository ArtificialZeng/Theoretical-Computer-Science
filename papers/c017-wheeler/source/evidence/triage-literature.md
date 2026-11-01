# Bounded current-source screening

Job `c017-wheeler-triage-b86cccc47ffc`, inspected 2026-11-01 UTC.

## Primary records inspected

1. D'Agostino and Paradiso, *Finite-State Transducers in the Wheeler Setting*,
   <https://arxiv.org/abs/2606.29405> and
   <https://arxiv.org/pdf/2606.29405v3>.
   The live abstract/history lists v3, 13 August 2026, as the latest revision.
   Its correction notice concerns the earlier definition. Definitions 4/5,
   printed p.6, require finitely many convex weakly monotone pieces and accumulated
   transition output on each I_q. Section 4, p.16, explicitly identifies machine
   membership decidability as unresolved, separately from equivalent realization
   and minimization. Remark 4 p.15 supplies the complement example. The local
   text input is `intake/wheeler-v3.txt`; the existing source receipt describes
   the downloaded primary input, not a new manuscript.
2. D'Agostino, Martincigh and Policriti, *Ordering Regular Languages: A Danger
   Zone*, <https://ceur-ws.org/Vol-3072/paper5.pdf>.
   Inspected abstract pp.1 and definition pp.4-5. It distinguishes testing a
   given Wheeler DFA from recognizing its language's Wheeler realizability;
   neither includes an output monotonicity decision. Its graph definition has
   additional initial-state/incoming-label requirements. No unqualified transfer
   to the frozen v3 reaching-language definition is used here.
3. Becker, Cenzato, Kim, Kodric, Policriti and Prezza, *Optimal Wheeler Language
   Recognition*, <https://arxiv.org/abs/2306.04737>, v2, 18 December 2023.
   Inspected primary abstract: its O(mn) algorithm concerns whether the language
   accepted by a DFA has a Wheeler presentation. This is not the output property
   or the full current membership question. No proof in that paper was audited.
4. Filiot, Reynier and Lhote, *Lexicographic Transductions of Finite Words*,
   <https://arxiv.org/abs/2503.01746> and the primary MFCS record
   <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.MFCS.2025.50>.
   The inspected abstract and retrieved Section 4 excerpt describe exponential
   growth transductions, maplex and inverse regularity preservation. They do not
   supply a piecewise colex-monotonicity test. This is a terminology collision,
   not a verified algorithm settling our question. No full-text exclusion claimed.

## Exact and equivalent-language searches

Queries included the exact paper title; "Wheeler transducers" decidability
piecewise monotone membership; "Wheeler transducer" membership algorithm
decidability; "transducer" "piecewise monotone" decidable; "transducers"
"lexicographic" "monotonicity" decidability; "piecewise monotone" "sequential"
words; and "limitedness" "transducers" "lexicographic". Bounded search returned
the source and adjacent algorithms, but no inspected full resolution. Search
snippets and third-party old-version criticisms were treated only as leads.
This supports exploratory admission, not exhaustive priority or novelty.
An initial version-specific abstract fetch failed; the unversioned live abstract
and version-specific PDF subsequently succeeded. The failure is operational only.

## Historical overlap check

Read-only filtered inspection of the available continuous registry found three
related leads: `wheeler-membership-v3`, `wheeler-realizability-v3`, and
`wheeler-minimization-v3`, plus the current running job. The membership lead
matches this assigned question; realizability changes the quantifier to existence
of an equivalent machine; minimization concerns a different optimization target.
The historical batch2 registry had no Wheeler match in the screened scalar
identity/title/status fields. No registry or scheduling data were edited; no
claim of exhaustive semantic duplicate detection is made.

## Decision

Advance for bounded research: precise full target, direct primary open-status
support, nontrivial potential payoff, and a falsifiable first pumping test.
Current kind is none and original status unresolved. The paper's other quotient
or closure claims are not premises of a proposed algorithm and have not been
certified. No output algorithm, effective output comparator, finite partition
bound, or original resolution has been established.
