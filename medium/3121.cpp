// problem: 3121. Count the Number of Special Characters II
//
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
  int numberOfSpecialChars(string word) {
    int n = word.size(), ret = 0;
    vector<int> locl(26, -1), locu(26, -1);
    char cur;

    for (int i = 0; i < n; i++) {
      cur = word[i];
      if (islower(cur)) {
        locl[cur - 'a'] = i;
      } else {
        if (locu[cur - 'A'] == -1) {
          locu[cur - 'A'] = i;
        }
      }
    }

    for (int i = 0; i < 26; i++) {
      if (locu[i] > locl[i] && locu[i] != -1 && locl[i] != -1) {
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
