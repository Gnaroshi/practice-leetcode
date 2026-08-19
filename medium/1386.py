"""
Problem: 1386. Cinema Seat Allocation
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rd = defaultdict(set)
        for x, y in reservedSeats:
            rd[x].add(y)

        ret = (n - len(rd)) * 2

        for row, seats in rd.items():
            l = not any(seat in seats for seat in [2, 3, 4, 5])
            m = not any(seat in seats for seat in [4, 5, 6, 7])
            r = not any(seat in seats for seat in [6, 7, 8, 9])

            if l and r:
                ret += 2
            elif l or m or r:
                ret += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
