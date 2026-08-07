"""
Problem: 3348. Smallest Divisible Digit Product II
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tt = t
        for i in range(2, 10):
            while tt % i == 0:
                tt //= i

        if tt > 1:
            return "-1"

        n = len(num)
        arr = [0] * (n + 1)
        arr[0] = t
        idx = n - 1

        nl = list(num)
        for i in range(n):
            if nl[i] == "0":
                idx = i
                break
            arr[i + 1] = arr[i] // math.gcd(arr[i], int(nl[i]))

        if arr[n] == 1:
            return num

        for i in range(idx, -1, -1):
            while True:
                nl[i] = chr(ord(nl[i]) + 1)
                if nl[i] > "9":
                    break

                t_cur = arr[i] // math.gcd(arr[i], int(nl[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while t_cur % k != 0:
                        k -= 1
                    t_cur //= k
                    nl[j] = str(k)

                if t_cur == 1:
                    return "".join(nl)

        ret = []
        ot = t
        for i in range(9, 1, -1):
            while ot % i == 0:
                ret.append(str(i))
                ot //= i

        ret_str = "".join(ret)
        pd = max(n + 1 - len(ret_str), 0)
        ret_str += "1" * pd

        return ret_str[::-1]


if __name__ == "__main__":
    sol = Solution()
    print()
