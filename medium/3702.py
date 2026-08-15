"""
Problem: 3702. Longest Subsequence With Non-Zero Bitwise XOR
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        tot = 0
        is_zero = True

        for x in nums:
            tot ^= x
            if x > 0:
                is_zero = False

        if tot > 0:
            return n
        return n - 1 if is_zero == False else 0


if __name__ == "__main__":
    sol = Solution()
    print()
