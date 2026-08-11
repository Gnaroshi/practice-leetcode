"""
Problem: 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
"""

import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        cur = nums[0]

        for x, y in itertools.pairwise(nums):
            if x + 1 == y:
                cur += y
            else:
                break

        ns = set(nums)

        while cur in ns:
            cur += 1

        return cur


if __name__ == "__main__":
    sol = Solution()
    print()
