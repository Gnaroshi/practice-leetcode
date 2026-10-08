"""
Problem: 1021. Remove Outermost Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ret = ""
        cur = ""
        lc, rc = 0, 0
        for c in s:
            if c == "(":
                lc += 1
            else:
                rc += 1
            cur += c
            if lc == rc:
                if lc > 1:
                    ret += cur[1:-1]

                cur = ""
                lc, rc = 0, 0

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
