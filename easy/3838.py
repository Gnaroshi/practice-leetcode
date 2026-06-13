"""
Problem: 3838. Weighted Word Mapping
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ret = ""
        for w in words:
            cur = 0
            for c in w:
                cur += weights[ord(c) - ord("a")]
            cur %= 26
            ret += chr(25 - cur + ord("a"))

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.problem_name())
