"""
Problem: 2213. Longest Substring of One Repeating Character
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Node:
    __slots__ = ["size", "max_l", "pref_l", "suf_l", "pref_c", "suf_c"]

    def __init__(self, size=0, max_l=0, pref_l=0, suf_l=0, pref_c="", suf_c="") -> None:
        self.size = size
        self.max_l = max_l
        self.pref_l = pref_l
        self.suf_l = suf_l
        self.pref_c = pref_c
        self.suf_c = suf_c


class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.arr = list(arr)
        self.seg = [None] * (self.n << 2)

        if self.n:
            self.build(1, 0, self.n - 1)

    def merge(self, left: Node, right: Node) -> Node:
        res = Node(size=left.size + right.size)
        res.pref_c = left.pref_c
        res.suf_c = right.suf_c

        res.pref_l = left.pref_l
        if left.pref_l == left.size and left.pref_c == right.pref_c:
            res.pref_l += right.pref_l

        res.suf_l = right.suf_l
        if right.suf_l == right.size and right.suf_c == left.suf_c:
            res.suf_l += left.suf_l

        res.max_l = max(left.max_l, right.max_l)
        if left.suf_c == right.pref_c:
            res.max_l = max(res.max_l, left.suf_l + right.pref_l)

        return res

    def build(self, p: int, l: int, r: int) -> None:
        if l == r:
            c = self.arr[l]
            self.seg[p] = Node(1, 1, 1, 1, c, c)
            return
        mid = (l + r) >> 1

        self.build(p << 1, l, mid)
        self.build(p << 1 | 1, mid + 1, r)

        self.seg[p] = self.merge(self.seg[p << 1], self.seg[p << 1 | 1])

    def update(self, p: int, l: int, r: int, idx: int, char: str) -> None:
        if l == r:
            self.arr[l] = char
            self.seg[p] = Node(1, 1, 1, 1, char, char)
            return

        mid = (l + r) >> 1
        if idx <= mid:
            self.update(p << 1, l, mid, idx, char)
        else:
            self.update(p << 1 | 1, mid + 1, r, idx, char)

        self.seg[p] = self.merge(self.seg[p << 1], self.seg[p << 1 | 1])
        return


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        st = SegmentTree(s)
        ans = []

        for char, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, st.n - 1, idx, char)
            ans.append(st.seg[1].max_l)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
