// problem: 66. Plus One

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
  vector<int> plusOne(vector<int> &digits) {
    bool crr = true;
    int iter = digits.size();
    for (int i = iter - 1; i >= 0; i--) {
      if (crr) {
        if (digits[i] + 1 == 10) {
          crr = true;
          digits[i] = 0;
        } else {
          crr = false;
          digits[i] += 1;
        }
      }
      if (!crr) {
        break;
      }
    }
    if (crr) {
      digits.insert(digits.begin(), 1);
    }
    return digits;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
