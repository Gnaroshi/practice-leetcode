// problem: 2144. Minimum Cost of Buying Candies With Discount

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
  int minimumCost(vector<int> &cost) {
    sort(cost.begin(), cost.end(), greater<>());
    int ans = 0, iter = cost.size(), left = iter % 3;
    for (int i = 2; i < iter; i += 3) {
      ans += cost[i - 2] + cost[i - 1];
    }
    for (int i = iter - 1; i >= iter - left; i--) {
      ans += cost[i];
    }

    return ans;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
