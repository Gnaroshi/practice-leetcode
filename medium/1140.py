"""
Problem: 1140. Stone Game II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dfs(i, m):
            if i == n:
                return 0
            if i + 2 * m >= n:
                return suffix_sum[i]
            if (i, m) in memo:
                return memo[(i, m)]

            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix_sum[i] - dfs(i + x, max(m, x)))

            memo[(i, m)] = res
            return res

        return dfs(0, 1)


if __name__ == "__main__":
    sol = Solution()
    print()
