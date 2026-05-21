// problem: 3043. Find the Length of the Longest Common Prefix

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
  int longestCommonPrefix(vector<int> &arr1, vector<int> &arr2) {
    int ans = 0;
    unordered_set<string> prefs;
    for (int i : arr1) {
      string s = to_string(i), pref = "";
      for (char c : s) {
        pref += c;
        prefs.insert(pref);
      }
    }
    for (int i : arr2) {
      string s = to_string(i), pref = "";
      for (char c : s) {
        pref += c;
        if (prefs.count(pref)) {
          ans = max(ans, (int)pref.size());
        } else {
          break;
        }
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
