"""
Problem: 3720. Lexicographically Smallest Permutation Greater Than Target
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        n = len(target)
        ans = []

        for i in range(n):
            t = ord(target[i]) - ord("a")

            if cnt[t] > 0:
                cnt[t] -= 1
                if self.fn(cnt, target[i + 1 :]):
                    ans.append(target[i])
                    continue
                cnt[t] += 1

            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    ans.append(chr(c + ord("a")))
                    ans.append("".join(chr(j + ord("a")) * cnt[j] for j in range(26)))

                    return "".join(ans)

            return ""
        return ""

    def fn(self, cnt: list[int], suf: str) -> bool:
        mx = "".join(
            chr(i + ord("a")) * cnt[i] for i in range(25, -1, -1) if cnt[i] > 0
        )

        return mx > suf


if __name__ == "__main__":
    sol = Solution()
    print()
