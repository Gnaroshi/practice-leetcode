// problem: 2540. Minimum Common Value

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
  int getCommon(vector<int> &nums1, vector<int> &nums2) {
    int idx1 = 0, idx2 = 0;
    int l1 = nums1.size(), l2 = nums2.size();

    while (idx1 < l1 && idx2 < l2) {
      if (nums1[idx1] == nums2[idx2]) {
        return nums1[idx1];
      }
      if (nums1[idx1] > nums2[idx2]) {
        idx2++;
      } else {
        idx1++;
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
