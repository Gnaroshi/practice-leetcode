"""
Problem: 921. Minimum Add to Make Parentheses Valid
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ret = 0
        dq = deque()
        for c in s:
            if c == "(":
                dq.append("(")
            else:
                if dq:
                    dq.pop()
                else:
                    ret += 1

        return len(dq) + ret


if __name__ == "__main__":
    sol = Solution()
    print()
