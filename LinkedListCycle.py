from typing import List
from typing import Optional
'''
LeetCode 141
LinkedList Cycle
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,f= head, head

        while s:
            if f.next == None:
                return False
            
            f = f.next
            if f.next != None:
                f = f.next
            else:
                return False
            
            s = s.next

            if s == f:
                return True
            
        return False

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
# head.next.next.next = ListNode(-4)
# head.next.next.next.next = head.next
print(sol.hasCycle(head))