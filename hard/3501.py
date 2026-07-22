"""
Problem: 3501. Maximize Active Section with Trade II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = arr
        self.seg = [0] * (self.n << 2)

        if self.n:
            self.build(1, 0, self.n - 1)

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = self.arr[l]
            return
        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = max(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, L: int, R: int) -> int:
        if L > R:
            return 0

        def _query(p: int, l: int, r: int) -> int:
            if L <= l and r <= R:
                return self.seg[p]

            mid = (l + r) >> 1
            res = 0

            if L <= mid:
                res = max(res, _query(p << 1, l, mid))
            if R > mid:
                res = max(res, _query(p << 1 | 1, mid + 1, r))

            return res

        return _query(1, 0, self.n - 1)


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:
        n = len(s)
        one_cnt = s.count("1")

        zero_blocks = []
        block_left = []
        block_right = []

        idx = 0
        while idx < n:
            st = idx

            while idx < n and s[idx] == s[st]:
                idx += 1

            if s[st] == "0":
                zero_blocks.append(idx - st)
                block_left.append(st)
                block_right.append(idx - 1)

        m = len(zero_blocks)
        if m < 2:
            return [one_cnt] * len(queries)

        tmp_sum = [zero_blocks[i] + zero_blocks[i + 1] for i in range(m - 1)]
        seg = SegmentTree(tmp_sum)
        ans = []

        for l, r in queries:
            bl = bisect.bisect_left(block_right, l)
            br = bisect.bisect_right(block_left, r) - 1

            if bl > m - 1 or br < 0 or bl >= br:
                ans.append(one_cnt)
                continue

            first_len = block_right[bl] - max(block_left[bl], l) + 1
            last_len = min(block_right[br], r) - block_left[br] + 1

            if bl + 1 == br:
                ans.append(one_cnt + first_len + last_len)
                continue

            v1 = first_len + zero_blocks[bl + 1]
            v2 = zero_blocks[br - 1] + last_len
            v3 = seg.query(bl + 1, br - 2)

            ans.append(one_cnt + max(v1, v2, v3))

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
