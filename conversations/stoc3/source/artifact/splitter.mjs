import {Graph,reach,signature} from './core.mjs';
// Sparse smaller-half partition refinement for deterministic labeled graphs.
// Map/Set operations use the JavaScript runtime; counters expose graph work.
export function minimizeSplitter(g,root){
  const ids=reach(g,root),blocks=[],owner=new Map(),initial=new Map(),incoming=new Map();
  const work=[],stats={incomingEdgeVisits:0,splitterVertexVisits:0,movedVertices:0,splits:0};
  function newBlock(vertices){const b={members:new Set(vertices),pending:false};blocks.push(b);return b;}
  function enqueue(b){if(!b.pending){b.pending=true;work.push(b);}}
  for(const v of ids){const k=signature(g.nodes[v]);if(!initial.has(k))initial.set(k,newBlock([]));const b=initial.get(k);b.members.add(v);owner.set(v,b);incoming.set(v,[]);}
  for(const u of ids)for(const [label,v] of Object.entries(g.nodes[u].edges))incoming.get(v).push([label,u]);
  for(const b of blocks)enqueue(b);
  while(work.length){
    const splitter=work.pop();splitter.pending=false;
    // Snapshot all predecessor sets before any split mutates this splitter.
    const byLabel=new Map();
    for(const v of splitter.members){stats.splitterVertexVisits++;for(const [label,u] of incoming.get(v)){stats.incomingEdgeVisits++;if(!byLabel.has(label))byLabel.set(label,[]);byLabel.get(label).push(u);}}
    for(const sources of byLabel.values()){
      const affected=new Map();
      for(const u of sources){const b=owner.get(u);if(!affected.has(b))affected.set(b,[]);affected.get(b).push(u);}
      for(const [b,marked] of affected){
        if(marked.length===b.members.size)continue;
        const wasPending=b.pending,c=newBlock(marked);stats.splits++;
        for(const u of marked){b.members.delete(u);owner.set(u,c);stats.movedVertices++;}
        if(wasPending)enqueue(c); // The old queue entry now denotes the complement.
        else enqueue(c.members.size<=b.members.size?c:b);
      }
    }
  }
  const index=new Map(blocks.map((b,i)=>[b,i]));
  const z=new Graph();z.nodes=[];
  for(const b of blocks){const u=b.members.values().next().value,v=g.nodes[u];z.nodes.push({...v,edges:Object.fromEntries(Object.entries(v.edges).map(([k,t])=>[k,index.get(owner.get(t))]))});}
  return {g:z,root:index.get(owner.get(root)),size:z.nodes.length,classes:new Map(ids.map(v=>[v,index.get(owner.get(v))])),stats};
}
