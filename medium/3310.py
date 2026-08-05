"""
Problem: 3310. Remove Methods From Project
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        e = [[] for _ in range(n)]
        i_d = [0] * n

        for u, v in invocations:
            e[u].append(v)
            i_d[v] += 1

        dq = deque([k])
        sus = bytearray(n)
        sus[k] = 1

        while dq:
            u = dq.popleft()
            for v in e[u]:
                i_d[v] -= 1

                if sus[v] == 0:
                    dq.append(v)
                    sus[v] = 1

        is_rmall = True
        for i in range(n):
            if sus[i] == 1 and i_d[i] > 0:
                is_rmall = False
                break

        if not is_rmall:
            return list(range(n))

        return [i for i in range(n) if sus[i] == 0]


if __name__ == "__main__":
    sol = Solution()
    print()
