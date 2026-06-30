"""
Problem: 1358. Number of Substrings Containing All Three Characters
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = r = tot = 0
        cnt = [0] * 3

        while r < n:
            cnt[ord(s[r]) - ord("a")] += 1

            while self._fn(cnt):
                tot += n - r
                cnt[ord(s[l]) - ord("a")] -= 1
                l += 1
            r += 1
        return tot

    def _fn(self, cnt: list) -> bool:
        return all(c > 0 for c in cnt)


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
