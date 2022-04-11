#include <bits/stdc++.h>
using namespace std;
using Graph = vector<vector<int>>;

vector<bool> seen, finished;

int pos = -1;
stack<int> hist;

void dfs(const Graph &G, int v, int p) {
  seen[v] = true;
  hist.push(v);
  for (auto nv : G[v]) {
    if (nv == p) continue;

    if (finished[nv]) continue;

    if (seen[nv] && !finished[nv]) {
      pos = nv;
      return;
    }

    dfs(G, nv, v);

    if (pos != -1) return;
  }
  hist.pop();
  finished[v] = true;
}

int main() {
  int N;
  cin >> N;

  Graph G(N);
  for (int i = 0; i < N; ++i) {
    int a, b;
    cin >> a >> b;
    --a, --b;
    G[a].push_back(b);
    G[b].push_back(a);
  }

  seen.assign(N, false), finished.assign(N, false);
  pos = -1;
  dfs(G, 0, -1);

  set<int> cycle;
  while (!hist.empty()) {
    int t = hist.top();
    cycle.insert(t);
    hist.pop();
    if (t == pos) break;
  }

  int Q;
  cin >> Q;
  for (int _ = 0; _ < Q; ++_) {
    int a, b;
    cin >> a >> b;
    --a, --b;
    if (cycle.count(a) && cycle.count(b))
      cout << 2 << endl;
    else
      cout << 1 << endl;
  }
}
