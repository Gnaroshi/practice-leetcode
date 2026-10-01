"""
Problem: 20. Valid Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        for c in s:
            if c == ")":
                if len(dq) == 0 or dq[-1] != "(":
                    return False
                dq.pop()
            elif c == "}":
                if len(dq) == 0 or dq[-1] != "{":
                    return False
                dq.pop()
            elif c == "]":
                if len(dq) == 0 or dq[-1] != "[":
                    return False
                dq.pop()
            else:
                dq.append(c)

        return False if dq else True


if __name__ == "__main__":
    sol = Solution()
    print()
