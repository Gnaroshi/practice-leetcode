// problem: 154. Find Minimum in Rotated Sorted Array II

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
  int findMin(vector<int> &nums) {
    int l = 0, r = nums.size() - 1, md;
    while (l < r) {
      md = (l + r) / 2;
      if (nums[r] > nums[md]) {
        r = md;
      } else if (nums[r] < nums[md]) {
        l = md + 1;
      } else {
        r--;
      }
    }

    return nums[l];
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
