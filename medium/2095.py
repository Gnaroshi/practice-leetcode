"""
Problem: 2095. Delete the Middle Node of a Linked List
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
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        l, r = head, head.next.next
        
        while r and r.next:
            l = l.next
            r = r.next.next

        l.next = l.next.next

        return head


        

if __name__ == '__main__':
    sol = Solution()
    print(sol.2095. Delete the Middle Node of a Linked List())
