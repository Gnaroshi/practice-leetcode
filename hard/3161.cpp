// problem: 3161. Block Placement Queries

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
using ll = long long;

using pii = pair<int, int>;
using pll = pair<ll, ll>;
using vi = vector<int>;
using vvi = vector<vi>;
using vpi = vector<pii>;
using vvpi = vector<vpi>;
using vb = vector<bool>;
using vd = vector<double>;
using vs = vector<string>;
using vll = vector<ll>;
using vvll = vector<vll>;
using vpll = vector<pll>;
using vvpll = vector<vpll>;
using qi = queue<int>;
using si = stack<int>;

class Solution {
public:
  vector<int> seg_tree;
  void update(int idx, int val, int p, int l, int r) {
    if (l == r) {
      seg_tree[p] = val;
      return;
    }
    int md = (l + r) / 2;
    if (idx <= md) {
      update(idx, val, p * 2, l, md);
    } else {
      update(idx, val, p * 2 + 1, md + 1, r);
    }
    seg_tree[p] = max(seg_tree[p * 2], seg_tree[p * 2 + 1]);
  }

  int query(int L, int R, int p, int l, int r) {
    if (L <= l && r <= R) {
      return seg_tree[p];
    }
    int md = (l + r) / 2, ret = 0;
    if (L <= md) {
      ret = max(ret, query(L, R, p * 2, l, md));
    }
    if (R > md) {
      ret = max(ret, query(L, R, p * 2 + 1, md + 1, r));
    }
    return ret;
  }
  vector<bool> getResults(vector<vector<int>> &queries) {
    int mx = 50000;
    seg_tree.resize(mx * 4);
    set<int> st = {0, mx};
    update(mx, mx, 1, 0, mx);
    vector<bool> ans;

    for (auto &q : queries) {
      if (q[0] == 1) {
        int x = q[1];
        auto it = st.upper_bound(x);
        int r = *it, l = *prev(it);
        update(x, x - l, 1, 0, mx);
        update(r, r - x, 1, 0, mx);
        st.insert(x);
      } else {
        int x = q[1];
        int sz = q[2];
        auto it = st.upper_bound(x);
        int bef = *prev(it);
        int mx_space = query(0, bef, 1, 0, mx);
        mx_space = max(mx_space, x - bef);
        ans.push_back(mx_space >= sz);
      }
    }

    return ans;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
