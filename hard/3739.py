"""
Problem: 3739. Counting Subarrays With Majority Element II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        prefixes_sums = [0] * (n * 2 + 1)
        prefixes_sums[n] = 1
        cnt = n
        ans = 0
        cur = 0

        for i in range(n):
            if nums[i] == target:
                cur += prefixes_sums[cnt]
                cnt += 1
                prefixes_sums[cnt] += 1
            else:
                cnt -= 1
                cur -= prefixes_sums[cnt]
                prefixes_sums[cnt] += 1
            ans += cur

        return ans
    
        

if __name__ == '__main__':
    sol = Solution()
    print(sol.3739. Counting Subarrays With Majority Element II())
