"""
Problem: 3963. Create Grid With Exactly One Path
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ret = []
        for _ in range(m - 1):
            ret.append("." + "#" * (n - 1))
        ret.append("." * n)
        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
