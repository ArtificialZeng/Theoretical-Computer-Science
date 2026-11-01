import {runMuSub} from './pipeline.mjs';
import {Graph,subtype,fixedpoint,equal,minimize,musub,ovGraphs,orthogonal} from './core.mjs';
import fs from 'node:fs';
let counts={exhaustive_ov:0,random_cyclic:0};
const assert=(b,m)=>{if(!b)throw Error(m);};
// All nonempty subsets of {0,1}^2 on each side, then random vector lists.
let vectors=Array.from({length:4},(_,i)=>[i>>1,i&1]);
for(let i=1;i<16;i++)for(let j=1;j<16;j++){
 let A=vectors.filter((_,k)=>i>>k&1),B=vectors.filter((_,k)=>j>>k&1),{g,h,s,t}=ovGraphs(A,B);
 assert(subtype(g,h,s,t).ok===!orthogonal(A,B),'OV reduction');assert(musub(g,h,s,t).ok===!orthogonal(A,B),'minimized OV');assert(runMuSub(g,h,s,t).ok===!orthogonal(A,B),'splitter OV');counts.exhaustive_ov++;
}
let seed=1701;function rng(k){seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed%k;}
for(let trial=0;trial<2000;trial++){
 let make=()=>{let g=new Graph();for(let j=0;j<6;j++)g.add(['rec','fun','atom'][rng(3)],{},'number');for(let j=2;j<8;j++){let x=g.nodes[j];if(x.kind==='fun')x.edges={dom:rng(8),cod:rng(8)};if(x.kind==='rec'){if(rng(2))x.edges.a=rng(8);if(rng(2))x.edges.b=rng(8);}}return g;};
 let g=make(),h=make(),s=rng(8),t=rng(8),truth=fixedpoint(g,h,s,t);
 assert(subtype(g,h,s,t).ok===truth,'cyclic product');assert(musub(g,h,s,t).ok===truth,'cyclic quotient');assert(runMuSub(g,h,s,t).ok===truth,'splitter cyclic quotient');
 // Equality is structural unfolding equality, checked independently by partitioning combined graph.
 let both=new Graph();both.nodes=[...g.nodes,...h.nodes.map(x=>({...x,edges:Object.fromEntries(Object.entries(x.edges).map(([k,v])=>[k,v+8]))}))];let synthetic=both.add('rec',{a:s,b:t+8});let m=minimize(both,synthetic);let eq=equal(g,h,s,t).ok;
 // Pairwise equality using synchronous product without union closure.
 let q=[[s,t]],seen=new Set(),eqtruth=true;while(q.length){let [a,b]=q.pop(),k=`${a},${b}`;if(seen.has(k))continue;seen.add(k);let x=g.nodes[a],y=h.nodes[b];if(x.kind!==y.kind||x.atom!==y.atom||Object.keys(x.edges).sort().join()!==Object.keys(y.edges).sort().join()){eqtruth=false;break;}for(let k of Object.keys(x.edges))q.push([x.edges[k],y.edges[k]]);}
 assert(eq===eqtruth,'union-find equality');counts.random_cyclic++;
}
fs.writeFileSync(new URL('validation.json',import.meta.url),JSON.stringify({seed:1701,counts,passed:true},null,2));console.log(counts);
