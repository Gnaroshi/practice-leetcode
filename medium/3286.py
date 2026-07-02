"""
Problem: 3286. Find a Safe Walk Through a Grid
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        q.append((0, 0))
        vist = [[float("inf")] * m for _ in range(n)]
        vist[0][0] = grid[0][0]
        while q:
            cx, cy = q.popleft()
            if cx == n - 1 and cy == m - 1:
                return True
            for dx, dy in self.directions:
                nx, ny = cx + dx, cy + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                nh = vist[cx][cy] + grid[nx][ny]
                if nh >= health:
                    continue

                if nh < vist[nx][ny]:
                    vist[nx][ny] = nh
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny))
                    else:
                        q.append((nx, ny))

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
