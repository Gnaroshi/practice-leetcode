"""
Problem: 3723. Maximize Sum of Squares of Digits
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        q, r = divmod(sum, 9)
        ans = "9" * q
        if r > 0:
            ans += str(r)
        ans += "0" * (num - len(ans))
        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
