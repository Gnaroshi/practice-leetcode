// problem: 1345. Jump Game IV

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
  int minJumps(vector<int> &arr) {

    int n = arr.size(), ans = 0;
    if (n <= 1) {
      return 0;
    }

    map<int, vector<int>> mp;
    for (int i = 0; i < n; i++) {
      mp[arr[i]].push_back(i);
    }
    unordered_set<int> cur, vist, rest;
    cur.insert(0);
    vist.insert(0);
    vist.insert(n - 1);
    rest.insert(n - 1);
    while (!cur.empty()) {
      if (cur.size() > rest.size()) {
        swap(cur, rest);
      }

      unordered_set<int> nxt;

      for (auto i : cur) {
        for (auto j : mp[arr[i]]) {
          if (rest.find(j) != rest.end()) {
            return ans + 1;
          }
          if (vist.find(j) == vist.end()) {
            vist.insert(j);
            nxt.insert(j);
          }
        }

        mp[arr[i]].clear();

        if (rest.find(i + 1) != rest.end() || rest.find(i - 1) != rest.end()) {
          return ans + 1;
        }

        if (i + 1 < n && vist.find(i + 1) == vist.end()) {
          vist.insert(i + 1);
          nxt.insert(i + 1);
        }
        if (i - 1 >= 0 && vist.find(i - 1) == vist.end()) {
          vist.insert(i - 1);
          nxt.insert(i - 1);
        }
      }
      cur = nxt;
      ans++;
    }
    return -1;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
