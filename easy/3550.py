"""
Problem: 3550. Smallest Index With Digit Sum Equal to Index
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def fn(x: int) -> int:
            sx = str(x)
            return sum([int(t) for t in sx])

        for i, n in enumerate(nums):
            if fn(n) == i + 1:
                return i + 1

        return -1


if __name__ == "__main__":
    sol = Solution()
    print()
