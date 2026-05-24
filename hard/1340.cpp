// problem: 1340. Jump Game V

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
  int maxJumps(vector<int> &arr, int d) {
    int iter = arr.size();
    v.resize(iter, -1);
    for (int i = 0; i < iter; i++) {
      dfs(arr, i, d, iter);
    }
    return *max_element(v.begin(), v.end());
  }

private:
  vector<int> v;
  void dfs(vector<int> &arr, int idx, int d, int n) {
    if (v[idx] != -1) {
      return;
    }
    v[idx] = 1;
    for (int i = idx - 1; i >= 0 && idx - i <= d && arr[idx] > arr[i]; i--) {
      dfs(arr, i, d, n);
      v[idx] = max(v[idx], v[i] + 1);
    }
    for (int i = idx + 1; i < n && i - idx <= d && arr[idx] > arr[i]; i++) {
      dfs(arr, i, d, n);
      v[idx] = max(v[idx], v[i] + 1);
    }
    return;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
