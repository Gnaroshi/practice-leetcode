"""
Problem: 1967. Number of Strings That Appear as Substrings in Word
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ret = 0
        for p in patterns:
            if p in word:
                ret += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
