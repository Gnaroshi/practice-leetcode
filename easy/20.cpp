// problem: Valid Parentheses

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
  bool isValid(string s) {
    stack<char> stk;
    for (auto &i : s) {
      if (i == ')') {
        if (stk.empty() || stk.top() != '(') {
          return false;
        }
        stk.pop();
      } else if (i == '}') {
        if (stk.empty() || stk.top() != '{') {
          return false;
        }
        stk.pop();

      } else if (i == ']') {
        if (stk.empty() || stk.top() != '[') {
          return false;
        }
        stk.pop();

      } else {
        stk.push(i);
      }
    }
    return stk.empty();
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
