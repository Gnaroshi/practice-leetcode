"""
Problem: 3558. Number of Ways to Assign Edge Weights I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MD = 10**9 + 7
        n = len(edges)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        dist = [-1] * (n + 2)
        queue = deque([1])
        dist[1] = 0
        while queue:
            cur = queue.popleft()
            for nxt in adj[cur]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[cur] + 1
                    queue.append(nxt)
        max_depth = max(dist)

        return pow(2, max_depth - 1, MD)


if __name__ == "__main__":
    sol = Solution()
    print()
