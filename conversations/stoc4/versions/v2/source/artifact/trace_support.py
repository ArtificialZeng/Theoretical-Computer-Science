"""Deterministic, per-record validation evidence for revision v2."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
COUNTS = Counter()
FILES = {}

def record(kind, **payload):
    if kind not in FILES:
        FILES[kind] = (ROOT/'records'/f'{kind}.jsonl').open('w')
    COUNTS[kind] += 1
    obj = {'id':f'{kind}:{COUNTS[kind]}', 'kind':kind, **payload}
    FILES[kind].write(json.dumps(obj, separators=(',',':'))+'\n')

def close():
    for f in FILES.values():
        f.close()
    return dict(COUNTS)
