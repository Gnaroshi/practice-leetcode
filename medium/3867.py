"""
Problem: 3867. Sum of GCD of Formed Pairs
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        mx = 0
        # prefix_gcd = sorted([math.gcd(max(nums[: i + 1]), nums[i]) for i in range(n)])
        prefix_gcd = []
        for i in range(n):
            mx = max(mx, nums[i])
            prefix_gcd.append(math.gcd(mx, nums[i]))

        prefix_gcd.sort()

        hn = n // 2
        ans = 0

        for i in range(hn):
            ans += math.gcd(prefix_gcd[i], prefix_gcd[n - i - 1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
