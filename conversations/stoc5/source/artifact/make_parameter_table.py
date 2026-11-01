#!/usr/bin/env python3
from pathlib import Path
import json,gzip,collections,hashlib
b=Path(__file__).resolve().parent;j=json.loads((b/'results.json').read_text());e=json.loads((b/'elina_results.json').read_text())
params=[
('Parity/model',r'$n\in[1,6]$; $[-7,8]$ weights; uniform arc draws, then coherent mates'),
('Integer enumeration',r'$n\in[1,3]$; $[-5,5]$ weights; unary box $[-3,3]^n$'),
('Static product',r'$r\in[1,8]$, $n=3r$; dense $A,B\in[-20,20]^{r\times r}$'),
('Incremental product',r'$r\in[1,6]$, $n=4r$; $A,B\in[-9,9]^{r\times r}$; all prefixes'),
('Elimination',r'$N\in[2,23]$; arc probability $0.15$; $w=c+h_v-h_u$, $c\in[0,9]$, $h\in[-20,20]$'),
('Direct embedding',r'$N\in[1,9]$; arc probability $0.3$; integer weights $[-9,9]$')]
lines=[r'\begin{tabularx}{\textwidth}{@{}P{.20\textwidth}Y P{.13\textwidth}P{.18\textwidth}@{}}',r'\toprule',r'Family / cases & Generation ranges & Observed $m$ & F/I: $\Q$; $\Z$\\',r'\midrule']
for row,(name,desc) in zip(j['rows'],params):
 p=row['parameters'];c=row['cases'];fq=p['rational_feasible'];fz=p['integer_feasible']
 lines.append(name+' / '+str(c)+' & '+desc+' & '+str(p['m']['min'])+'--'+str(p['m']['max'])+' & '+f'{fq}/{c-fq}; {fz}/{c-fz}'+r'\\')
lines.append('ELINA kernel / 1000 & '+r'$n\in[1,16]$; potential $[-40,40]$, slack $[0,8]$; arc probability $0.2$'+' & '+str(e['m_min'])+'--'+str(e['m_max'])+' & '+r'1000/0; ---\\')
lines += [r'\bottomrule',r'\end{tabularx}']
(b/'parameter_table.tex').write_text('\n'.join(lines)+'\n')
# Recompute counts and matrix-entry total from the archived records, rather than trusting the summaries.
reference=[json.loads(s) for s in gzip.decompress((b/'reference_cases.jsonl.gz').read_bytes()).splitlines()]
elina=[json.loads(s) for s in gzip.decompress((b/'elina_cases.jsonl.gz').read_bytes()).splitlines()]
assert len(reference)==j['total_cases']==7250
for row in j['rows']:
 records=[r for r in reference if r['suite']==row['suite']];stats=row['parameters']
 assert len(records)==row['cases']
 assert sum(r['rational_feasible'] for r in records)==stats['rational_feasible']
 assert sum(r['integer_feasible'] for r in records)==stats['integer_feasible']
 for key in ['n','N','m']:
  assert min(r[key] for r in records)==stats[key]['min']
  assert max(r[key] for r in records)==stats[key]['max']
assert len(elina)==e['cases']==1000
assert sum(x['entries'] for x in elina)==e['entries_compared']==389512
assert all(x['status']=='pass' for x in reference+elina)
(b/'coverage.json').write_text(json.dumps({'reference_cases':len(reference),'original_five_suites':6750,'new_direct_embedding_cases':500,'elina_cases':len(elina),'elina_entries':sum(x['entries'] for x in elina),'elina_n_distribution':dict(collections.Counter(x['n'] for x in elina)),'all_status_pass':True},indent=2)+'\n')
print('Coverage recomputed from archived cases:',len(reference),len(elina),e['entries_compared'])
