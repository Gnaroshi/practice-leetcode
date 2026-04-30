// problem: 69. Sqrt(x)

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
  int mySqrt(int x) {
    if (x <= 1) {
      return x;
    }
    int t, ans = -1;
    for (int i = 1; i <= x; i++) {
      t = i * i;
      if (t == x) {
        ans = i;
        break;
      } else if (x < t) {
        ans = i - 1;
        break;
      }
    }
    return ans;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
