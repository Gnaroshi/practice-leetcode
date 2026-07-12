"""
Problem: 1331. Rank Transform of an Array
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        tarr = sorted([(v, i) for i, v in enumerate(arr)])
        rarr = []
        rank = 0
        cmx = float("inf")
        for v, i in tarr:
            if cmx != v:
                rank += 1
                cmx = v
            rarr.append((i, rank))
        rarr = [r[1] for r in sorted(rarr)]

        return rarr


if __name__ == "__main__":
    sol = Solution()
    print()
