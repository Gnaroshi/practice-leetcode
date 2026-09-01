"""
Problem: 3568. Minimum Moves to Clean the Classroom
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m, n = len(classroom), len(classroom[0])
        id = [[0] * n for _ in range(m)]
        cx = cy = 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    cx, cy = i, j
                elif classroom[i][j] == "L":
                    id[i][j] = 1 << cnt
                    cnt += 1

        full = 1 << cnt
        best = [[[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)]
        best[cx][cy][0] = energy
        dq = deque()
        dq.append((cx, cy, 0, energy, 0))

        while dq:
            x, y, mask, e, steps = dq.popleft()
            if mask == full - 1:
                return steps
            if e == 0:
                continue
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if nx < 0 or nx >= m or ny < 0 or ny >= n or classroom[nx][ny] == "X":
                    continue
                nxt_e = energy if classroom[nx][ny] == "R" else e - 1
                nxt_mask = mask | id[nx][ny]
                if nxt_e > best[nx][ny][nxt_mask]:
                    best[nx][ny][nxt_mask] = nxt_e
                    dq.append((nx, ny, nxt_mask, nxt_e, steps + 1))

        return -1


if __name__ == "__main__":
    sol = Solution()
    print()
