"""
Problem: 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Any, Dict, List, Optional, Set, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        idx = [-1, -1]
        mn = float("inf")

        cur_idx = 1
        cur_node = head.next
        bef_node = head
        bef_cidx = 0
        first_cidx = 0

        while cur_node.next is not None:
            if (cur_node.val < bef_node.val and cur_node.val < cur_node.next.val) or (
                cur_node.val > bef_node.val and cur_node.val > cur_node.next.val
            ):
                if bef_cidx == 0:
                    bef_cidx = cur_idx
                    first_cidx = cur_idx
                else:
                    mn = min(mn, cur_idx - bef_cidx)
                    bef_cidx = cur_idx
            cur_idx += 1
            bef_node = cur_node
            cur_node = cur_node.next

        if mn != float("inf"):
            mx = bef_cidx - first_cidx
            idx = [mn, mx]


if __name__ == "__main__":
    sol = Solution()
    print()
