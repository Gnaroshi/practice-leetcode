"""
Problem: 3612. Process String with Special Operations I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def processStr(self, s: str) -> str:
        ret = ""
        for c in s:
            if c == '*':
                ret = ret[:-1]
            elif c == '#':
                ret += ret
            elif c == '%':
                ret = ret[::-1]
            else:
                ret += c
        return ret


if __name__ == '__main__':
    sol = Solution()
    print(sol.3612. Process String with Special Operations I())
