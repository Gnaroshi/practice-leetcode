"""
Problem: 3691. Maximum Total Subarray Value II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.segment_tree = [(0,0) for _ in range(4 * self.n)]
        self.build(1, 0, self.n - 1)

    def build(self, node, l, r):
        if l == r:
            self.segment_tree[node] = (self.arr[l], self.arr[l])
            return

        mid = l + (r - l) // 2
        self.build(2 * node, l, mid)
        self.build(2 * node + 1, mid + 1, r)
        self.segment_tree[node] = (
                max(self.segment_tree[node * 2][0], self.segment_tree[node * 2 + 1][0]),
                min(self.segment_tree[node * 2][1], self.segment_tree[node * 2 + 1][1])
                )

    def query(self, ql, qr, node = 1, l = 0, r = None):
        if r == None:
            r = self.n - 1
                
        if ql > r or qr < l:
            return (-math.inf, math.inf)

        if ql <= l and qr >=r:
            return self.segment_tree[node]

        mid = l + (r - l) // 2
        lmx, lmn = self.query(ql, qr, node * 2, l, mid)
        rmx, rmn = self.query(ql, qr, node * 2 + 1, mid + 1, r)

        return (
                max(lmx, rmx),
                min(lmn, rmn)
                )

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        segment_tree = SegmentTree(nums)
        max_heap = []

        mx, mn = segment_tree.query(0, n - 1)
        heapq.heappush(max_heap, (-(mx - mn), 0, n - 1))
        vist = set()
        vist.add((0, n - 1))
        ans = 0

        while k:
            k -= 1
            v, l, r = heapq.heappop(max_heap)
            v = -v
            ans += v

            if l + 1 <= r and not (l + 1, r) in vist:
                mx, mn = segment_tree.query(l + 1, r)
                heapq.heappush(max_heap, (-(mx - mn), l + 1, r))
                vist.add((l + 1, r))

            if r - 1 >= l and not (l, r - 1) in vist:
                mx, mn = segment_tree.query(l, r - 1)
                heapq.heappush(max_heap, (-(mx - mn), l, r - 1))
                vist.add((l, r - 1))

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.3691. Maximum Total Subarray Value II())
