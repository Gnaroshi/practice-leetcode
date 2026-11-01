"""
Problem: 453. Minimum Moves to Equal Array Elements
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums) - 1, -1, 0):
            ret += nums[i] - nums[0]
        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
