"""
Problem: 1569. Number of Ways to Reorder Array to Get Same BST
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MD = 10**9 + 7

        def dfs(nums):
            m = len(nums)
            if m < 3:
                return 1
            ln = [x for x in nums if x < nums[0]]
            rn = [x for x in nums if x > nums[0]]
            return dfs(ln) * dfs(rn) * comb(m - 1, len(ln)) % MD

        return (dfs(nums) - 1) % MD


if __name__ == "__main__":
    sol = Solution()
    print()
