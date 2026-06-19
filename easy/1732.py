"""
Problem: 1732. Find the Highest Altitude
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        cur = 0
        for i in gain:
            cur += i
            mx = max(cur, mx)

        return mx

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.1732. Find the Highest Altitude())
