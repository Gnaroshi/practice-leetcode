"""
Problem: 3619. Count Islands With Total Value Divisible by K
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        n = len(grid)
        m = len(grid[0])

        def dfs(i: int, j: int) -> int:
            cur = grid[i][j]
            grid[i][j] = 0
            for d in range(4):
                x = i + dx[d]
                y = j + dy[d]
                if 0 <= x < n and 0 <= y < m and grid[x][y] > 0:
                    cur += dfs(x, y)
            return cur

        return sum(
            grid[i][j] > 0 and dfs(i, j) % k == 0 for i in range(n) for j in range(m)
        )


if __name__ == "__main__":
    sol = Solution()
    print()
