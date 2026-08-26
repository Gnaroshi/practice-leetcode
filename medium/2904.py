"""
Problem: 2904. Shortest and Lexicographically Smallest Beautiful String
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        cand = []
        n = len(s)
        if n < k:
            return ""
        mn = float("inf")

        r = n - 1
        while r >= 0:
            if s[r] == "0":
                r -= 1
                continue
            cnt = 0
            l = r
            while l >= 0:
                if s[l] == "1":
                    cnt += 1
                if cnt == k:
                    break
                l -= 1
            if cnt == k:
                sub = s[l : r + 1]
                cur = len(sub)

                if cur < mn:
                    mn = cur
                    cand = [sub]
                elif cur == mn:
                    cand.append(sub)

            r -= 1

        return sorted(cand)[0] if cand else ""


if __name__ == "__main__":
    sol = Solution()
    print()
