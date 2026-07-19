"""
Problem: 1081. Smallest Subsequence of Distinct Characters
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        chk = [0] * 26
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - ord("a")] += 1

        ret = []

        for c in s:
            cur = ord(c) - ord("a")
            if not chk[cur]:
                while ret and ret[-1] > c:
                    t = ord(ret[-1]) - ord("a")
                    if cnt[t] > 0:
                        chk[t] = 0
                        ret.pop()
                    else:
                        break
                chk[cur] = 1
                ret.append(c)
            cnt[cur] -= 1

        return "".join(ret)


if __name__ == "__main__":
    sol = Solution()
    print()
