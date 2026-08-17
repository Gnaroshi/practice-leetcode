"""
Problem: 1563. Stone Game V
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(l: int, r: int) -> int:
            if l == r:
                return 0

            tot = sum(stoneValue[l : r + 1])
            sl = ans = 0
            for i in range(l, r):
                sl += stoneValue[i]
                sr = tot - sl

                if sl < sr:
                    ans = max(ans, dfs(l, i) + sl)
                elif sl > sr:
                    ans = max(ans, dfs(i + 1, r) + sr)
                else:
                    ans = max(ans, max(dfs(l, i), dfs(i + 1, r)) + sl)

            return ans

        n = len(stoneValue)
        return dfs(0, n - 1)


if __name__ == "__main__":
    sol = Solution()
    print()
