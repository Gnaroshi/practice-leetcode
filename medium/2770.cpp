// problem: 2770. Maximum Number of Jumps to Reach the Last Index

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
  int maximumJumps(vector<int> &nums, int target) {
    int n = nums.size();
    vector<int> dp(n, -1);
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
      if (dp[i] != -1) {
        for (int j = i + 1; j < n; j++) {
          if (abs(nums[j] - nums[i]) <= target) {
            dp[j] = max(dp[j], dp[i] + 1);
          }
        }
      }
    }

    return dp.back();
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
