"""
Problem: 2267. Check if There Is a Valid Parentheses String Path
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n, m = len(grid), len(grid[0])
        sz = n + m - 1
        if sz % 2 == 1:
            return False
        if grid[0][0] != "(" or grid[n - 1][m - 1] != ")":
            return False

        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 2

        for i in range(n):
            for j in range(m):
                chk = 1 if grid[i][j] == "(" else -1
                if i > 0:
                    if chk == 1:
                        dp[i][j] |= dp[i - 1][j] << 1
                    else:
                        dp[i][j] |= dp[i - 1][j] >> 1
                if j > 0:
                    if chk == 1:
                        dp[i][j] |= dp[i][j - 1] << 1
                    else:
                        dp[i][j] |= dp[i][j - 1] >> 1

        return bool(dp[n - 1][m - 1] & 1)


if __name__ == "__main__":
    sol = Solution()
    print()
