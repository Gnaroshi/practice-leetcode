"""
Problem: 3644. Maximum K to Sort a Permutation
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ret = -1
        for i in range(n):
            if nums[i] == i:
                continue
            ret &= nums[i]
        return 0 if ret == -1 else ret


if __name__ == "__main__":
    sol = Solution()
    print()
