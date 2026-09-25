"""
Problem: 1096. Brace Expansion II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        idx = 0
        n = len(expression)

        def fn() -> set:
            nonlocal idx
            ret = set()
            while True:
                ret |= term()
                if idx < n and expression[idx] == ",":
                    idx += 1
                    continue
                else:
                    break

            return ret

        def term() -> set:
            nonlocal idx
            ret = {""}
            while idx < n and (expression[idx] == "{" or expression[idx].islower()):
                sub = item()
                tmp = set()
                for l in ret:
                    for r in sub:
                        tmp.add(l + r)
                ret = tmp
            return ret

        def item() -> set:
            nonlocal idx
            ret = set()
            if expression[idx] == "{":
                idx += 1
                ret = fn()
            else:
                ret = {expression[idx]}
            idx += 1
            return ret

        ret = fn()
        return sorted(list(ret))


if __name__ == "__main__":
    sol = Solution()
    print()
