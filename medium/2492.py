"""
Problem: 2492. Minimum Score of a Path Between Two Cities
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def bfs(self, n: int, adj: List[List[int]]) -> int:
        vist = [False] * (n + 1)
        q = deque()
        ret = float("inf")
        q.append(1)
        vist[1] = True

        while q:
            cur = q.popleft()

            for e in adj[cur]:
                ret = min(ret, e[1])
                if not vist[e[0]]:
                    vist[e[0]] = True
                    q.append(e[0])

        return ret

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n + 1)]
        for r in roads:
            adj[r[0]].append((r[1], r[2]))
            adj[r[1]].append((r[0], r[2]))

        return self.bfs(n, adj)


if __name__ == "__main__":
    sol = Solution()
    print()
