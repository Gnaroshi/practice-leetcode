"""
Problem: 3513. Number of Unique XOR Triplets I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        ans = 1
        while ans <= n:
            ans <<= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
