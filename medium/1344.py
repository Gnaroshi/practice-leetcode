"""
Problem: 1344. Angle Between Hands of a Clock
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h, m = float(hour), float(minutes)
        md = 6 * m
        if h == 12:
            h = 0
        hd = 30 * h + 0.5 * m
        mxd = max(hd, md)
        mnd = min(hd, md)
        # print(f"mnd: {mnd} mxd: {mxd}")
        ans = min((mxd - mnd), 360 - abs(mnd - mxd))

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.angleClock(1, 57))
