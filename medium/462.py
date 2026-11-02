"""
Problem: 462. Minimum Moves to Equal Array Elements II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mn = float("inf")
        sm, tot = 0, sum(nums)

        sz = len(nums)
        for i in range(sz):
            cur = (nums[i] * i - sm) + ((tot - sm) - nums[i] * (sz - i))
            mn = min(mn, cur)
            sm += nums[i]

        return int(mn)


if __name__ == "__main__":
    sol = Solution()
    print()
