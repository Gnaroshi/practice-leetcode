"""
Problem: 3863. Minimum Operations to Sort a String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0
        elif len(s) == 2:
            return -1 if s[0] > s[1] else 0
        ret = 0
        nums = [(ord(x) - ord("a")) for x in s]
        n = len(nums)
        mx = max(nums)
        mn = min(nums)
        if nums[0] == mn:
            if nums[-1] == mx:
                if all(nums[i] <= nums[i + 1] for i in range(n - 1)):
                    ret = 0
                else:
                    ret = 1
            else:
                ret = 1
        elif nums[-1] == mx:
            if nums[0] == mn:
                if all(nums[i] <= nums[i + 1] for i in range(n - 1)):
                    ret = 0
                else:
                    ret = 1
            else:
                ret = 1
        elif nums[0] == mx and nums[-1] == mn:
            ret = 3
            if nums.count(mn) != 1 or nums.count(mx) != 1:
                ret = 2
        else:
            ret = 2
        print(nums)

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.minOperations("jgg"))
