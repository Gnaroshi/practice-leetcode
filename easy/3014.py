"""
Problem: 3014. Minimum Number of Pushes to Type Word I
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = sorted(Counter(word).items(), key=lambda x: (-x[1], x[0]))
        idx = 0
        ret = 0
        for ch, cn in cnt:
            ret += cn * (idx // 8 + 1)
            idx += 1

        return ret


if __name__ == "__main__":
    sol = Solution()
    print()
