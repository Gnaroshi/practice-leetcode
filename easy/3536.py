"""
Problem: 3536. Maximum Product of Two Digits
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxProduct(self, n: int) -> int:
        s = "".join(sorted(str(n), reverse=True))
        return int(s[0]) * int(s[1]) if len(s) >= 2 else int(s[0])


if __name__ == "__main__":
    sol = Solution()
    print()
