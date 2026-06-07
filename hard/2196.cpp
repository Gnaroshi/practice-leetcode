// problem: 2196. Create Binary Tree From Descriptions

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
  TreeNode *createBinaryTree(vector<vector<int>> &descriptions) {
    unordered_map<int, TreeNode *> mp;
    unordered_set<int> children;

    for (auto &d : descriptions) {
      int p = d[0], c = d[1], isL = d[2];

      if (mp.find(p) == mp.end()) {
        mp[p] = new TreeNode(p);
      }

      if (mp.find(c) == mp.end()) {
        mp[c] = new TreeNode(c);
      }

      if (isL) {
        mp[p]->left = mp[c];
      } else {
        mp[p]->right = mp[c];
      }

      children.insert(c);
    }

    for (auto &d : descriptions) {
      if (children.find(d[0]) == children.end()) {
        return mp[d[0]];
      }
    }

    return nullptr;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
