"""
Problem: 1807. Evaluate the Bracket Pairs of a String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict_knowledge = dict(knowledge)
        ans = []
        idx = -1
        for i, c in enumerate(s):
            if c == "(":
                idx = i
            elif c == ")":
                ans.append(dict_knowledge.get(s[idx + 1 : i], "?"))
                idx = -1
            elif idx < 0:
                ans.append(c)
        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print()
