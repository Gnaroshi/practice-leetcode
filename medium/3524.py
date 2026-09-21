"""
Problem: 3524. Find X Value of Array I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            val = num % k

            new_dp[val] += 1
            
            for prev_rem in range(k):
                if dp[prev_rem] > 0:
                    new_rem = (prev_rem * val) % k
                    new_dp[new_rem] += dp[prev_rem]

            for i in range(k):
                ans[i] += new_dp[i]

            dp = new_dp

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()ㅓ
