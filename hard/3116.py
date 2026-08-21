"""
Problem: 3116. Kth Smallest Amount With Single Denomination Combination
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        new_coins = []
        for x in coins:
            if all(x % y for y in new_coins):
                new_coins.append(x)
        coins = new_coins

        n = len(coins)
        m = 1 << n
        lcm = [1] * m

        l = k
        r = coins[0] * k + 1

        for mask in range(1, m):
            pre_mask = mask & (mask - 1)
            i = (mask & -mask).bit_length() - 1

            t = lcm[pre_mask] // math.gcd(lcm[pre_mask], coins[i])
            if t <= r // coins[i]:
                lcm[mask] = t * coins[i]
            else:
                lcm[mask] = r + 1

        def get(x: int) -> int:
            cnt = 0
            for mask in range(1, m):
                if lcm[mask] > x:
                    continue
                if mask.bit_count() & 1:
                    cnt += x // lcm[mask]
                else:
                    cnt -= x // lcm[mask]
            return cnt

        while l < r:
            md = (l + r) // 2
            if get(md) >= k:
                r = md
            else:
                l = md + 1

        return l


if __name__ == "__main__":
    sol = Solution()
    print()
