# Writing citation map and limitations

Job: curvature-noise-write-cf9542198fc2. This is an authoring aid for the
fresh release reviewer, not a citation acceptance audit. No authoritative
user Excel workbook or BibTeX table was supplied; see
`literature/user_bibliography_check.md`, read before PDF generation.

## Cited records and supported prose

- HorelSinger16: Thibaut Horel and Yaron Singer, original NIPS 2016 paper.
  Official proceedings metadata rechecked. Frozen original extracted fulltext
  is `evidence/horel-singer-nips2016.txt`; original source PDF is in the
  literature directory. Section 2.1 eq. (3) supports the capped-rank and
  transcript attribution. Proposition 8 supports the known singleton method
  and its noisy-objective factor. The true-objective improvement is proved
  in the manuscript and credited as elementary. The 2024 arXiv deposit is
  not represented as a new publication.
- SVW14: author-controlled arXiv:1311.4728v3, revised 2014. Metadata rechecked
  at https://arxiv.org/abs/1311.4728. Theorems 6.1/7.1 and Section 7 were
  inspected in the accepted research/referee evidence. Used for exact-oracle
  benchmark with accuracy slack and prior modular curvature tuning. The
  bib entry cites this precise version, avoiding unrefreshed publisher DOI.
- HassidimSinger17: official PMLR 65:1069--1122 (2017) metadata rechecked at
  https://proceedings.mlr.press/v65/hassidim17a.html. Theorem 8 and Section 5
  were inspected by the mathematical referee for randomized adversarial
  noise hardness and its different cardinality regime.
- BCFLL25: full five authors and arXiv:2510.21128v2 record refreshed at
  https://arxiv.org/abs/2510.21128. Section 2 was inspected during the
  accepted research/referee passes for unbiasedness and independence across
  distinct sets. Used only to explain the different noise contract.

## Limits

The adjacent Gong--Liu--Geng--Fang publisher abstract was inspected by the
referee; its theorem fulltext remains unavailable in that preview. The
manuscript makes no claim about its exact constants or missing theorems,
and does not cite it to support an unsupported comparison. The bounded
literature screen in `evidence/research-literature.md` and `audit/math.md`
is not a priority certificate. Source access limitations are retained here
instead of presenting absence of a record as a mathematical finding.

Fresh citation/build/visual release review remains pending.
