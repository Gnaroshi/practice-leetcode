"""
Problem: 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord("a")] += 1

        n = len(s)
        if n == 1:
            return s if s > target else ""

        odd_c = ""
        for i in range(26):
            if cnt[i] % 2 == 1:
                if odd_c != "":
                    return ""

                odd_c = chr(i + ord("a"))

            cnt[i] //= 2

        prefix = []

        def fn(c):
            l = prefix.copy()
            l.append(c)

            for i in range(25, -1, -1):
                l.extend([chr(i + ord("a"))] * cnt[i])

            pd = l + [odd_c] + l[::-1]

            return "".join(pd) > target

        for i in range(n // 2):
            flag = False
            for j in range(26):
                if cnt[j] == 0:
                    continue
                cnt[j] -= 1

                if fn(chr(j + ord("a"))):
                    prefix.append(chr(j + ord("a")))
                    flag = True
                    break
                else:
                    cnt[j] += 1

            if not flag:
                return ""

            if prefix[i] > target[i]:
                l = prefix[:]

                for j in range(26):
                    l.extend([chr(j + ord("a"))] * cnt[j])

                pd = l + [odd_c] + l[::-1]

                return "".join(pd)

        ans = prefix + [odd_c] + prefix[::-1]

        return "".join(ans)


if __name__ == "__main__":
    sol = Solution()
    print()
