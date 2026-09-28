"""
Problem: 1614. Maximum Nesting Depth of the Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxDepth(self, s: str) -> int:
        cur = 0
        mx = 0
        for c in s:
            if c == "(":
                cur += 1
                mx = max(mx, cur)
            elif c == ")":
                cur -= 1
        return mx


if __name__ == "__main__":
    sol = Solution()
    print()
