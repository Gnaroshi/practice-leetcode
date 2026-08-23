"""
Problem: 1927. Sum Game
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        bob, ali = 0, 0
        bob_q, ali_q = 0, 0
        for i in range(0, n // 2):
            if num[i] == "?":
                bob_q += 1
            else:
                bob += int(num[i])

        for i in range(n // 2, n):
            if num[i] == "?":
                ali_q += 1
            else:
                ali += int(num[i])

        return (bob_q + ali_q) % 2 == 1 or bob - ali != (ali_q - bob_q) * 9 // 2


if __name__ == "__main__":
    input_str = input()
    sol = Solution().sumGame(input_str)
    print()
