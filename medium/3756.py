"""
Problem: 3756. Concatenate Non-Zero Digits and Multiply by Sum II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    MD = 10**9 + 7
    SZ = 100001
    pw10 = [1] * SZ
    for i in range(1, SZ):
        pw10[i] = pw10[i - 1] * 10 % MD

    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        sm = [0] * (n + 1)
        x = [0] * (n + 1)
        cnt = [0] * (n + 1)
        for i, c in enumerate(s):
            d = int(c)
            sm[i + 1] = sm[i] + d
            x[i + 1] = (x[i] * 10 + d) % self.MD if d > 0 else x[i]
            cnt[i + 1] = cnt[i] + (d > 0)

        m = len(queries)
        ret = [0] * m
        for i in range(m):
            l = queries[i][0]
            r = queries[i][1] + 1
            sz = cnt[r] - cnt[l]
            ret[i] = (x[r] - x[l] * self.pw10[sz]) * (sm[r] - sm[l]) % self.MD

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
