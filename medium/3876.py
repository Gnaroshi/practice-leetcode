"""
Problem: 3876. Construct Uniform Parity Array II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = nums1[0]
        chk = False

        for i in nums1:
            mn = min(mn, i)
            if i & 1:
                chk = True
        if mn & 1:
            return True
        return not chk


if __name__ == "__main__":
    sol = Solution()
    print()
