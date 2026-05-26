// problem: 3120. Count the Number of Special Characters 1

#include <algorithm>
#include <cctype>
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
  int numberOfSpecialChars(string word) {
    int ret = 0;
    vector<bool> chka(26, false), chkb(26, false);
    for (const auto &i : word) {
      if (isupper(i)) {
        chka[i - 'A'] = true;
      } else {
        chkb[i - 'a'] = true;
      }
    }

    for (int i = 0; i < 26; i++) {
      if (chka[i] && chkb[i]) {
        ret++;
      }
    }

    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
