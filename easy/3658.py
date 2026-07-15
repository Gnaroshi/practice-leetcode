"""
Problem: 3658. GCD of Odd and Even Sums
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        os = n**2
        es = n * (n + 1)

        return math.gcd(os, es)


if __name__ == "__main__":
    sol = Solution()
    print()
