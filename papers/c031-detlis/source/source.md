# Frozen original — deterministic subquadratic 2D range LIS

Karthik C. S. and Saladi Rahul, ITCS2026 Section6, current full
arXiv2404.04795v2 Section7, asks:
"Another interesting research direction is to design a deterministic algorithm
which runs in sub-quadratic time. Specifically, can the construction of
stitching set be efficiently derandomized?"
Primary https://arxiv.org/abs/2404.04795v2 .

Resolve the complete deterministic algorithm question for the paper's
uncolored 2D reporting model: there exist universal epsilon>0,C,B and a
uniform deterministic algorithm that, for EVERY sequence of n arbitrary real
values and m query rectangles (index interval times value interval), reports
a longest strictly increasing subsequence in each rectangle in at most
C*(n+m)*n^(1-epsilon)*log(n+m+2)^B+O(k) operations, where k is total output
length. In particular m=Theta(n) has truly subquadratic overhead. Repeated
values, arbitrary query overlaps, sparse/dense patterns and every LIS length
are included. Input comparisons and O(log(n+m+2))-bit word operations have
unit cost. A stronger deterministic O-tilde((n+m)*sqrt(n))+O(k) bound is
welcome, but a uniform fixed positive exponent saving answers the original.
Offline queries and any tie-consistent optimal witness are allowed.
