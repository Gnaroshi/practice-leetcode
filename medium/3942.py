"""
Problem: 3942. Minimum Operations to Sort a Permutation
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        st = nums.index(0)

        l, r = True, True

        for i in range(1, n):
            cur = nums[(st + i) % n]
            if cur != i:
                l = False
            if cur != n - i:
                r = False
            if not l and not r:
                return -1

        return min(st, n - st + 2) if l else min(n - st, st + 2)


if __name__ == "__main__":
    sol = Solution()
    print()
