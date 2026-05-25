// problem: 1871. Jump Game VII

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
  bool canReach(string s, int minJump, int maxJump) {
    int n = s.size(), cur, mx = 0, st, ed;
    if (s.back() != '0') {
      return false;
    }
    vector<bool> chk(n, false);
    chk[0] = true;
    queue<int> q;
    q.push(0);
    while (!q.empty()) {
      cur = q.front();
      q.pop();
      st = max(cur + minJump, mx + 1);
      ed = min(cur + maxJump, n - 1);

      for (int i = st; i <= ed; i++) {
        if (s[i] == '0') {
          q.push(i);
          chk[i] = true;
        }
      }

      mx = max(mx, ed);
    }
    return chk.back();
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
