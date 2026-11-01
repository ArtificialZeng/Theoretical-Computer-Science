import fs from 'node:fs';import path from 'node:path';import crypto from 'node:crypto';
import {parseTS,graphStats,parseScala} from './frontends.mjs';import {subtype} from './core.mjs';
const dir=process.argv[2];if(!dir)throw Error('pass pinned corpus root');
let files=[];function walk(d){for(let x of fs.readdirSync(d,{withFileTypes:true})){let f=path.join(d,x.name);if(x.isDirectory())walk(f);else if(f.endsWith('.d.ts'))files.push(f);}}walk(dir);files.sort();
let rows=[],total=0,accepted=0,hist={},statehist={},digest=crypto.createHash('sha256'),queries=[];
for(let file of files){let text=fs.readFileSync(file,'utf8');digest.update(path.relative(dir,file));digest.update('\0');digest.update(text);let {g,roots,total:t}=parseTS(text,file);total+=t;accepted+=roots.length;
 for(let r of roots){let st=graphStats(g,r.id);rows.push({file:path.relative(dir,file),name:r.name,...st});hist[st.back]=(hist[st.back]||0)+1;let bin=st.states<=4?'1-4':st.states<=16?'5-16':st.states<=64?'17-64':'65+';statehist[bin]=(statehist[bin]||0)+1;}
 // Adjacent accepted declarations: an explicitly artificial workload, never labeled compiler queries.
 for(let j=1;j<roots.length&&queries.length<10000;j++){let start=process.hrtime.bigint(),v=subtype(g,g,roots[j-1].id,roots[j].id),ns=Number(process.hrtime.bigint()-start);queries.push({...v,ns});}
}
let sorted=queries.map(x=>x.ns).sort((a,b)=>a-b),quant=p=>sorted[Math.min(sorted.length-1,Math.floor(p*sorted.length))];
let summary={files:files.length,topLevelCandidates:total,accepted,corpusDigest:digest.digest('hex'),backedgeHistogram:hist,quotientHistogram:statehist,queries:queries.length,queryNs:{p50:quant(.5),p90:quant(.9),p99:quant(.99)},node:process.version};
fs.writeFileSync(new URL('corpus-summary.json',import.meta.url),JSON.stringify(summary,null,2));fs.writeFileSync(new URL('corpus-roots.json',import.meta.url),JSON.stringify(rows));fs.writeFileSync(new URL('corpus-queries.json',import.meta.url),JSON.stringify(queries));console.log(summary);
