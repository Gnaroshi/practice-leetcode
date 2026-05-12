// problem: 1665. Minimum Initial Energy to Finish Tasks

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
  int minimumEffort(vector<vector<int>> &tasks) {
    sort(tasks.begin(), tasks.end(),
         [](const vector<int> &a, const vector<int> &b) {
           return (a[1] - a[0]) < (b[1] - b[0]);
         });
    int cur = 0;
    for (auto i : tasks) {
      cur = max(cur + i[0], i[1]);
    }
    return cur;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
