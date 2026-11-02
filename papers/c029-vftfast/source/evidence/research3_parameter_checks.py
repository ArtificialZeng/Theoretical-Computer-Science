#!/usr/bin/env python3
"""Exact rational checks of the displayed packing-transfer parameters.

Finite checks supplement the inequalities proved in research3-resolution.md.
"""
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json

def main():
    total=0
    etas=[Fraction(1,4),Fraction(1,8),Fraction(1,10),Fraction(1,100),Fraction(2,9)]
    for k in range(4,4097):
        d=isqrt(k);t=d+(d*d<k)
        for eta in etas:
            a,b=eta.numerator,eta.denominator
            R=isqrt(k*b*b//(a*a))
            R+=R*R*a*a<k*b*b
            s=2*R-1
            r=(12*k*b+a-1)//a
            assert d*s<=r
            assert (d+1)-eta*R*(1+Fraction(1,t))<=1
            assert (1-Fraction(R,k))*(1+Fraction(1,t))<=1
            assert d*s+2*R<=Fraction(4*k,eta)
            assert (2*R+d)**2*eta**2<=9*k
            assert 9*(2*t-1)**2<=64*k
            assert d+1<=2**d
            total+=1
    out=dict(job_id='c029-vftfast-research-9df2f29ab673',
        k_range=[4,4096],eta_values=[str(x) for x in etas],parameter_cases=total,
        inequalities_per_case=7,failures=0,
        scope='Exact finite rational tests of critical-edge scale, q/N exponents, and source triangle-inequality constants; universal justification is in the proof record.')
    Path('evidence/research3-parameter-checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
