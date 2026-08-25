"""
Problem: 3718. Smallest Missing Multiple of K
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        arr = [x for x in nums if x % k == 0]
        arr.sort()
        print(f"arr: {arr}")
        n = len(arr)
        for i in range(1, n + 1):
            if k * i not in arr:
                return k * i
        return (n + 1) * k


if __name__ == "__main__":
    sol = Solution()
    print()
