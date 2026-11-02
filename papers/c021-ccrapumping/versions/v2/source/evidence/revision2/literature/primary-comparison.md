# Additional primary-source comparison for the active research

Supervisor source reading, 2026-11-01 UTC. These notes are outside every frozen project packet and do not constitute a fresh referee verdict. Download receipts are adjacent. The JCSS2019 URL failed SSL after redirect; STACS2016 author-hosted full text was obtained instead. Do not claim the JCSS body was inspected.

## Classical copyless normal forms

Mazowiecki–Riveros, Copyless Cost-Register Automata: Structure, Expressiveness, and Closure Properties, STACS2016, author-hosted fulltext https://fmazowiecki.github.io/papers/copyless2.pdf. Sections2–3, Proposition4 establish an equivalent normal form using permutations in finite control. Proposition5 resets nonstable registers within a strongly connected component; Proposition7 studies stable-register growth under nonzero-expression assumptions. Section4's expressiveness/reversal example is over the max-plus semiring. Sections5–6 give bounded-alternation copyless CRA (BAC) closure under reversal and related operations.

The text contains no asserted minimal-weighted-subquotient commuting-unipotent criterion. This is only a bounded comparison, not evidence that the new criterion cannot be derived from prior normal forms. A fresh reviewer must assess whether the minimum-rank retraction/projection transfer adds a substantive invariant beyond those facts. Existing zero/nonzero assumptions should not be silently transferred to Q with cancellation. The source's tropical reversal negative does not settle reversal over Q.

## Unary polyregular versus polyblind is not the new rectangular question

Gaëtan Douéneau-Tabot, Hiding Pebbles When the Output Alphabet Is Unary, ICALP2022 paper120, https://doi.org/10.4230/LIPIcs.ICALP.2022.120. Actual PDF Theorems3.3/3.4 characterize unary-output polyregular functions by rational series of polynomial growth and polyblind functions by sum/Hadamard closure of regular costs. Theorem4.6 decides polyblind membership through repetitiveness; Example4.8 says block-power sums a^n1 b ... a^nm b -> sum ni^k are not polyblind for k>=2.

A direct rectangular expression computes the square block sum: on each unary block, use a regular function to form A^n B^n (finite-tagged duplication/reversal suffice), apply rectangle, erase outer A letters, then map over block separators and erase the separators. Its output length is sum ni^2. Hence a blanket claim that rectangular output lengths must be polyblind is FALSE, not merely unproved. This does not refute the intended rectangular-length-to-Q-CCRA bridge: two independent counting registers, multiplied once and reset at each block end, plus an accumulator compute this square sum copylessly.

A possible stronger compositional invariant may be bounded-alternation arithmetic expressions rather than scalar lengths or polyblindness. This remains a prospective route, not a proved rectangular-to-BAC/CCRA translation. Arbitrary middle regular transductions and separator erasure must be handled. The full compression question remains unresolved, and no second manuscript is authorized.
