"""
Problem: 3514. Number of Unique XOR Triplets II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        t = set()
        ret = set()
        for i in nums:
            for j in nums:
                t.add(i ^ j)
        for i in nums:
            for j in t:
                ret.add(i ^ j)

        return len(ret)


if __name__ == "__main__":
    sol = Solution()
    print()
