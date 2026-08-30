"""
Problem: 2091. Removing Minimum and Maximum From Array
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn_idx = nums.index(min(nums))
        mx_idx = nums.index(max(nums))
        l = min(mn_idx, mx_idx)
        r = max(mn_idx, mx_idx)
        n = len(nums)
        return min(r + 1, n - l, l + 1 + n - r)


if __name__ == "__main__":
    sol = Solution()
    print()
