"""
Problem: 3518. Smallest Palindromic Rearrangement II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def comb(self, n: int, m: int, k_limit: int) -> int:
        ret = 1
        m = min(m, n - m)

        for i in range(1, m + 1):
            ret = ret * (n - i + 1) // i
            if ret > k_limit:
                return k_limit + 1

        return ret

    def perm(self, rem: int, bucket: List[int], k: int) -> int:
        ways = 1
        for i in range(26):
            if bucket[i] == 0:
                continue
            ways *= self.comb(rem, bucket[i], k)
            if ways > k:
                break
            rem -= bucket[i]

        return ways

    def smallestPalindrome(self, s: str, k: int) -> str:
        partition = len(s) // 2
        bucket = [0] * 26

        for i in range(partition):
            bucket[ord(s[i]) - 97] += 1

        left_chars = []
        st_idx = 1

        for pos in range(partition):
            for i in range(26):
                if bucket[i] == 0:
                    continue

                bucket[i] -= 1

                ways = self.perm(partition - pos - 1, bucket, k)

                if st_idx + ways > k:
                    left_chars.append(chr(i + 97))
                    break

                bucket[i] += 1
                st_idx += ways

        if len(left_chars) < partition:
            return ""

        mid = s[partition] if len(s) % 2 == 1 else ""
        left_str = "".join(left_chars)
        right_str = left_str[::-1]

        return left_str + mid + right_str


if __name__ == "__main__":
    sol = Solution()
    print()
