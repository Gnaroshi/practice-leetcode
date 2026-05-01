// problem: 94. Binary Tree Inorder Traversal

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
  vector<int> inorderTraversal(TreeNode *root) {
    stack<TreeNode *> stk;
    vector<int> ret;
    TreeNode *cur = root;
    while (cur != nullptr || !stk.empty()) {
      if (cur != nullptr) {
        stk.push(cur);
        cur = cur->left;
      } else {
        ret.push_back(stk.top()->val);
        cur = stk.top()->right;
        stk.pop();
      }
    }
    return ret;
  }
};

class Solution_opt {
public:
  vector<int> inorderTraversal(TreeNode *root) {
    vector<int> ret;
    TreeNode *cur = root;
    // Morris Traversal: Achieves O(1) auxiliary space via temporary threading
    while (cur != nullptr) {
      if (cur->left == nullptr) {
        ret.push_back(cur->val); // Visit node with no left subtree
        cur = cur->right;
      } else {
        // Find inorder predecessor (rightmost node in left subtree)
        TreeNode *pre = cur->left;
        while (pre->right != nullptr && pre->right != cur) {
          pre = pre->right;
        }
        if (pre->right == nullptr) {
          pre->right = cur; // Create temporary thread
          cur = cur->left;
        } else {
          pre->right = nullptr;    // Revert thread (restore tree structure)
          ret.push_back(cur->val); // Visit current node
          cur = cur->right;
        }
      }
    }
    return ret;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
