"""
Problem: 1621. Number of Sets of K Non-Overlapping Line Segments
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MD = 10**9 + 7
        dp = [1] * n
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = (prefix_sums[i] + dp[i]) % MD
        for _ in range(k):
            dp[0] = 0
            for i in range(1, n):
                dp[i] = (dp[i - 1] + prefix_sums[i]) % MD
            for i in range(n):
                prefix_sums[i + 1] = (prefix_sums[i] + dp[i]) % MD

        return dp[n - 1]


if __name__ == "__main__":
    sol = Solution()
    print()
