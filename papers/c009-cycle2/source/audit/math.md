# Fresh referee assessment

Job: `c009-cycle2-referee-eb6d40fb0393`. Review date: 2026-11-01 UTC.
Submitted snapshot: `06b470c27e7195c3ffb2ba0d198581e77aa79d1b5d87d6485d396b6af906d1bc`.

**Disposition: ACCEPT. The required structural check-math gate passed.** The exact submitted full-scope resolution, global inequality, equality characterization and optimal-exponent forcing statement are correct. The independently checked primary literature supports a substantive, nonroutine contribution at this scope. A transient instruction-file mismatch was resolved before this final decision; the initial nonacceptance and actual failed gate are preserved as historical records, not hidden or recast as a successful audit.

## Reading boundary and freeze check

I read the assigned skill/referee/contract instructions, current project instructions and publication policy, `source.md`, `problem.md`, `claim.json`, `audit/snapshot.json`, and relevant files listed by that snapshot. I did not read checkpoint, state, earlier audit verdicts, job transcripts or owner progress summaries. I also checked actual primary statements online. No agent or other worker was launched.

The initial rehash of all 21 inputs found exactly one mismatch: `AGENTS.md`. The snapshot records `142e7b7b82bb76e4a604bd9fdc65b0db64dbbca6812d5dea7a8842efcb67c1f0`, while the then-current file hashed to `a0404fd94d6b4ac15cc3ae55e95d7d4e7c37589e5c69884c094c53e73d98a9ff`. The bytes preceding the appended “Additional primary-literature update” paragraph hash exactly to the frozen value. The initial mismatch made acceptance unavailable at that time. At the final integrity check, the current AGENTS.md had returned to the exact frozen hash, and the snapshot digest and all other input hashes were unchanged. I did not write that restoration, change the snapshot or re-freeze evidence. I do not infer who restored the file. The transient extra paragraph only directed attention to an already cited primary source, which I checked independently; it changed no mathematical statement. The reviewed packet now exactly matches the original freeze, so the initial integrity objection is resolved without accepting revised mathematics. `source.md` remains byte-for-byte unchanged, SHA-256 `d0dbd81f856b64b6fc49f3e0a0d9242427573bf2460ba28a4f3c1beb93ed635d`.

## Original scope and reconstruction of the main proof

The primary source's weighted-host definition, Definition 3.1, directed-subdivision convention and Problem 3.23 agree with the frozen reading: every integer ell >= 1, every host size n >= 1, and all sufficiently small spectral perturbations of weighted tournaments. The density sums over all vertex maps. The candidate claims a global bound for every weighted host, plus an equality characterization and forcing modulus. I assessed all these claims, not a single cycle length or just regular hosts.

Let u be unit, P=uu^T, B^T=-B and T=P/2+B. With b=Bu, a=||b||^2 and D the skew compression to u-perp, the blocks of T are [1/2,-b^T;b,D]. This reduction is classical. For x=u+2b, direct multiplication gives

    (T^T)^2 x = u/4 -(1/2+2a)b + Db + 2D^2b.

I checked the first coordinate independently: it is (1/2)(1/2+2a)-a=1/4. The remaining squared norm expands using b^TDb=(Db)^TD^2b=0 and b^TD^2b=-||Db||^2. In particular the coefficient of ||Db||^2 is 1+4(1/2+2a)=3+8a. Therefore

    ||(T^T)^2x||^2-||x||^2/16
      = 2a^2+4a^3+(3+8a)||Db||^2+4||D^2b||^2 >= 0.

There is no zero-vector issue since ||x||^2=1+4a. For Q=T^2(T^T)^2 this proves

    lambda_1(Q) >= 1/16+2a^2/(1+4a).

For a weighted tournament use u=1/sqrt(n), B=(A-J/2)/n and T=A/n. Expanding the cyclic trace directly assigns T to clockwise edges and T^T to counterclockwise edges. Hence the (++--) repeated ell times density is exactly tr(Q^ell), with all coincidences and the normalization already included. Since Q is positive semidefinite, tr(Q^ell)>=lambda_1(Q)^ell>=16^(-ell) for every ell>=1. This is a global affirmative answer to the entire immutable local question. No limit, injectivity adjustment, dimension-dependent loss or uniformity assumption is being concealed. The n=1 and ell=1 cases are included.

## Forcing, equality and exponent

Squaring T, the lower blocks are y=b/2+Db and R=D^2-bb^T. The compression of Q is yy^T+R^2. Put K=-R=-D^2+bb^T >= -D^2 >= 0. When D is nonzero, the top eigenspace F of -D^2 has dimension at least two and eigenvalue d^2, where d=||D||. For z in F, z^TKz>=d^2||z||^2, so ||Kz||>=d^2||z||. Consequently z^TQz>=d^4||z||^2. The min-max principle in the full space gives lambda_2(Q)>=d^4. This does not square a Loewner inequality, which would be invalid in general. D=0 only requires positivity; n=1 is handled separately with B=0.

