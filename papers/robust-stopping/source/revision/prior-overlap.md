# Exact overlap with the known one-hot optimizer

The uniform policy family must not be advertised as a new form of stopping
law. KF26 arXiv:2603.29233v1 Appendix C.4 Theorem C.1(ii), specialized to
one-hot forecast y=b, already uses the capped geometric CDF
 F_P(x)=min{G(x),P}, G(x)=r((b/(b-1))^x-1), 0<=x<=b,
with the residual mass at b+1. Its selected P is the smallest solution to
 Phi(P)>=max{b(1-r),Phi(Pcheap)},
where Phi(P)=sum_{x=1}^b min{G(x),P} and Pcheap=min{r/(b-1),1}.

For rho_b-1<=r<=1-1/b we have Pcheap=r/(b-1) and
 Phi(Pcheap)=br/(b-1)<=b(1-r).
The uniform candidate has exactly that CDF up to b, with
 P=sum_{i<=j}f_i. Its moment equality is equivalent to
 Phi(P)=sum_{i<=j}(b+1-i)f_i=b(1-r).
Phi is continuous and strictly increasing before its saturation value;
therefore the uniform P is exactly the P selected in C.1(ii). This is
an analytic identification, not just agreement on finitely many inputs.
For 1-1/b<=r<=1 the uniform optimizer is supported on {1,b+1}, with
f_1=1-r. Both days have one-hot-b cost b, so this is another optimum for
that prior objective (C.1's chosen optimum need not be this law).

Consequently the support pattern on the open first segment, and a route
to sharp support necessity, were already available in the known one-hot
construction. They must be credited as close prior structure. The new
uniform calculation is the exact all-b expected-cost frontier, its full
set of rational breakpoints, strict dual proof of uniqueness under that
forecast, and the explicit simultaneous support-necessity demonstration.
It is not a new geometric recurrence or a new canonical schedule. Whether
this extension is a sufficient structural addition is a question for the
fresh referee; it must not be assumed because an explicit formula exists.
The earlier general corrected optimizer remains the central proposed
contribution of the combined note.

`check_prior_overlap.py` evaluates the C.1 scalar equation directly, with
no call to the general optimizer, and saves the finite checks in
`prior-overlap-checks.json`. These checks supplement the identities above.
