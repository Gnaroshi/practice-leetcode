"""
Problem: 628. Maximum Product of Three Numbers
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


if __name__ == "__main__":
    sol = Solution()
    print()
