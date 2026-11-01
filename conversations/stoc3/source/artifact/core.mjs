// Deterministic regular-tree subtyping; no heuristic depth limit.
export class Graph {
  constructor(){this.nodes=[];this.top=this.add('top');this.bot=this.add('bot');}
  add(kind, edges={}, atom=''){this.nodes.push({kind,edges,atom});return this.nodes.length-1;}
  record(edges){return this.add('rec',edges);}
}
export function signature(v){return JSON.stringify([v.kind,v.atom,Object.keys(v.edges).sort()]);}
export function reach(g,root){let seen=new Set(),q=[root];while(q.length){let x=q.pop();if(seen.has(x))continue;seen.add(x);q.push(...Object.values(g.nodes[x].edges));}return [...seen];}
export function obligations(g,h,a,b){
  const x=g.nodes[a],y=h.nodes[b];
  if(x.kind==='bot'||y.kind==='top')return [];
  if(x.kind!==y.kind)return null;
  if(x.kind==='top'||x.kind==='bot')return [];
  if(x.kind==='atom')return x.atom===y.atom?[]:null;
  if(x.kind==='fun')return [[x.edges.dom,y.edges.dom,1],[x.edges.cod,y.edges.cod,0]];
  let out=[];for(let k of Object.keys(y.edges)){if(!(k in x.edges))return null;out.push([x.edges[k],y.edges[k],0]);}return out;
}
export function subtype(g,h,s,t){
  let q=[[s,t,0]],seen=new Set(),count=0;
  while(q.length){let [a,b,p]=q.pop(),key=`${a},${b},${p}`;if(seen.has(key))continue;seen.add(key);count++;
    let obs=p?obligations(h,g,b,a):obligations(g,h,a,b);
    if(obs===null)return {ok:false,pairs:count};
    for(let [x,y,flip] of obs)q.push(p?[y,x,p^flip]:[x,y,p^flip]);
  }return {ok:true,pairs:count};
}
// Independently decomposes constructors; intentionally does not call obligations().
export function fixedpoint(g,h,s,t){
  let bad=new Set(),ng=g.nodes.length,nh=h.nodes.length;
  const key=(a,b,p)=>`${a},${b},${p}`;
  for(let changed=true;changed;){changed=false;
    for(let a=0;a<ng;a++)for(let b=0;b<nh;b++)for(let p=0;p<2;p++){
      let k=key(a,b,p);if(bad.has(k))continue;
      let ga=g.nodes[a],hb=h.nodes[b],left=p?hb:ga,right=p?ga:hb,fail=false;
      if(left.kind==='bot'||right.kind==='top')continue;
      if(left.kind!==right.kind)fail=true;
      else if(left.kind==='atom')fail=left.atom!==right.atom;
      else if(left.kind==='fun')fail=bad.has(key(ga.edges.dom,hb.edges.dom,p^1))||bad.has(key(ga.edges.cod,hb.edges.cod,p));
      else if(left.kind==='rec')for(let label of Object.keys(right.edges)){
        if(!(label in left.edges)||bad.has(key(ga.edges[label],hb.edges[label],p))){fail=true;break;}
      }
      if(fail){bad.add(k);changed=true;}
    }
  }return !bad.has(key(s,t,0));
}
export function equal(g,h,s,t){
  const off=g.nodes.length,v=[...g.nodes,...h.nodes.map(x=>({...x,edges:Object.fromEntries(Object.entries(x.edges).map(([k,y])=>[k,y+off]))}))];
  let parent=v.map((_,i)=>i),rank=v.map(()=>0),q=[[s,t+off]],merges=0;
  const find=x=>{while(x!==parent[x]){parent[x]=parent[parent[x]];x=parent[x];}return x;};
  while(q.length){let [a,b]=q.pop(),ra=find(a),rb=find(b);if(ra===rb)continue;if(signature(v[a])!==signature(v[b]))return {ok:false,merges};
    if(rank[ra]<rank[rb])[ra,rb]=[rb,ra];parent[rb]=ra;if(rank[ra]===rank[rb])rank[ra]++;merges++;
    for(let k of Object.keys(v[a].edges))q.push([v[a].edges[k],v[b].edges[k]]);
  }return {ok:true,merges};
}
// Deliberately simple Moore refinement reference, not the O(n log n) splitter implementation.
export function minimize(g,root){
  let ids=reach(g,root),cls=new Map(),groups=new Map();
  for(let i of ids){let k=signature(g.nodes[i]);if(!groups.has(k))groups.set(k,groups.size);cls.set(i,groups.get(k));}
  while(true){let next=new Map(),m=new Map();for(let i of ids){let v=g.nodes[i],key=JSON.stringify([cls.get(i),Object.keys(v.edges).sort().map(k=>[k,cls.get(v.edges[k])])]);if(!m.has(key))m.set(key,m.size);next.set(i,m.get(key));}
    let oldCount=new Set(cls.values()).size;cls=next;if(m.size===oldCount)break;
  }
  let z=new Graph();z.nodes=[];for(let i of ids){let c=cls.get(i),v=g.nodes[i];z.nodes[c]={...v,edges:Object.fromEntries(Object.entries(v.edges).map(([k,j])=>[k,cls.get(j)]))};}
  return {g:z,root:cls.get(root),size:z.nodes.length};
}
export function musub(g,h,s,t){
  if(equal(g,h,s,t).ok)return {ok:true,pairs:0};
  let a=minimize(g,s),b=minimize(h,t),v=subtype(a.g,b.g,a.root,b.root);return {...v,quotient:[a.size,b.size]};
}
// Partial, layered binary automata for word = selector(B) followed by vector(A).
export function ovGraphs(A,B){
  if(!A.length||!B.length)throw Error('nonempty lists required');let d=A[0].length,L=Math.ceil(Math.log2(B.length));
  function trie(words){let tr=[{e:{},accept:false}];for(let w of words){let x=0;for(let c of w){if(!(c in tr[x].e)){tr[x].e[c]=tr.length;tr.push({e:{},accept:false});}x=tr[x].e[c];}tr[x].accept=true;}return tr;}
  let ta=trie(A.map(v=>v.join(''))),sa=0;
  for(let i=0;i<L;i++){ta.push({e:{'0':sa,'1':sa},accept:false});sa=ta.length-1;}
  let tb=trie(B.map((_,i)=>L?i.toString(2).padStart(L,'0'):''));
  B.forEach((v,j)=>{let x=0;for(let c of (L?j.toString(2).padStart(L,'0'):''))x=tb[x].e[c];tb[x].accept=false;for(let i=0;i<d;i++){let y=tb.length;tb.push({e:{},accept:false});tb[x].e={'0':y};if(v[i]===0)tb[x].e['1']=y;x=y;}tb[x].accept=true;});
  function encode(tr,left){let g=new Graph(),offset=g.nodes.length;for(let v of tr)g.record({});tr.forEach((v,i)=>{g.nodes[i+offset].edges={'0':v.e['0']===undefined?(left?g.bot:g.top):v.e['0']+offset,'1':v.e['1']===undefined?(left?g.bot:g.top):v.e['1']+offset,'c':left?(v.accept?g.top:g.bot):(v.accept?g.bot:g.top)};});return {g,offset};}
  let a=encode(ta,true),b=encode(tb,false);return {g:a.g,h:b.g,s:a.offset+sa,t:b.offset};
}
export function orthogonal(A,B){return A.some(a=>B.some(b=>a.every((x,i)=>!x||!b[i])));}
