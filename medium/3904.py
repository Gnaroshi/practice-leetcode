"""
Problem: 3904. Smallest Stable Index II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mn = [math.inf] * (n - 1) + [nums[-1]]
        for i in range(n - 2, -1, -1):
            mn[i] = min(mn[i + 1], nums[i])

        mx = 0
        for i in range(n):
            mx = max(mx, nums[i])
            if mx - mn[i] <= k:
                return i
        return -1


if __name__ == "__main__":
    sol = Solution()
    print()
