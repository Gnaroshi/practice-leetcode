// problem: 1. Two Sum

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
  vector<int> twoSum(vector<int> &nums, int target) {
    int cur, iter = nums.size();
    sort(nums.begin(), nums.end());
    bool chk = false;
    for (int i = 0; i < iter; i++) {
      cur = nums[i];
      for (int j = i + 1; j < iter; j++) {
        if (cur + nums[j] == target) {
          return {i, j};
        }
      }
    }
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
