// problem: 1914. Cyclically Rotating a Grid

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
  vector<vector<int>> rotateGrid(vector<vector<int>> &grid, int k) {
    int n = grid.size(), m = grid.front().size();
    int iter = min(m, n) / 2;
    for (int i = 0; i < iter; i++) {
      vector<int> cur;
      int rmn = i, rmx = n - 1 - i;
      int cmn = i, cmx = m - 1 - i;
      for (int r = rmn; r < rmx; r++) {
        cur.push_back(grid[r][cmn]);
      }
      for (int c = cmn; c < cmx; c++) {
        cur.push_back(grid[rmx][c]);
      }
      for (int r = rmx; r > rmn; r--) {
        cur.push_back(grid[r][cmx]);
      }
      for (int c = cmx; c > cmn; c--) {
        cur.push_back(grid[rmn][c]);
      }
      int p = cur.size(), md = k % p;
      vector<int> cur_r(p);
      for (int j = 0; j < p; j++) {
        cur_r[j] = cur[(j - md + p) % p];
      }

      int idx = 0;
      for (int r = rmn; r < rmx; r++) {
        grid[r][cmn] = cur_r[idx++];
      }
      for (int c = cmn; c < cmx; c++) {
        grid[rmx][c] = cur_r[idx++];
      }
      for (int r = rmx; r > rmn; r--) {
        grid[r][cmx] = cur_r[idx++];
      }
      for (int c = cmx; c > cmn; c--) {
        grid[rmn][c] = cur_r[idx++];
      }
    }
    return grid;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
