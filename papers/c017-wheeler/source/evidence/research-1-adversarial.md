# Adversarial checks of the SCC/block algorithm

Job c017-wheeler-research-8ca2b0cef7a6. Internal researcher checks, not an
independent referee context or acceptance. No other agent/process was launched.

## Exact common-suffix certificates in both cut directions

Full tables/templates and exact replay checks are in exact-certificates.json;
regenerate with `python3 evidence/check_exact_certificates.py` from project root.

1. **Branching two-state SCC.** Both states read 0 into state 0 and 1 into
   state 1, outputting the complemented letter. Start at 0, all states final.
   The reaching-language order is I_0<I_1 (I_0 includes epsilon and all words
   ending 0). A base valley at 0 is 000<10<0010. Return loops 0 and 10 have
   distinct first letters. Their squares A=00, B=1010 are suffix-incomparable.
   Appending A B^n gives the certificate
   00000(1010)^n < 1000(1010)^n < 001000(1010)^n.
   It retains the strict valley. The interval direction is INCREASING, since
   rev(A)=00 precedes rev(B)=0101 at their second symbol; after n common
   rev(B) blocks this fixed mismatch separates every point of interval n
   from every point of interval n+1. This checks a multi-state branching SCC.

2. **Simple cycle, increasing side and unbounded independent prefix outputs.**
   States s=0,r=1,p=2, initial s; edges s0/0->r, r0/0->r,
   s1/epsilon->p, r1/epsilon->p, p1/0->p. All states final, terminal outputs
   empty. Reaching languages are {epsilon}, 0^+, and
   {1^m:m>=1} union {0^k1^m:k,m>=1}, in that order. At p with loop c=1,
   R is empty and L={1} union 0^+1. Thus the predecessor range 0^+ is
   unbounded, not replaced by a finite cap. The exact family is

       U1(n)=1(11)^n, U2(n)=001(11)^n, U3(n)=11(11)^n.

   Their reversals show U1<U2<U3<U1(n+1). Their output lengths are
   2n,2n+2,2n+1, so this is a strict peak for every n. It is the failure
   of monotonicity of L union Lc, with two loop traversals per pump.

3. **Simple cycle, decreasing side with erasure.** States s=0,p=1,r=2,
   input alphabet 0<1<2; edges s0/epsilon->p, s1/epsilon->r,
   s2/1->r, r0/epsilon->p, p0/0->p. All states final. Reaching languages
   are I_s={epsilon}, I_p=0^+ union 10^+ union 20^+, I_r={1,2}, ordered
   I_s<I_p<I_r. At p, c=0, L={0}, R={10,20}. The family

       U1(n)=100(00)^n, U2(n)=200(00)^n, U3(n)=10(00)^n

   is strictly ordered and has output peak 0^(2n+1), 10^(2n+1), 0^(2n).
   The next interval lies strictly before the current one: U3(n+1)<U1(n)
   because their reversals first differ at 0 versus 1 after 2n+2 zeros.
   This is a failure of the Rc union R test. Empty edge outputs occur at
   four of the five transitions; the argument does not require nonerasure.

All hypotheses (accessibility, coaccessibility, defined runs, ordered reaching
languages, strict output signs and interval direction) follow from these exact
tables and identities. Replay at n=0..11,17,31,257 checks the implementation;
the identities above, rather than the finite replay, establish all n.

## Positive nested-turn control

The supervisor's three-state example is accepted, with exactly two finite-sample
pieces at p and, by the written annular proof, two infinite pieces. Its left
and right side tests both pass with opposite orientations. A common central
cut can contain infinitely many nested turns while each side stays monotone.
Thus the new criterion does not reuse the refuted 'any cyclic turn' shortcut.
Identity, complete erasure and h(0)=0,h(1)=11 pass as required. Complement,
length-only and h(0)=epsilon,h(1)=1 fail. Unary complete coding passes.

## Comparator and finite prototype controls

All 16,384 ordered pairs of finite binary languages from the universe
{epsilon,0,1,00,01,10,11} were compared by both direct exhaustive colex
comparison and the epsilon-NFA procedure. This includes empty languages,
equality, proper suffixes and nondeterministic epsilon branches. All agree.
The larger prototype checks are documented in membership-check.json and the
resolution note. They bound finite observations explicitly and do not replace
the theorem's proof.

## Failed/insufficient routes preserved

- **observed-failure:** the first run of check_exact_certificates.py completed
  the 16,384 comparator checks but failed the branching family's separation
  assertion. The manually entered direction had been `decreasing`; computing
  rev(00)<rev(1010) shows the direction is increasing. The direction label was
  corrected and the ENTIRE script rerun successfully. No template, theorem or
  source scope was weakened. This is an implementation-control correction,
  not a counterexample to the structural lemma.
- **proved-obstruction (prior input):** nested turns cannot substitute for
  disjoint interval packing; the supplied positive control remains retained.
- **unknown/insufficient (prior route):** bounded off-diagonal paths alone did
  not control independent prefix-output ranges or interval packing. The valid
  auxiliary pair-component lemma is unused by the new algorithm. Its proof's
  periodic-word argument was checked; no novelty is asserted for that lemma.
- **routine supporting fact:** fixed pump certificates reduce to Presburger
  arithmetic as in the supervisor note; its period/residue and constant-modulus
  comparisons were checked. The new decision algorithm does not depend on a
  Presburger implementation or enumerate certificates before deciding.
- Prior one-piece v1 reasoning, old-v2 criticism, realization/minimization,
  morphism-only controls and rational-relation intersection shortcuts remain
  insufficient for the original question; they have not been reclassified as
  resolutions or removed from the dossier.

## Gap assessment for proposed full resolution

No mathematical gap is currently identified in the SCC proof after these
researcher checks. The full original scope is explicitly covered. A fresh
referee must try to break convexity of blocks, seed propagation, the simple-cycle
annular necessity/sufficiency, the noncommuting-loop construction and the
polynomial resource accounting, and must independently recheck current novelty
and substantive significance. This record is not that referee assessment.
