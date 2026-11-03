#include <algorithm>
#include <cstdint>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;
// Independent reachability comparison, simultaneously to up to 64 targets.
int main(){
 int n,m,t,p;if(!(cin>>n>>m>>t>>p))return 1;if(t>64)throw runtime_error("target width exceeded");
 vector<int>a(m),b(m),keep(m),ind(n);vector<vector<int>>out(n);
 for(int e=0;e<m;e++){cin>>a[e]>>b[e]>>keep[e];out[a[e]].push_back(e);ind[b[e]]++;}
 vector<int>S(t),T(t);for(int&i:S)cin>>i;for(int&i:T)cin>>i;
 vector<pair<int,int>>P(p);for(auto&ij:P)cin>>ij.first>>ij.second;
 queue<int>q;for(int v=0;v<n;v++)if(!ind[v])q.push(v);vector<int>order;
 while(!q.empty()){int u=q.front();q.pop();order.push_back(u);for(int e:out[u])if(!--ind[b[e]])q.push(b[e]);}
 if((int)order.size()!=n)throw runtime_error("not a DAG");reverse(order.begin(),order.end());
 vector<uint64_t>base(n),G(n),H(n);for(int i=0;i<t;i++)base[T[i]]|=uint64_t(1)<<i;
 long long failures=0,queries=0;
 for(int f=-1;f<m;f++)for(int g=f;g<m;g++){
  if(f>=0&&g==f)continue;failures++;G=base;H=base;
  for(int u:order)for(int e:out[u])if(e!=f&&e!=g){G[u]|=G[b[e]];if(keep[e])H[u]|=H[b[e]];}
  for(auto ij:P){queries++;if(((G[S[ij.first]]^H[S[ij.first]])>>ij.second)&1){
   cout<<"{\"preserves\":false,\"fault1\":"<<f<<",\"fault2\":"<<g<<",\"source_index\":"<<ij.first<<",\"target_index\":"<<ij.second<<"}\n";return 0;
  }}
 }
 cout<<"{\"preserves\":true,\"fault_sets\":"<<failures<<",\"queries\":"<<queries<<"}\n";
}
