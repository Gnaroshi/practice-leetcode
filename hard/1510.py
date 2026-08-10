"""
Problem: 1510. Stone Game IV
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(maxsize=None)
        def dfs(remain):
            if remain == 0:
                return False

            sqrt_cur = int(remain**0.5)
            for i in range(1, sqrt_cur + 1):
                if not dfs(remain - i * i):
                    return True

            return False

        return dfs(n)


if __name__ == "__main__":
    sol = Solution()
    print()
