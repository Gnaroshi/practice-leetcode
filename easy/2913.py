"""
Problem: 2913. Subarrays Distinct Element Sum of Squares I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        for w in range(1, n + 1):
            for i in range(n - w + 1):
                cur = set(nums[i : i + w])
                ret += len(cur) ** 2

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
