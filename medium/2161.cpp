// problem: 2161. Partition Array According to Given Pivot

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
  vector<int> pivotArray(vector<int> &nums, int pivot) {
    vector<int> a, b, c, ret;
    for (auto &i : nums) {
      if (i > pivot) {
        c.push_back(i);
      } else if (i < pivot) {
        a.push_back(i);
      } else {
        b.push_back(i);
      }
    }
    ret.reserve(a.size() + b.size() + c.size());
    ret.insert(ret.end(), a.begin(), a.end());
    ret.insert(ret.end(), b.begin(), b.end());
    ret.insert(ret.end(), c.begin(), c.end());
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
