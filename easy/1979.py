"""
Problem: 1979. Find Greatest Common Divisor of Array
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return math.gcd(min(nums), max(nums))


if __name__ == "__main__":
    sol = Solution()
    print()
