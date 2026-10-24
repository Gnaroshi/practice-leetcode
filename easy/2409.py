"""
Problem: 2409. Count Days Spent Together
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def fn(self, d: str, prefixSum: List[int]) -> int:
        m = int(d[:2])
        cur = int(d[3:])
        return prefixSum[m - 1] + cur

    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        dm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        pfs = [0]
        for d in dm:
            pfs.append(pfs[-1] + d)

        aad = self.fn(arriveAlice, pfs)
        lad = self.fn(leaveAlice, pfs)
        abd = self.fn(arriveBob, pfs)
        lbd = self.fn(leaveBob, pfs)

        return max(0, min(lad, lbd) - max(aad, abd) + 1)


if __name__ == "__main__":
    sol = Solution()
    print()
