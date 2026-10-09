"""
Problem: 1541. Minimum Insertions to Balance a Parentheses String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        cnt, lc, idx = 0, 0, 0

        while idx < n:
            if s[idx] == "(":
                lc += 1
                idx += 1
            else:
                if lc > 0:
                    lc -= 1
                else:
                    cnt += 1
                if idx < n - 1 and s[idx + 1] == ")":
                    idx += 2
                else:
                    cnt += 1
                    idx += 1

        cnt += lc * 2
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print()
