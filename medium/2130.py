"""
Problem: 2130. Maximum Twin Sum of a Linked List
"""

import bisect
import heapq
import math
from collections import Counter, defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next

        bef = None
        cur = l
        while cur:
            nxt = cur.next
            cur.next = bef
            bef = cur
            cur = nxt
        
        ans = 0
        l = head
        r = bef

        while r:
            ans = max(ans, l.val + r.val)
            l = l.next
            r = r.next

        return ans



        

if __name__ == '__main__':
    sol = Solution()
    print(sol.2130. Maximum Twin Sum of a Linked List())
