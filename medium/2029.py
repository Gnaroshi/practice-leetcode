"""
Problem: 2029. Stone Game IX
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a = b = c = 0
        for x in stones:
            if (typ := x % 3) == 0:
                a += 1
            elif typ == 1:
                b += 1
            else:
                c += 1
        if a % 2 == 0:
            return b >= 1 and c >= 1
        return b - c > 2 or c - b > 2


if __name__ == "__main__":
    sol = Solution()
    print()