It follows that E=tr(Q^ell)-16^(-ell) satisfies both E>=d^(4ell) and E>=2ell*16^(-(ell-1))*a^2/(1+4a). The entry bound gives beta=||B||<=||B||HS<=1/2, a<=1/4 and beta<=d+sqrt(a). If d>=beta/2 the first estimate gives E>=16^(-ell)beta^(4ell). Otherwise a>beta^2/4 and the second gives E>=ell*16^(-ell)beta^4>=16^(-ell)beta^(4ell). Thus the frozen constant and exponent are correct. Equality in the density bound forces beta=0 and conversely B=0 gives equality. The stated cut-norm comparison follows directly from indicator-vector Cauchy–Schwarz, and beta<=2E^(1/(4ell)) has the correct constant.

For the specified three-vertex cyclic skew matrix K0 and A=J/2+rK0, Bu=0, beta=r/sqrt(3) and Q=P/16+B^4. The two other eigenvalues of Q are beta^4, giving E=2beta^(4ell). Sending r to zero disproves every proposed positive-constant lower bound with exponent below 4ell at each fixed ell. This is exponent optimality in the precisely stated spectral formulation, not a claim about the best constant.

## Checks actually performed

The standard-library verifier `audit/referee_verify.py` imports no proposer code. It checks 96 new rational residual identities and 96 compression identities in dimensions 1 through 8, including b=0 and D=0; separately enumerates every vertex map in 15 new hosts with n<=3; checks the exact forcing inequality there using the exact skew norm formula in dimensions <=3; and verifies 15 sharpness identities at lengths through ell=13. All passed. These are diagnostics supplementary to the analytic proof above.

The first verifier attempt failed at import because sympy was unavailable; its source is preserved as `referee_verify_sympy_unavailable.py`. No checks ran then. One replacement patch was rejected without execution. The completed verifier uses only the standard library. Neither operational failure was treated as mathematical evidence.

`audit/referee_prior_criterion.py` freshly enumerates selected-edge connected components, rather than running the proposer script. It reproduces the frozen coefficients and rational Theorem 12 expression bounds at lengths 4,8,12,16. The sufficient criterion applies at 4,8,12 and fails at 16. This is a statement about that criterion alone, not a theorem of novelty or a negative result about the cycle.

## Current novelty and theoretical significance

The detailed checked-source comparison is in `audit/referee-literature.md`. I independently read the actual McDonald–Psarrakos–Tsatsomeros (2004) author-uploaded primary text, including (3.2) and Theorem 3.7. Their singular-value estimate is for T, not T^2. Submultiplicativity cannot power a lower bound in the desired direction, and T^2 need not have rank-one symmetric part. The new certificate is not supplied by those displayed results.

Grzesik–Il'kovic–Kielak–Kral' Theorem 12 gives the credited short cases and a general sufficient criterion, but not an identified all-length implication. Fox–Himwich–Mani–Zhou Theorem 1.5 / Theorem 4.2 requires a homomorphism to a directed edge. The family has mixed vertices, so this hypothesis fails. Their parallel two-edge-path family is different after ell=1. Current 2026 sources inspected concern trees/paths, target tournaments in nearly regular hosts, or upper bounds on pure directed-cycle traces. None of the inspected statements implies this mixed-trace lower bound. A newly inspected 2026 sectorial-power source also has a strict-sector hypothesis and fractional powers; it supplies no direct implication here.

On that bounded comparison, this is a substantive advance: it answers an explicitly posed entire infinite family globally and gives optimal-exponent spectral forcing. The short Rayleigh computation supplies a dimension-free singular-value bound for the square that the known first-power estimate does not provide. The stability argument extracts a second spectral direction, so this is more than relabeling a known norm bound. No routine prior implication or equivalent theorem was identified. I do not infer STOC suitability or acceptance from this assessment. Old Friedland and Perron-eigenspace leads remain incompletely inspected, and the search is not an exhaustive priority certificate.

## Final verdict and release boundary

No correctness, original-scope or substantive-contribution gap was found. All frozen inputs again match the original snapshot. I accept the submitted resolution-paper scope: the complete original family is affirmatively resolved, with the stronger global inequality, equality characterization and optimal-exponent spectral forcing. `audit/innovation.json` gives the required reasoned contribution assessment. The current acceptance supersedes the preserved transient rejection because its sole integrity defect has actually disappeared; no claim, proof or frozen snapshot was changed by this referee. The required check-math command is run on this actual acceptance and its successful output retained in `audit/referee-gate-check.json`. Writing remains a separate dispatched phase; this referee job creates no manuscript or PDF. This is a local model review, not external peer review, a formal truth certificate, or a prediction of venue acceptance.
