"""
Problem: 3970. Shortest Path With At Most K Consecutive Identical Characters
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        g = [[] for _ in range(n)]
        for (
            i,
            j,
            v,
        ) in edges:
            g[i].append((j, v))

        MX = 2**31 - 1
        dist = [[MX] * (k + 1) for _ in range(n)]
        pq = []

        dist[0][1] = 0
        heapq.heappush(pq, (0, 0, 1))

        while pq:
            cur, i, cnt = heapq.heappop(pq)
            if cur > dist[i][cnt]:
                continue
            if i == n - 1:
                return cur
            for j, v in g[i]:
                tmp = cnt + 1 if labels[i] == labels[j] else 1
                if tmp > k:
                    continue
                nxt = cur + v
                if nxt < dist[j][tmp]:
                    dist[j][tmp] = nxt
                    heapq.heappush(pq, (nxt, j, tmp))
        return -1


if __name__ == "__main__":
    sol = Solution()
    print()
