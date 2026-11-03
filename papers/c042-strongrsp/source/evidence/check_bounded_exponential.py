#!/usr/bin/env python3
"""Finite R3 decoder subroutine checks. Decimal checks are explicitly numerical.
Integer dyadic rounding below is a diagnostic convenience; charged bounded
binary comparison implements exactly the same operation in the proof.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import json

def down(x,b): return F((x.numerator*(1<<b))//x.denominator,1<<b)

def upper_exp(k,mu,z,b,q):
    lgq=(q+1).bit_length()
    d=1-z
    J=16*(b+lgq+1)
    power=d; ls=F(0)
    for r in range(1,J+1):
        ls-=power/r; power*=d
    x0=k*ls+d*mu
    T=b+2
    if x0>=T+1: return None,'reject'
    if x0<=-T-1: return F(1,1<<b),'underflow'
    R=1
    while R<8*(T+2): R*=2
    B=100*(b+lgq+1)
    y=down(x0/R,B)
    value=F(1)
    for r in range(16*b,0,-1): value=down(1+y*value/r,B)
    j=R
    while j>1: value=down(value*value,B);j//=2
    return value+F(1,1<<(10*b)),'bounded-series'

def main():
    records=[]
    with localcontext() as ctx:
        ctx.prec=130
        for z in (F(15,16),F(63,64)):
            for k,mu in ((0,F(0)),(0,F(1,4)),(1,F(1,4)),
                         (3,F(8)),(7,F(32))):
                got,branch=upper_exp(k,mu,z,32,8)
                assert branch=='bounded-series'
                dec=lambda a: Decimal(a.numerator)/Decimal(a.denominator)
                ref=(Decimal(k)*dec(z).ln()+(1-dec(z))*dec(mu)).exp()
                gap=dec(got)-ref
                assert Decimal(0)<gap<Decimal(2)**(-300)
                records.append({'z':str(z),'k':k,'mean':str(mu),
                                'branch':branch,'decimal_upper_gap':str(gap)})
        # Exact guard-branch inequalities use exp(x)>1+x for rejection and
        # analytic e>2 for underflow; Decimal is just a finite smoke check.
        got,branch=upper_exp(0,F(10000),F(15,16),32,8)
        assert branch=='reject' and got is None
        got,branch=upper_exp(10000,F(0),F(15,16),32,10001)
        assert branch=='underflow' and got==F(1,1<<32)
    out={'job_id':'c042-strongrsp-research-a3a11d57c4b5',
         'all_checks_passed':True,'series_cases':len(records),'guard_cases':2,
         'records':records,'scope':'Exact rational bounded-precision arithmetic under test; '
         '130-digit Decimal exp/log is numerical reference, NOT a certified interval or proof. '
         'Universal enclosure/error/operation bounds are mathematical obligations in the proof record.'}
    Path('evidence/bounded-exponential-results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'}))

if __name__=='__main__':main()
