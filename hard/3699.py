"""
Problem: 3699. Number of ZigZag Arrays I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MD = 10**9 + 7
        w = r - l + 1

        dp = [1] * w

        for _ in range(2, n + 1):
            nxt_dp = [0] * w
            cur = 0

            for j in range(1, w):
                cur = (cur + dp[w - j]) % MD
                nxt_dp[j] = cur

            dp = nxt_dp

        return (sum(dp) * 2) % MD


if __name__ == "__main__":
    sol = Solution()
    print()
