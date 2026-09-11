"""
Problem: 3483. Unique 3-Digit Even Numbers
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        set_arr = set()

        def fn(chk: List[bool], cur: str, cnt: int):
            if cnt == 3:
                if int(cur) % 2 == 0:
                    set_arr.add(cur)
                return
            for i, b in enumerate(chk):
                if b:
                    if cnt == 0 and digits[i] == 0:
                        continue

                    cur += str(digits[i])
                    chk[i] = False
                    fn(chk, cur, cnt + 1)
                    chk[i] = True
                    cur = cur[:cnt]

        fn([True] * len(digits), "", 0)

        return len(set_arr)


if __name__ == "__main__":
    sol = Solution()
    print()
