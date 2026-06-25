"""
Problem: 3737. Count Subarrays With Majority Element I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def countMajoritySubarrays(self, nums: List[int], tgt: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == tgt:
                    cnt += 1
                else:
                    cnt -= 1
                if cnt > 0:
                    ans += 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
