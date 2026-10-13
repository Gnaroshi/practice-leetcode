"""
Problem: 3727. Maximum Alternating Sum of Squares
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [abs(t) for t in nums]
        nums.sort(reverse=False)
        a = nums[n // 2 :]
        b = nums[: n // 2]
        print(f"a: {a} \n b: {b}")

        return sum(x**2 for x in a) - sum(x**2 for x in b)


if __name__ == "__main__":
    sol = Solution()
    print()
