"""
Problem: 3471. Find the Largest Almost Missing Integer
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        SZ = 51
        if n == k:
            return max(nums)
        cnt = [0] * SZ
        for x in nums:
            cnt[x] += 1
        if k == 1:
            for i in range(SZ - 1, -1, -1):
                if cnt[i] == 1:
                    return i
            return -1
        ans = -1
        if cnt[nums[0]] == 1:
            ans = max(ans, nums[0])
        if cnt[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
