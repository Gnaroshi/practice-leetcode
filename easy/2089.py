"""
Problem: 2089. Find Target Indices After Sorting Array
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ret = []
        nums.sort()
        for i, x in enumerate(nums):
            if x == target:
                ret.append(i)

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
