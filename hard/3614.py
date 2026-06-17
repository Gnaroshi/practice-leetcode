"""
Problem: 3614. Process String with Special Operations II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        if not n:
            return "."

        L = [0] * n
        cur = 0

        for i in range(n):
            c = s[i]
            if c == "*":
                cur = max(0, cur - 1)
            elif c == "#":
                cur *= 2
            elif c == "%":
                pass
            else:
                cur += 1
            L[i] = cur

        if k >= L[-1]:
            return "."

        for i in range(n - 1, -1, -1):
            bef = L[i - 1] if i > 0 else 0
            c = s[i]

            if c == "*":
                pass
            elif c == "#":
                if k >= bef:
                    k -= bef
            elif c == "%":
                k = bef - 1 - k
            else:
                if k == bef:
                    return c

        return "."


if __name__ == "__main__":
    sol = Solution()
    print(sol)
