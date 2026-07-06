"""
Problem: 1288. Remove Covered Intervals
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ret = []
        while intervals:
            cur = intervals[0]
            if len(intervals) == 1:
                ret.append(cur)
                break


if __name__ == "__main__":
    sol = Solution()
    print()
