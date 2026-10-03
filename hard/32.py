"""
Problem: 32. Longest Valid Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def chk(s: str) -> bool:
            stk = []
            for char in s:
                if char == "(":
                    stk.append("(")
                elif stk and stk[-1] == "(":
                    stk.pop()
                else:
                    return False
            return len(stk) == 0

        mx = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if chk(s[i:j]):
                    mx = max(mx, j - i)

        return mx


if __name__ == "__main__":
    sol = Solution()
    print()
