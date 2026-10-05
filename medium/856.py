"""
Problem: 856. Score of Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dq = deque()
        dq.append(0)
        for c in s:
            if c == "(":
                dq.append(0)
            else:
                cur = dq.pop()
                dq[-1] += max(1, 2 * cur)

        return dq.pop()


if __name__ == "__main__":
    sol = Solution()
    print()
