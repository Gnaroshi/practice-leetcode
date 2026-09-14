"""
Problem: 836. Rectangle Overlap
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)

        return intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and intersect(
            rec1[1], rec1[3], rec2[1], rec2[3]
        )


if __name__ == "__main__":
    sol = Solution()
    print()
