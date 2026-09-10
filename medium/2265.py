"""
Problem: 2265. Count Nodes Equal to Average of Subtree
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ret = 0

        def dfs(node):
            if not node:
                return 0, 0
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            tot = ls + rs + node.val
            tot_cnt = lc + rc + 1
            if tot // tot_cnt == node.val:
                self.ret += 1
            return tot, tot_cnt

        dfs(root)
        return self.ret


if __name__ == "__main__":
    sol = Solution()
    print()
