"""
Problem: 3312. Sorted GCD Pair Queries
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for num in nums:
            cnt[num] += 1

        for i in range(1, mx + 1):
            for j in range(i * 2, mx + 1, i):
                cnt[i] += cnt[j]

        for i in range(1, mx + 1):
            cnt[i] = cnt[i] * (cnt[i] - 1) // 2
        for i in range(mx, 0, -1):
            for j in range(i * 2, mx + 1, i):
                cnt[i] -= cnt[j]

        for i in range(1, mx + 1):
            cnt[i] += cnt[i - 1]

        ans = []
        for q in queries:
            q += 1
            pos = bisect_left(cnt, q)
            ans.append(pos)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
