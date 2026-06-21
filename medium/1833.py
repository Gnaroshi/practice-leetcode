"""
Problem: 1833. Maximum Ice Cream Bars
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for c in costs:
            if coins >= c:
                ans += 1
                coins -= c
            else:
                break

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
