"""
Problem: 2472. Maximum Number of Non-overlapping Palindrome Substrings
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        chk = [[False] * n for _ in range(n)]

        for sz in range(1, n + 1):
            for l in range(n - sz + 1):
                r = l + sz - 1
                chk[l][r] = s[l] == s[r] and (sz <= 2 or chk[l + 1][r - 1])

        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i - k + 1):
                if chk[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    print()
