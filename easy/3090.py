"""
Problem: 3090. Maximum Length Substring With Two Occurrences
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        n = len(s)
        l, r = 0, 1
        mx = 0
        cnt[s[0]] += 1
        while True:
            if r == n:
                break

            if cnt[s[r]] < 2:
                cnt[s[r]] += 1
                r += 1
            elif cnt[s[r]] == 2:
                while True:
                    if s[l] == s[r]:
                        cnt[s[l]] -= 1
                        l += 1
                        break

                    cnt[s[l]] -= 1
                    l += 1

            mx = max(mx, r - l)

        return mx


if __name__ == "__main__":
    sol = Solution()
    print()
