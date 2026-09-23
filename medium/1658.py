"""
Problem: 1658. Minimum Operations to Reduce X to Zero
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        tot = sum(nums)
        n = len(nums)
        mx = -1
        l = cur = 0

        for r in range(n):
            cur += nums[r]
            while cur > tot - x and l <= r:
                cur -= nums[l]
                l += 1
            if cur == tot - x:
                mx = max(mx, r - l + 1)

        return n - mx if mx != -1 else -1


if __name__ == "__main__":
    sol = Solution()
    print()
