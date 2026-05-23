// problem: 33. Search in Rotated Sorted Array

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

// class Solution {
// public:
//   int search(vector<int> &nums, int target) {
//     auto idx = find(nums.begin(), nums.end(), target);
//     if (idx == nums.end()) {
//       return -1;
//     }
//     return idx - nums.begin();
//   }
// };

class Solution {
public:
  int search(vector<int> &nums, int target) {
    int l = 0, r = nums.size() - 1, md;
    while (l < r) {
      md = l + (r - l) / 2;
      if (nums[md] > nums[r]) {
        l = md + 1;
      } else {
        r = md - 1;
      }
    }
    int ans = bns(nums, 0, l - 1, target);
    return (ans != -1 ? ans : bns(nums, l, nums.size() - 1, target));
  }

private:
  int bns(vector<int> &nums, int lb, int rb, int tgt) {
    int l = lb, r = rb, md;
    while (l <= r) {
      md = l + (r - l) / 2;
      if (nums[md] == tgt) {
        return md;
      } else if (nums[md] > tgt) {
        r = md - 1;
      } else {
        l = md + 1;
      }
    }
    return -1;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
