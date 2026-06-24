"""
Problem: 3700. Number of ZigZag Arrays II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    MD = 10**9 + 7

    def mul(self, a, b):
        n = len(a)
        m = len(b[0])
        ret = [[0] * m for _ in range(n)]

        for i in range(n):
            for k in range(len(a[0])):
                r = a[i][k]
                if r == 0:
                    continue
                for j in range(m):
                    ret[i][j] = (ret[i][j] + r * b[k][j]) % self.MD

        return ret

    def pmul(self, b, e, ret):
        while e > 0:
            if e & 1:
                ret = self.mul(ret, b)
            b = self.mul(b, b)
            e >>= 1
        return ret

    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        w = r - l + 1

        if n == 1:
            return w

        w2 = 2 * w
        u = [[0] * w2 for _ in range(w2)]
        for i in range(w):
            for j in range(i):
                u[i][j + w] = 1
            for j in range(i + 1, w):
                u[i+w][j] = 1

        dp =[[1] * w2]
        dp = self.pmul(u, n -1 , dp)
        ans = 0
        for i in range(w2):
            ans = (ans + dp[0][i]) % self.MD

        return ans



if __name__ == '__main__':
    sol = Solution()
    print(sol.3700. Number of ZigZag Arrays II())
