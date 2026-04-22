// problem: 14. Longest Common Prefix

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
  string longestCommonPrefix(vector<string> &strs) {
    bool chk = true;
    string ret = "";
    char c;
    int siter = 0x3f3f3f3f, iter = strs.size();
    for (int i = 0; i < iter; i++) {
      siter = min(siter, (int)strs[i].size());
    }
    for (int i = 0; i < siter; i++) {
      c = strs[0][i];
      for (int j = 1; j < iter; j++) {
        if (c != strs[j][i]) {
          chk = false;
          break;
        }
      }
      if (!chk) {
        break;
      }
      ret += c;
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
