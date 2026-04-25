// problem: 28. Find the Index of the First Occurrence in a String

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
  int strStr(string haystack, string needle) {
    bool chk = false;
    int idx = -1;
    int hsl = haystack.size(), nl = needle.size();
    if (nl > hsl) {
      return -1;
    }
    hsl -= nl;
    for (int i = 0; i <= hsl; i++) {
      if (needle == haystack.substr(i, nl)) {
        chk = true;
        idx = i;
        break;
      }
    }
    return idx;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
