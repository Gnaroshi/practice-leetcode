"""
Problem: 3622. Check Divisibility by Digit Sum and Product
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ns = sum(int(t) for t in str(n))
        np = 1
        for t in str(n):
            np *= int(t)

        return n % (ns + np) == 0


if __name__ == "__main__":
    sol = Solution()
    print()
