"""
Problem: 1291. Sequential Digits
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ll = len(str(low))
        hl = len(str(high))
        ret = []
        sd = "123456789"
        for i in range(ll, hl + 1):
            for j in range(10 - i):
                cur = sd[j : j + i]
                icur = int(cur)
                if low <= icur <= high:
                    ret.append(icur)
                if icur >= high:
                    break
        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
