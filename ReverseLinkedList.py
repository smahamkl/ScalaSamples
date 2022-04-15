from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            cache = cur.next
            cur.next = prev
            prev = cur
            cur = cache

        return prev

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

res = sol.reverseList(head)
while res:
    print(res.val, end=",")
    res = res.next