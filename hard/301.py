"""
Problem: 301. Remove Invalid Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:

    def __init__(self):
        self.ans = None
        self.mn_rm = None

    def reset(self):
        self.ans = set()
        self.mn_rm = float("inf")

    def remains(self, s, idx, lc, rc, expr, rem_cnt):
        if idx == len(s):
            if lc == rc:
                if rem_cnt <= self.mn_rm:
                    tmp = "".join(expr)

                    if rem_cnt < self.mn_rm:
                        self.ans = set()
                        self.mn_rm = rem_cnt

                    self.ans.add(tmp)
        else:
            cur = s[idx]

            if cur != "(" and cur != ")":
                expr.append(cur)
                self.remains(s, idx + 1, lc, rc, expr, rem_cnt)
                expr.pop()
            else:
                self.remains(s, idx + 1, lc, rc, expr, rem_cnt + 1)
                expr.append(cur)

                if s[idx] == "(":
                    self.remains(s, idx + 1, lc + 1, rc, expr, rem_cnt)
                elif rc < lc:
                    self.remains(s, idx + 1, lc, rc + 1, expr, rem_cnt)

                expr.pop()

    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.reset()
        self.remains(s, 0, 0, 0, [], 0)
        return list(self.ans)


if __name__ == "__main__":
    sol = Solution()
    print()
