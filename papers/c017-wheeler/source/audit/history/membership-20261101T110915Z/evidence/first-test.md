# First research test: bounded disjoint-turn pumping

Job `c017-wheeler-triage-b86cccc47ffc`. This is an internal unproved hypothesis
to attack, not a theorem, output algorithm, or publication candidate. Research
pass 1 should settle a precise version or exhibit an exact obstruction; do not
spend that pass extending finite input-length controls.

## Precise certificate schema

Assume T passes the literal input-order condition. For a state q, a certificate
consists of nine words x_i,y_i,z_i in Sigma*, i=1,2,3, and two fixed signs.
For n>=0 let U_i(n)=x_i y_i^n z_i. Require ALL of the following for EVERY n:

1. U_i(n) is in I_q, for all i;
2. U_1(n) <co U_2(n) <co U_3(n);
3. either f_q(U_1(n)) <co f_q(U_2(n)) >co f_q(U_3(n)) for every n,
   or the two strict inequalities are reversed for every n;
4. either U_3(n) <co U_1(n+1) for every n, or
   U_3(n+1) <co U_1(n) for every n.

Both choices in items 3 and 4 are part of the certificate. This includes
increasing intervals and decreasing intervals converging to a colex cut. Empty
x_i,y_i,z_i are allowed; strict interval separation ensures genuinely distinct
instances even if an individual y_i is empty. Erasing OUTPUT words remain allowed
everywhere in the input transducer.

**Established sufficiency only:** each interval [U_1(n),U_3(n)] within I_q
contains a strict peak or valley and so cannot lie inside a single weakly
monotone piece. A finite partition into k convex pieces has only k-1 boundaries,
and can split at most k-1 pairwise disjoint ordered intervals. Item 4 makes these
intervals pairwise disjoint. Thus any such certificate implies failure of the
statewise piecewise condition. This proof uses no pumping assumption.

## Hypothesis to prove or refute

There exists a total computable bound B on finite transducer descriptions such
that, whenever T passes input order but fails the statewise piecewise condition,
some state has a certificate above with EACH of its nine words of length at
most B(T). In addition, validity of each finite certificate schema must be
effectively decidable, with a proved terminating universal-n comparison routine.

If both statements hold, finite enumeration of q, words up to B(T), and signs
gives a complete membership algorithm. No B(T), necessity proof, or general
certificate-verification algorithm is currently supplied. A claim that these
relations are rational or that arbitrary rational intersections are decidable
does not fill that gap. Finding a literal failing instance with no certificate
of ANY size refutes necessity; failure up to a size cap does not.

Start with path-state periodicity of x_i y_i^n z_i and the corresponding
periodic output words, then assess whether finite-state output-delay
comparisons suffice. If the single-pump schema is too weak, save the exact
countermodel and failed necessity argument; any revised schema must be explicit
and still address the full original question.

## Literal negative witnesses and positive controls

For both the one-state complement and length-only maps, take

    U_1(n)=00(11)^n, U_2(n)=1(11)^n, U_3(n)=001(11)^n.

Their reversals are respectively 1^(2n)00, 1^(2n+1), and 1^(2n+1)00.
Consequently U_1(n)<co U_2(n)<co U_3(n)<co U_1(n+1).
Complement outputs have a strict valley: their reversals are 0^(2n)11,
0^(2n+1), 0^(2n+1)11. Length-only output lengths are 2n+2, 2n+1, 2n+3,
also giving a strict valley. These are exact all-n witnesses, not finite fits.
Identity, the all-erasing map, and h(0)=0,h(1)=11 have no such certificate by
their global nondecreasingness; see `triage-baseline.md`.

The decisive adversarial tests are state-dependent erasure, delayed output
comparisons, and intervals accumulating in either colex direction. A surviving
schema requires a proof covering these cases, not confidence from controls.
Allow at most three research passes overall, preserving all failed routes.
