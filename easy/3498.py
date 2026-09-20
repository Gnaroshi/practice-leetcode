"""
Problem: 3498. Reverse Degree of a String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def reverseDegree(self, s: str) -> int:
        ret = 0
        for i, c in enumerate(s):
            ret += (ord("z") - ord(c) + 1) * (i + 1)

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
