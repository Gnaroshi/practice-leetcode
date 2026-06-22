"""
Problem: 1189. Maximum Number of Balloons
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c_cnt = {chr(ord("a") + i): 0 for i in range(26)}
        for c in text:
            c_cnt[c] += 1
        c_cnt["l"] //= 2
        c_cnt["o"] //= 2
        tgt = "balon"
        mn = math.inf

        return min(c_cnt[c] for c in "balon")


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
