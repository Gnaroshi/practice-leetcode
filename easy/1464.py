"""
Problem: 1464. Maximum Product of Two Elements in an Array
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)


if __name__ == "__main__":
    sol = Solution()
    print()
