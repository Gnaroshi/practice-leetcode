"""
Problem: 3532. Path Existence Queries in a Graph I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.rank[root_i] += self.rank[root_j]
            return True
        return False


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        sorted_nodes = sorted([(v, i) for i, v in enumerate(nums)])
        uf = UnionFind(n)

        for i in range(n - 1):
            v1, i1 = sorted_nodes[i]
            v2, i2 = sorted_nodes[i + 1]

            if v2 - v1 <= maxDiff:
                uf.union(i1, i2)

        ans = []
        for u, v in queries:
            ans.append(uf.find(u) == uf.find(v))

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
