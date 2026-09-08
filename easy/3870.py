"""
Problem: 3870. Count Commas in Range
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 1000 + 1)


if __name__ == "__main__":
    sol = Solution()
    print()
