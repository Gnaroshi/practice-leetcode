"""
Problem: 1111. Maximum Nesting Depth of Two Valid Parentheses Strings
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ret = []
        depth = 0
        for c in seq:
            if c == "(":
                depth += 1
                ret.append(depth % 2)
            if c == ")":
                ret.append(depth % 2)
                depth -= 1
        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
