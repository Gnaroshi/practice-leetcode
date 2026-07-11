"""
Problem: 2685. Count the Number of Complete Components
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
        self.parent[i] = self.find(self.parent[i])  # Path compression
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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v in edges:
            uf.union(u, v)

        e_cnt = [0] * n
        for u, v in edges:
            r = uf.find(u)
            e_cnt[r] += 1

        ans = 0
        for i in range(n):
            if uf.parent[i] == i:
                v = uf.rank[i]
                e = e_cnt[i]

                if e == v * (v - 1) // 2:
                    ans += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
