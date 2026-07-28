"""
Problem: 3517. Smallest Palindromic Rearrangement I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        counter = Counter(char for char in s if char.isalpha())
        counter = sorted(counter.items())
        ret = ""
        t = ""
        for c, cnt in counter:
            if cnt == 0:
                continue
            elif cnt % 2 == 1:
                t += c
            ret += c * (cnt // 2)

        return ret + t + ret[::-1]


if __name__ == "__main__":
    sol = Solution()
    print()
