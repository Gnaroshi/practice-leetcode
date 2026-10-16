"""
Problem: 2916. Subarrays Distinct Element Sum of Squares II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class BinaryIndexedTree:
    def __init__(self, n: int) -> None:
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, l: int, r: int, d: int) -> None:
        self._add(l, d)
        self._add(r + 1, -d)

    def _add(self, index: int, d: int) -> None:
        index += 1
        _index = index
        while index <= self.size:
            self._tree1[index] += d
            self._tree2[index] += (_index - 1) * d
            index += self._lowbit(index)

    def query(self, l: int, r: int) -> int:
        return self._query(r) - self._query(l - 1)

    def _query(self, index: int) -> int:
        index += 1
        if index > self.size:
            index = self.size
        _index = index
        ret = 0
        while index > 0:
            ret += _index * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return ret


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ret = cur = 0
        bit = BinaryIndexedTree(n + 10)
        seen = {}
        MD = 10**9 + 7
        for i, a in enumerate(nums):
            j = seen.get(a, -1) + 1
            cur = (cur + bit.query(j, i) * 2 + i - j + 1) % MD
            ret = (ret + cur) % MD
            bit.add(j, i, 1)
            seen[a] = i

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
