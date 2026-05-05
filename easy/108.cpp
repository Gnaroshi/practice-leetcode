// problem: 108. Convert Sorted Array to Binary Search Tree

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
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    TreeNode *ret;
    ret = buildBST(0, nums.size() - 1, nums);
    return ret;
  }

private:
  TreeNode *buildBST(int l, int r, vector<int> &nums) {
    if (l > r) {
      return nullptr;
    }
    int mid = l + (r - l) / 2;
    TreeNode *cur = new TreeNode(nums[mid]);
    cur->left = buildBST(l, mid - 1, nums);
    cur->right = buildBST(mid + 1, r, nums);
    return cur;
  }
};

int main(void) {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  return 0;
}
