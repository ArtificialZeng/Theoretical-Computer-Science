import fs from 'node:fs';import os from 'node:os';
import {ovGraphs,subtype} from './core.mjs';import {runMuSub} from './pipeline.mjs';
const median=x=>[...x].sort((a,b)=>a-b)[Math.floor(x.length/2)];
let rows=[];
for(let N of [16,32,64,128,256]){
 let L=Math.log2(N),bits=i=>i.toString(2).padStart(L,'0').split('').map(Number);
 let A=Array.from({length:N},(_,i)=>[...bits(i),...Array(L).fill(0),1]),B=Array.from({length:N},(_,i)=>[...Array(L).fill(0),...bits(i),1]);
 let {g,h,s,t}=ovGraphs(A,B),nv=g.nodes.length+h.nodes.length,ne=[...g.nodes,...h.nodes].reduce((sum,v)=>sum+Object.keys(v.edges).length,0);
 for(let k=0;k<2;k++){subtype(g,h,s,t);runMuSub(g,h,s,t);}
 let samples=[];
 for(let k=0;k<7;k++){
  let start=process.hrtime.bigint(),baseline=subtype(g,h,s,t),baselineMs=Number(process.hrtime.bigint()-start)/1e6;
  let optimized=runMuSub(g,h,s,t);if(!baseline.ok||!optimized.ok)throw Error('stress answer');
  samples.push({baselineMs,baselinePairs:baseline.pairs,...optimized});
 }
 let first=samples[0],r=Math.min(...first.quotient),quotientProductBound=2*first.quotient[0]*first.quotient[1];
 if(first.pairs>quotientProductBound)throw Error('quotient state bound');
 rows.push({N,d:2*L+1,nv,ne,n:nv+ne,r,quotient:first.quotient,baselinePairs:first.baselinePairs,quotientPairs:first.pairs,quotientProductBound,
 baselineMs:median(samples.map(x=>x.baselineMs)),equalityMs:median(samples.map(x=>x.equalityMs)),minimizationMs:median(samples.map(x=>x.minimizationMs)),searchMs:median(samples.map(x=>x.searchMs)),totalMs:median(samples.map(x=>x.totalMs)),samples});
}
const out={release:'musub-r2',date:'2026-10-31',node:process.version,cpu:os.cpus()[0].model,arch:os.arch(),repetitions:7,warmup:2,method:'sparse smaller-half splitter',rows};
fs.writeFileSync(new URL('bench-results.json',import.meta.url),JSON.stringify(out,null,2));console.log(rows.map(({samples,...r})=>r));
