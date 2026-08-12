"""
Problem: 2958. Length of Longest Subarray With at Most K Frequency
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Deque, Dict, List, Optional, Set, Tuple


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnts = Counter()
        mxl = 0
        l = 0

        for r in range(n):
            cnts[nums[r]] += 1
            while cnts[nums[r]] > k:
                cnts[nums[l]] -= 1
                l += 1

            mxl = max(mxl, r - l + 1)

        return mxl


if __name__ == "__main__":
    sol = Solution()
    print()
