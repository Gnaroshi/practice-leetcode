// problem: 2657. Find the Prefix Common Array of Two Arrays

#include <algorithm>
#include <cmath>
#include <iostream>
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
  vector<int> findThePrefixCommonArray(vector<int> &a, vector<int> &b) {
    int n = a.size();
    vector<int> ret(n, 0);
    vector<bool> ba(n + 1, false), bb(n + 1, false);
    if (a[0] == b[0]) {
      ret[0]++;
    }
    ba[a[0]] = true;
    bb[b[0]] = true;

    for (int i = 1; i < n; i++) {
      ret[i] = ret[i - 1];
      if (a[i] == b[i]) {
        ret[i]++;
      }
      if (ba[b[i]]) {
        ret[i]++;
      }
      if (bb[a[i]]) {
        ret[i]++;
      }
      ba[a[i]] = true;
      bb[b[i]] = true;
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
