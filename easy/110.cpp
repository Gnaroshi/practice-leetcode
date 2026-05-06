// problem: 110. Balanced Binary Tree

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

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  bool isBalanced(TreeNode *root) { return chk(root).first; }

private:
  pair<bool, int> chk(TreeNode *cur) {
    if (cur == nullptr) {
      return {true, 0};
    }

    bool lb, rb;
    int lh, rh;

    tie(lb, lh) = chk(cur->left);
    if (!lb) {
      return {false, 0};
    }
    tie(rb, rh) = chk(cur->right);
    if (!rb) {
      return {false, 0};
    }

    if (abs(lh - rh) > 1) {
      return {false, 0};
    }
    return {true, max(lh, rh) + 1};
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
