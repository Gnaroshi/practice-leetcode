"""
Problem: 940. Distinct Subsequences II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MD = 10**9 + 7
        dp = [1]
        last = {}
        for i, x in enumerate(s):
            dp.append(dp[-1] * 2)
            if x in last:
                dp[-1] -= dp[last[x]]
            last[x] = i

        return (dp[-1] - 1) % MD


if __name__ == "__main__":
    sol = Solution()
    print()
