// problem: 3751. Total Waviness of Numbers in Range I

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
  int totalWaviness(int a, int b) {
    int ans = 0;
    for (int i = max(a, 100); i <= b; i++) {
      string s = to_string(i);
      int iter = s.size() - 1;
      for (int j = 1; j < iter; j++) {
        if (s[j - 1] > s[j] && s[j] < s[j + 1]) {
          ans++;
        } else if (s[j - 1] < s[j] && s[j] > s[j + 1]) {
          ans++;
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
