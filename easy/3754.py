"""
Problem: 3754. Concatenate Non-Zero Digits and Multiply by Sum I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = str(n)
        x = ""
        sm = 0
        for c in s:
            if c != "0":
                sm += int(c)
                x += c

        return int(x) * sm if len(x) != 0 else 0


if __name__ == "__main__":
    sol = Solution()
    print()
