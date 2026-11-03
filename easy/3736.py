"""
Problem: 3736. Minimum Moves to Equal Array Elements III
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ret = 0
        mx = max(nums)
        for i in nums:
            ret += mx - i

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
