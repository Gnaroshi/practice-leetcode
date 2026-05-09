// problem: 118. Pascal's Triangle

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
  vector<vector<int>> generate(int numRows) {
    vector<vector<int>> ret;
    if (numRows >= 1) {
      ret.push_back(vector<int>(1, 1));
    }
    if (numRows >= 2) {
      ret.push_back(vector<int>(2, 1));
    }

    for (int i = 3; i <= numRows; i++) {
      vector<int> t(i, 0);
      t[0] = 1;
      t[i - 1] = 1;

      for (int j = 1; j < i - 1; j++) {
        t[j] = ret[i - 2][j - 1] + ret[i - 2][j];
      }
      ret.push_back(t);
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
