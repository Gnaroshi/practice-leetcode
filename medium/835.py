"""
Problem: 835. Image Overlap
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        def non_zero_cells(img: List[List[int]]) -> List[List[int]]:
            ret = []
            for x in range(n):
                for y in range(n):
                    if img[x][y] == 1:
                        ret.append((x, y))

            return ret

        transformation_cnt = defaultdict(int)
        mx = 0

        img1_1 = non_zero_cells(img1)
        img2_1 = non_zero_cells(img2)

        for x1, y1 in img1_1:
            for x2, y2 in img2_1:
                vec = (x2 - x1, y2 - y1)
                transformation_cnt[vec] += 1
                mx = max(mx, transformation_cnt[vec])

        return mx


if __name__ == "__main__":
    sol = Solution()
    print()
