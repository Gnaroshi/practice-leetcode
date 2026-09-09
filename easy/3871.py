"""
Problem: 3871. Count Commas in Range II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def countCommas(self, n: int) -> int:
        p = 1000
        res = 0
        while p <= n:
            res += n - p + 1
            p *= 1000
        return res


if __name__ == "__main__":
    sol = Solution()
    print()
