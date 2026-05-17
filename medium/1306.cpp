// problem: 1306. Jump Game III

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
  bool canReach(vector<int> &arr, int start) {
    int as = arr.size();
    int cur, nxta, nxtb;
    vector<bool> vist(as, false);
    queue<int> q;
    bool ans = false;
    q.push(start);
    while (!q.empty()) {
      cur = q.front();
      q.pop();
      if (arr[cur] == 0) {
        ans = true;
        break;
      }
      nxta = cur - arr[cur];
      nxtb = cur + arr[cur];
      if (nxta >= 0 && nxta < as) {
        if (!vist[nxta]) {
          vist[nxta] = true;
          q.push(nxta);
        }
      }
      if (nxtb >= 0 && nxtb < as) {
        if (!vist[nxtb]) {
          vist[nxtb] = true;
          q.push(nxtb);
        }
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
