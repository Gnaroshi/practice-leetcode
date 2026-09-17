"""
Problem: 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        ans = n + 1
        s = 0
        pos = {0: -1}
        mn = n

        for i, x in enumerate(arr):
            s += x
            if s - target in pos:
                j = pos[s - target]
                sz = i - j
                ans = min(ans, sz + (n if j == -1 else arr[j]))
                mn = min(mn, sz)
            arr[i] = mn
            pos[s] = i

        return -1 if ans == n + 1 else ans


if __name__ == "__main__":
    sol = Solution()
    print()
