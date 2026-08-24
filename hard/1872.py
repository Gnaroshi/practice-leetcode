"""
Problem: 1872. Stone Game VIII
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        arr = list(accumulate(stones))
        f = [0] * n
        f[n - 1] = arr[n - 1]
        for i in range(n - 2, 0, -1):
            f[i] = max(f[i + 1], arr[i] - f[i + 1])

        return f[1]


if __name__ == "__main__":
    sol = Solution()
    print()
