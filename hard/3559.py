"""
Problem: 3559. Number of Ways to Assign Edge Weights II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def assignEdgeWeights(
        self, edges: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        MD = 10**9 + 7
        n = len(edges) + 1
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * (n + 2)
        parent = [[-1] * (n + 1) for _ in range(20)]
        queue = deque([(1, -1, 0)])
        while queue:
            cur, p, d = queue.popleft()
            depth[cur] = d
            parent[0][cur] = p
            for v in adj[cur]:
                if v != p:
                    queue.append((v, cur, d + 1))

        for i in range(1, 20):
            for v in range(1, n + 1):
                if parent[i - 1][v] != -1:
                    parent[i][v] = parent[i - 1][parent[i - 1][v]]

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for i in range(20):
                if (diff >> i) & 1:
                    u = parent[i][u]

            if u == v:
                return u

            for i in range(20 - 1, -1, -1):
                if parent[i][u] != parent[i][v]:
                    u = parent[i][u]
                    v = parent[i][v]

            return parent[0][u]

        ans = []
        for a, b in queries:
            if a == b:
                ans.append(0)
            else:
                lca_node = get_lca(a, b)
                dist = depth[a] + depth[b] - 2 * depth[lca_node]
                ans.append(pow(2, dist - 1, MD))

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
