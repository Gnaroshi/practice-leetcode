// problem: 3633. Earliest Finish Time for Land and Water Rides I

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

  int getEarliest(const vector<int> &s1, const vector<int> &d1,
                  const vector<int> &s2, const vector<int> &d2) {
    int n = s1.size(), m = s2.size();
    int ans = 0x3f3f3f3f;

    vector<pair<int, int>> ss2(m);
    for (int i = 0; i < m; i++) {
      ss2[i] = {s2[i], d2[i]};
    }
    sort(ss2.begin(), ss2.end());

    vector<int> min_t(m);
    min_t[m - 1] = ss2[m - 1].first + ss2[m - 1].second;
    for (int i = m - 2; i >= 0; i--) {
      int cur = ss2[i].first + ss2[i].second;
      min_t[i] = min(min_t[i + 1], cur);
    }

    for (int i = 0; i < n; i++) {
      int cur = s1[i] + d1[i];
      int l = 0, r = m - 1, idx = m;
      while (l <= r) {
        int md = l + (r - l) / 2;
        if (ss2[md].first >= cur) {
          idx = md;
          r = md - 1;
        } else {
          l = md + 1;
        }
      }

      if (idx < m) {
        ans = min(ans, min_t[idx]);
      }
    }

    return ans;
  }

public:
  int earliestFinishTime(vector<int> &landStartTime, vector<int> &landDuration,
                         vector<int> &waterStartTime,
                         vector<int> &waterDuration) {
    return min(
        getEarliest(landStartTime, landDuration, waterStartTime, waterDuration),
        getEarliest(waterStartTime, waterDuration, landStartTime,
                    landDuration));
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
