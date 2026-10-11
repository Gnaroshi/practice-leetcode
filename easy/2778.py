"""
Problem: 2778. Sum of Squares of Special Elements
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ret = 0
        n = len(nums)
        for i, x in enumerate(nums):
            if n % (i + 1) == 0:
                ret += x**2

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
