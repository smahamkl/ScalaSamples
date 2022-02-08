from os import TMP_MAX
from typing import List, Optional
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  
        dummy = ListNode(0, head)
        
        # 1. get to left position
        leftPrev, curr = dummy, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next 

        # 2. reversal from left to right 
        prev = None
        for i in range(right - left + 1):
            tnext = curr.next 
            curr.next = prev 
            prev, curr = curr, tnext 

        # 3. connect left - 1 to right and 
        # right + 1 to left 
        # update pointers 
        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy.next


        

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
head = sol.reverseBetween(head, 1,3)
while head:
    print(head.val)
    head = head.next