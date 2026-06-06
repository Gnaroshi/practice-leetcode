// problem: 2574. Left and Right Sum Differences

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
  vector<int> leftRightDifference(vector<int> &nums) {
    int n = nums.size();
    int ls = 0, rs = accumulate(nums.begin(), nums.end(), 0);
    vector<int> ret(n, 0);
    for (int i = 0; i < n; i++) {
      rs -= nums[i];
      ret[i] = abs(ls - rs);
      ls += nums[i];
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
