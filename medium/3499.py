"""
Problem: 3499. Maximize Active Section with Trade I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        one_cnt = s.count("1")
        zero_blocks = []
        idx = 0
        while idx < n:
            st = idx

            while idx < n and s[idx] == s[st]:
                idx += 1

            if s[st] == "0":
                zero_blocks.append(idx - st)
        m = len(zero_blocks)

        if m < 2:
            return one_cnt

        ans = 0
        for i in range(m - 1):
            ans = max(ans, zero_blocks[i] + zero_blocks[i + 1])

        return one_cnt + ans


if __name__ == "__main__":
    sol = Solution()
    print()
