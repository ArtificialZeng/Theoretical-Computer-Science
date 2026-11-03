#include <algorithm>
#include <bitset>
#include <chrono>
#include <iostream>
#include <queue>
#include <stdexcept>
#include <vector>
using namespace std;
// Exact DAG dominators by intersection of predecessor mandatory-edge sets.
// No path counts, floating point, or probabilistic identity checks are used.
const int MAXM=4096;
int main(){
  int n,m,p,c;if(!(cin>>n>>m>>p>>c))return 1;
  if(m>MAXM)throw runtime_error("bitset domain exceeded");
  vector<int> a(m),b(m),ind(n);vector<vector<int>> in(n),out(n);
  for(int e=0;e<m;e++){cin>>a[e]>>b[e];out[a[e]].push_back(e);in[b[e]].push_back(e);ind[b[e]]++;}
  vector<pair<int,int>> P(p);for(auto &st:P)cin>>st.first>>st.second;
  queue<int> q;for(int v=0;v<n;v++)if(!ind[v])q.push(v);
  vector<int> order;while(!q.empty()){int u=q.front();q.pop();order.push_back(u);for(int e:out[u])if(!--ind[b[e]])q.push(b[e]);}
  if((int)order.size()!=n)throw runtime_error("input is not a DAG");
  vector<bitset<MAXM>> dom(n);vector<char> reach(n);vector<char> critical(m);
  vector<int> wf(m,-9),wg(m,-9),wp(m,-1);
  long long failures=0,queries=0;
  for(int f=-1;f<m;f++)for(int g=f;g<m;g++){
    // f=g=-1 means no fault; f=-1,g>=0 means one fault;
    // f>=0,g>f means two DISTINCT faults.
    if(f>=0&&g==f)continue;
    failures++;
    for(int i=0;i<p;i++){
      int s=P[i].first,t=P[i].second;
      fill(reach.begin(),reach.end(),0);reach[s]=1;dom[s].reset();
      for(int v:order){
        if(v==s)continue;
        bool first=true;
        for(int e:in[v])if(e!=f&&e!=g&&reach[a[e]]){
          auto pred=dom[a[e]];pred.set(e);
          if(first){dom[v]=pred;first=false;}else dom[v]&=pred;
        }
        reach[v]=!first;
      }
      queries++;
      if(reach[t])for(int e=0;e<m;e++)if(!critical[e]&&dom[t][e]){
        critical[e]=1;wf[e]=f;wg[e]=g;wp[e]=i;
      }
    }
  }
  cout<<"{\"n\":"<<n<<",\"m\":"<<m<<",\"p\":"<<p<<",\"core_edges\":"<<c
      <<",\"fault_sets\":"<<failures<<",\"demand_queries\":"<<queries<<",\"witnesses\":[";
  bool comma=false;int cc=0,ac=0;
  for(int e=0;e<m;e++)if(critical[e]){ac++;if(e<c)cc++;if(comma)cout<<",";comma=true;
    cout<<"{\"edge\":"<<e<<",\"demand\":"<<wp[e]<<",\"faults\":[";
    if(wf[e]>=0)cout<<wf[e];if(wg[e]>=0){if(wf[e]>=0)cout<<",";cout<<wg[e];}cout<<"]}";
  }
  cout<<"],\"critical_core_edges\":"<<cc<<",\"critical_all_edges\":"<<ac<<",\"noncritical_core_edges\":[";
  comma=false;for(int e=0;e<c;e++)if(!critical[e]){if(comma)cout<<",";comma=true;cout<<e;}
  cout<<"]}\n";
}
