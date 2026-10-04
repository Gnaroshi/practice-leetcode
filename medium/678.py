"""
Problem: 678. Valid Parenthesis String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def checkValidString(self, s: str) -> bool:
        lc, rc = 0, 0
        n = len(s) - 1

        for i in range(n + 1):
            if s[i] == "(" or s[i] == "*":
                lc += 1
            else:
                lc -= 1

            if s[n - i] == ")" or s[n - i] == "*":
                rc += 1
            else:
                rc -= 1

            if lc < 0 or rc < 0:
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    print()
