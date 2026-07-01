"""
Problem: 2812. Find the Safest Path in a Grid
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        dist_t = self.setDist(grid)
        n = len(grid)
        l = 0
        r = 2 * n
        while l < r:
            m = l + (r - l) // 2
            if self.isValid(dist_t, m):
                l = m + 1
            else:
                r = m

        return l - 1

    def setDist(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ret = [[0] * n for _ in range(n)]
        vst = [[False] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append([i, j])
                    vst[i][j] = True

        dist = 0
        while q:
            qs = len(q)
            while qs > 0:
                cx, cy = q.popleft()
                ret[cx][cy] = dist
                for d in range(4):
                    nx = cx + self.dx[d]
                    ny = cy + self.dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if vst[nx][ny]:
                        continue
                    q.append([nx, ny])
                    vst[nx][ny] = True
                qs -= 1
            dist += 1

        return ret

    def isValid(self, dist_t: List[List[int]], flag: int) -> bool:
        if dist_t[0][0] < flag:
            return False

        n = len(dist_t)
        q = deque()
        vst = [[False] * n for _ in range(n)]
        q.append([0, 0])

        while q:
            cx, cy = q.popleft()
            if dist_t[cx][cy] < flag:
                continue
            if cx == n - 1 and cy == n - 1:
                return True
            for d in range(4):
                nx = cx + self.dx[d]
                ny = cy + self.dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if vst[nx][ny]:
                    continue
                q.append([nx, ny])
                vst[nx][ny] = True

        return False


if __name__ == "__main__":
    sol = Solution()
