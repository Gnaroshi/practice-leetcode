"""
Problem: 1520. Maximum Number of Non-Overlapping Substrings
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


class Seg:
    def __init__(self, left=-1, right=-1) -> None:
        self.left = left
        self.right = right

    def __lt__(self, rhs):
        if self.right == rhs.right:
            return self.left > rhs.left
        return self.right < rhs.right


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        seg = [Seg() for _ in range(26)]
        for i in range(len(s)):
            char_idx = ord(s[i]) - ord("a")
            if seg[char_idx].left == -1:
                seg[char_idx].left = seg[char_idx].right = i
            else:
                seg[char_idx].right = i

        for i in range(26):
            if seg[i].left != -1:
                j = seg[i].left
                while j <= seg[i].right:
                    char_idx = ord(s[j]) - ord("a")
                    if (
                        seg[i].left <= seg[char_idx].left
                        and seg[char_idx].right <= seg[i].right
                    ):
                        pass
                    else:
                        seg[i].left = min(seg[i].left, seg[char_idx].left)
                        seg[i].right = max(seg[i].right, seg[char_idx].right)
                        j = seg[i].left
                    j += 1
        seg.sort()
        ans = list()
        end = -1
        for segment in seg:
            l, r = segment.left, segment.right
            if l == -1:
                continue
            if end == -1 or l > end:
                end = r
                ans.append(s[l : r + 1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    print()
