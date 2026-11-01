import fs from 'node:fs';import {Graph,subtype,ovGraphs,orthogonal} from './core.mjs';
function arrows(g,root){let h=new Graph(),memo=new Map([[g.top,h.top],[g.bot,h.bot]]);function enc(x){if(memo.has(x))return memo.get(x);let v=g.nodes[x];if(v.kind!=='rec')throw Error('record input');let ids=[h.add('fun'),h.add('fun'),h.add('fun'),h.add('fun')];memo.set(x,ids[0]);h.nodes[ids[0]].edges={dom:ids[1],cod:ids[2]};h.nodes[ids[1]].edges={dom:enc(v.edges['0']),cod:h.bot};h.nodes[ids[2]].edges={dom:ids[3],cod:enc(v.edges.c)};h.nodes[ids[3]].edges={dom:enc(v.edges['1']),cod:h.bot};return ids[0];}return {g:h,root:enc(root)};}
let vectors=Array.from({length:4},(_,i)=>[i>>1,i&1]),count=0;
for(let i=1;i<16;i++)for(let j=1;j<16;j++){let A=vectors.filter((_,k)=>i>>k&1),B=vectors.filter((_,k)=>j>>k&1),v=ovGraphs(A,B),a=arrows(v.g,v.s),b=arrows(v.h,v.t);if(subtype(a.g,b.g,a.root,b.root).ok!==!orthogonal(A,B))throw Error('arrow reduction');count++;}
function cycle(n){let g=new Graph();for(let i=0;i<n;i++)g.record({a:2+(i+1)%n});return g;}
let a=cycle(17),b=cycle(19),v=subtype(a,b,2,2);if(!v.ok||v.pairs!==17*19)throw Error('orbit');
fs.writeFileSync(new URL('extra-validation.json',import.meta.url),JSON.stringify({arrowReductionCases:count,coprimeCycles:{p:17,q:19,pairs:v.pairs},passed:true},null,2));console.log('Arrow cases:',count,'cycle product:',v.pairs);
