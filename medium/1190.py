"""
Problem: 1190. Reverse Substrings Between Each Pair of Parentheses
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def reverseParentheses(self, s: str) -> str:
        ans = []
        dq = deque()
        for c in s:
            if c == "(":
                dq.append(len(ans))
            elif c == ")":
                cur = dq.pop()
                ans[cur:] = ans[cur:][::-1]
            else:
                ans.append(c)
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print()
