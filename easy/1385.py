"""
Problem: 1385. Find the Distance Value Between Two Arrays
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ret = 0
        for x in arr1:
            flag = True
            for y in arr2:
                if abs(x - y) <= d:
                    flag = False
                    break
            if flag:
                ret += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
