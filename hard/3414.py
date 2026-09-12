"""
Problem: 3414. Maximum Score of Non-overlapping Intervals
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = [(intervals[i][1], intervals[i][0], intervals[i][2], i) for i in range(n)]

        arr.sort(key=lambda x: x[0])

        dp = [[0] * 5 for _ in range(n + 1)]
        idx = [[[] for _ in range(5)] for _ in range(n + 1)]

        for i in range(n):
            r, l, w, cur_idx = arr[i]
            k = bisect.bisect_left(arr, (l,), hi=i)

            for j in range(1, 5):
                s1 = dp[i][j]
                s2 = dp[k][j - 1] + w

                if s1 > s2:
                    dp[i + 1][j] = dp[i][j]
                    idx[i + 1][j] = idx[i][j].copy()
                    continue

                nxt_idx = idx[k][j - 1].copy()
                nxt_idx.append(cur_idx)
                nxt_idx.sort()
                if s1 == s2 and idx[i][j] < nxt_idx:
                    nxt_idx = idx[i][j].copy()
                dp[i + 1][j] = s2
                idx[i + 1][j] = nxt_idx

        return idx[n][4]


if __name__ == "__main__":
    sol = Solution()
    print()
