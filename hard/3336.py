"""
Problem: 3336. Find the Number of Subsequence With Equal GCD
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MD = 10**9 + 7
        m = max(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        dp[0][0] = 1

        for i in nums:
            ndp = [[0] * (m + 1) for _ in range(m + 1)]

            for j in range(m + 1):
                dv = math.gcd(j, i)
                for k in range(m + 1):
                    cur = dp[j][k]
                    if cur == 0:
                        continue

                    dv2 = math.gcd(k, i)
                    ndp[j][k] = (ndp[j][k] + cur) % MD
                    ndp[dv][k] = (ndp[dv][k] + cur) % MD
                    ndp[j][dv2] = (ndp[j][dv2] + cur) % MD

            dp = ndp

        ans = 0
        for i in range(1, m + 1):
            ans = (ans + dp[i][i]) % MD

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
