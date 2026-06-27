"""
Problem: 3020. Find the Maximum Number of Elements in Subset
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        cnt1 = cnt.get(1, 0)
        if cnt1 % 2 == 1:
            ans = cnt1
        else:
            ans = cnt1 - 1

        cnt.pop(1, None)

        for i in cnt:
            l = 0
            m = i
            while m in cnt and cnt[m] > 1:
                l += 2
                m *= m

            if m in cnt:
                l += 1
            else:
                l -= 1

            ans = max(ans, l)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
