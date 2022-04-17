#include <iostream>
#include <queue>
#include <vector>
using namespace std;

using Graph = vector<vector<int>>;
using pint = pair<int, int>;

int N, M;
Graph G;
int s, t;

long long solve() {
  vector<vector<long long>> dist(N, vector<long long>(3, -1));
  dist[s][0] = 0;
  queue<pint> que;
  que.push({s, 0});
  while (!que.empty()) {
    pint cur = que.front();
    que.pop();
    int v = cur.first;
    int parity = cur.second;
    for (auto nv : G[v]) {
      int np = (parity + 1) % 3;
      if (dist[nv][np] == -1) {
        dist[nv][np] = dist[v][parity] + 1;
        que.push({nv, np});
      }
    }
  }
  if (dist[t][0] == -1)
    return -1;
  else
    return dist[t][0] / 3;
}

int main() {
  cin >> N >> M;
  G.assign(N, vector<int>());
  for (int i = 0; i < M; ++i) {
    int u, v;
    cin >> u >> v;
    --u, --v;
    G[u].push_back(v);
  }
  cin >> s >> t;
  --s, --t;
  cout << solve() << endl;
}
