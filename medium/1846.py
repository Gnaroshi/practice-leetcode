"""
Problem: 1846. Maximum Element After Decreasing and Rearranging
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        counts = [0] * (n + 1)

        for i in arr:
            counts[min(i, n)] += 1

        ret = 1
        for i in range(2, n + 1):
            ret = min(ret + counts[i], i)

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumElementAfterDecrementingAndRearranging([]))
