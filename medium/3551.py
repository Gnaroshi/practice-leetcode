"""
Problem: 3551. Minimum Swaps to Sort by Digit Sum
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        ds = [0] * n
        for i, x in enumerate(nums):
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            ds[i] = s

        idx = list(range(n))
        idx.sort(key=lambda i: (ds[i], nums[i]))

        tgt = [0] * n
        for i, x in enumerate(idx):
            tgt[x] = i

        t = list(range(n))
        cur = n

        def find(x):
            if t[x] != x:
                t[x] = find(t[x])
            return t[x]

        for i in range(n):
            r, l = find(i), find(tgt[i])
            if r != l:
                t[r] = l
                cur -= 1

        return n - cur


if __name__ == "__main__":
    sol = Solution()
    print()
