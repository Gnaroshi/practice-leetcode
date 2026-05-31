// problem: 2126. Destroying Asteroids

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
  bool asteroidsDestroyed(int mass, vector<int> &asteroids) {
    sort(asteroids.begin(), asteroids.end());
    int iter = asteroids.size();
    long long cur = mass;
    if (cur < asteroids.front()) {
      return false;
    }
    cur += asteroids.front();
    for (int i = 1; i < iter; i++) {
      if (cur < asteroids[i]) {
        return false;
      }
      cur += asteroids[i];
    }
    return true;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
