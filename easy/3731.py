"""
Problem: 3731. Find Missing Elements
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn, mx = min(nums), max(nums)
        ret = []
        for i in range(mn, mx + 1):
            if i not in nums:
                ret.append(i)

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
