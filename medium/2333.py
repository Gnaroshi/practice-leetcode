"""
Problem: 2333. Minimum Sum of Squared Difference
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minSumSquareDiff(
        self, nums1: list[int], nums2: list[int], k1: int, k2: int
    ) -> int:

        ret = 0
        diff = []
        n = len(nums1)
        for i in range(n):
            a = nums1[i]
            b = nums2[i]
            diff.append(abs(a - b))

        k = k1 + k2
        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i in range(1, n + 1):
            chk = (diff[i - 1] - diff[i]) * i
            if chk > k:
                q, r = divmod(k, i)
                t = diff[i - 1] - q
                return t**2 * (i - r) + (t - 1) ** 2 * r + sum(x * x for x in diff[i:n])
            k -= chk
        return 0


if __name__ == "__main__":
    sol = Solution()
    print()
