"""
Problem: 3525. Find X Value of Array II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Node:
    __slots__ = ["prod", "pref"]

    def __init__(self, k: int):
        self.prod = 1
        self.pref = [0] * k


class SegmentTree:
    def __init__(self, arr: List[int], k: int):
        self.n = len(arr)
        self.k = k
        self.arr = arr
        self.seg = [None] * (self.n << 2)

        if self.n > 0:
            self.build(1, 0, self.n - 1)

    def make_leaf(self, val: int) -> Node:
        node = Node(self.k)
        v = val % self.k
        node.prod = v
        node.pref[v] = 1
        return node

    def merge(self, left: Node, right: Node) -> Node:
        res = Node(self.k)

        res.prod = (left.prod * right.prod) % self.k

        for i in range(self.k):
            res.pref[i] = left.pref[i]

        for i in range(self.k):
            if right.pref[i] > 0:
                new_mod = (left.prod * i) % self.k
                res.pref[new_mod] += right.pref[i]

        return res

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            self.seg[p] = self.make_leaf(self.arr[l])
            return
        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = self.merge(self.seg[p << 1], self.seg[p << 1 | 1])

    def update(self, p: int, l: int, r: int, idx: int, val: int) -> None:
        if l == r:
            self.arr[l] = val
            self.seg[p] = self.make_leaf(val)

            return

        mid = (l + r) >> 1
        if idx <= mid:
            self.update(p << 1, l, mid, idx, val)
        else:
            self.update(p << 1 | 1, mid + 1, r, idx, val)
        self.seg[p] = self.merge(self.seg[p << 1], self.seg[p << 1 | 1])

    def query(self, p: int, l: int, r: int, ql: int, qr: int) -> Node:
        if ql <= l and r <= qr:
            return self.seg[p]

        mid = (l + r) >> 1
        left_node = None
        right_node = None

        if ql <= mid:
            left_node = self.query(p << 1, l, mid, ql, qr)
        if qr > mid:
            right_node = self.query(p << 1 | 1, mid + 1, r, ql, qr)

        if not left_node:
            return right_node
        if not right_node:
            return left_node
        return self.merge(left_node, right_node)


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        st = SegmentTree(nums, k)
        ans = []
        n = len(nums)

        for idx, val, start, x in queries:
            st.update(1, 0, n - 1, idx, val)
            res_node = st.query(1, 0, n - 1, start, n - 1)
            ans.append(res_node.pref[x])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
