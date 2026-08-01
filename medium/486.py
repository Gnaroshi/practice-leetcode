"""
Problem: 486. Predict the Winner
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from functools import lru_cache
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:

    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def fn(l: int, r: int) -> int:
            if l > r:
                return 0

            cur_l = nums[l] - fn(l + 1, r)
            cur_r = nums[r] - fn(l, r - 1)

            return max(cur_l, cur_r)

        return fn(0, len(nums) - 1) >= 0


if __name__ == "__main__":
    sol = Solution()
    print()
