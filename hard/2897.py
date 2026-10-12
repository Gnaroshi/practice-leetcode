"""
Problem: 2897. Apply Operations on Array to Maximize Sum of Squares
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MD = 10**9 + 7
        cnt = [0] * 30

        for n in nums:
            for i in range(30):
                if n & (1 << i):
                    cnt[i] += 1

        ret = 0
        for _ in range(k):
            cur = 0
            for j in range(29, -1, -1):
                if cnt[j] > 0:
                    cur |= 1 << j
                    cnt[j] -= 1
            ret = (ret + cur * cur) % MD

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
