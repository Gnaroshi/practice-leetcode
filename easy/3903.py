"""
Problem: 3903. Smallest Stable Index I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            cur = max(nums[: i + 1]) - min(nums[i:])
            if cur <= k:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    print()
