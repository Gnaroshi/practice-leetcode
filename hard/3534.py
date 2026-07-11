"""
Problem: 3534. Path Existence Queries in a Graph II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        sorted_nodes = sorted([(v, i) for i, v in enumerate(nums)])
        vals = [v for v, _ in sorted_nodes]

        recon = {orig: idx for idx, (v, orig) in enumerate(sorted_nodes)}
        LOG = 20
        up = [[0] * n for _ in range(LOG)]

        r_ptr = 0
        for i in range(n):
            while r_ptr < n and vals[r_ptr] - vals[i] <= maxDiff:
                r_ptr += 1
            up[0][i] = r_ptr - 1

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
            a, b = recon[u], recon[v]
            if a > b:
                a, b = b, a

            jmps = 0
            cur = a

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < b:
                    cur = up[k][cur]
                    jmps += 1 << k

            if up[0][cur] < b:
                ans.append(-1)
            else:
                ans.append(jmps + 1)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
