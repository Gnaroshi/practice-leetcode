"""
Problem: 3345. Smallest Divisible Digit Product I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            cur = math.prod(map(int, str(n)))
            if cur % t == 0:
                return n
            n += 1


if __name__ == "__main__":
    sol = Solution()
    print()
