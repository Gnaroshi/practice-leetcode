// problem: 13. Roman to Integer

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
  std::map<char, int> mp{{'I', 1},   {'V', 5},   {'X', 10},  {'L', 50},
                         {'C', 100}, {'D', 500}, {'M', 1000}};

public:
  int romanToInt(string s) {
    int iter = s.length(), ret = 0, bef = 0, cur;

    for (int i = iter - 1; i >= 0; i--) {
      cur = mp[s[i]];
      if (cur < bef) {
        ret -= cur;
      } else {
        ret += cur;
      }
      bef = cur;
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
