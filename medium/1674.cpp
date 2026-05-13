// problem: 1674. minimum moves to make array complementary

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

class solution {
public:
  int minmoves(vector<int> &nums, int limit) {
    vector<int> diff(2 * limit + 2, 0);
    int n = nums.size(), iter = n / 2;
    for (int i = 0; i < iter; i++) {
      int mn = min(nums[i], nums[n - 1 - i]);
      int mx = max(nums[i], nums[n - 1 - i]);
      diff[2] += 2;
      diff[mn + 1]--;
      diff[mn + mx]--;
      diff[mn + mx + 1]++;
      diff[mx + limit + 1]++;
    }

    int cur = 0, ret = 0x3f3f3f3f;
    iter = 2 * limit + 1;
    for (int i = 2; i < iter; i++) {
      cur += diff[i];
      if (cur < ret) {
        ret = cur;
      }
    }

    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
