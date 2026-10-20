"""
Problem: 3886. Sum of Sortable Integers
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        K = []
        n = len(nums)
        sz = int(math.sqrt(n))

        for i in range(1, sz + 1):
            if n % i == 0:
                K.append(i)
                if i**2 != n:
                    K.append(n // i)
        # print(f"n: {n}, sz: {sz}, K: {K}")

        tgt = sorted(nums)

        def chk(a: list[int], b: list[int]) -> bool:
            al = len(a) - 1
            for i in range(al):
                if a[i] > a[i + 1]:
                    return a[i + 1 :] + a[: i + 1] == b

            return a == b

        ret = 0
        for k in K:
            for i in range(0, n, k):
                j = i + k - 1
                if not chk(nums[i : j + 1], tgt[i : j + 1]):
                    break
            else:
                ret += k

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.sortableIntegers([1, 2, 3, 4, 5, 6, 7, 8]))
