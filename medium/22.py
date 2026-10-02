"""
Problem: 22. Generate Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def checker(s):
            lc = 0
            for c in s:
                if c == "(":
                    lc += 1
                else:
                    lc -= 1
                if lc < 0:
                    return False
            return lc == 0

        ans = []
        dq = deque([""])
        while dq:
            cur = dq.popleft()

            if len(cur) == 2 * n:
                if checker(cur):
                    ans.append(cur)
                continue
            dq.append(cur + ")")
            dq.append(cur + "(")
        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
