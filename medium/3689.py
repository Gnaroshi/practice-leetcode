"""
Problem: 3689. Maximum Total Subarray Value I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTotalValue())
