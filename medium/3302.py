"""
Problem: 3302. Find the Lexicographically Smallest Valid Sequence
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        suf = [m] * (n + 1)

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf[i] = j
                j -= 1
            else:
                suf[i] = suf[i + 1]

        ans = []
        j = 0
        chk = False

        for i in range(n):
            if j == m:
                break
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not chk and suf[i + 1] <= j + 1:
                ans.append(i)
                j += 1
                chk = True

        if len(ans) == m:
            return ans
        return []


if __name__ == "__main__":
    sol = Solution()
    print()
