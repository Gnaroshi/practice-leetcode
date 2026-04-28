// problem: 67. Add Binary

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
  string addBinary(string a, string b) {
    string ret = "";
    int al = a.size() - 1, bl = b.size() - 1, cry = 0, t;
    while (al >= 0 || bl >= 0 || cry) {
      t = cry;
      if (al >= 0) {
        t += a[al--] - '0';
      }
      if (bl >= 0) {
        t += b[bl--] - '0';
      }
      ret += to_string(t % 2);
      cry = t / 2;
    }
    reverse(ret.begin(), ret.end());
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
