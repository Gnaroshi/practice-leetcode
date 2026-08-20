"""
Problem: 3069. Distribute Elements Into Two Arrays I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2 = [nums[0]], [nums[1]]
        n = len(nums)
        for i in range(2, n):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2


if __name__ == "__main__":
    sol = Solution()
    print()
