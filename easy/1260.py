"""
Problem: 1260. Shift 2D Grid
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        for _ in range(k):
            ret = [[0] * m for _ in range(n)]

            for r in range(n):
                for c in range(m - 1):
                    ret[r][c + 1] = grid[r][c]
            for r in range(n - 1):
                ret[r + 1][0] = grid[r][m - 1]

            ret[0][0] = grid[n - 1][m - 1]

            grid = ret

        return grid


if __name__ == "__main__":
    sol = Solution()
    print()
