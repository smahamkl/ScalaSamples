from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #first get the total length of A & B
        tmphA, lA, tmphB, lB = headA, 0, headB, 0
        while tmphA or tmphB:
            if tmphA:
                lA += 1
                tmphA = tmphA.next
            if tmphB:
                lB += 1
                tmphB = tmphB.next
        
        if lA > lB:
            while lA != lB:
                headA = headA.next
                lA -= 1
        elif lA < lB:
            while lA != lB:
                headB = headB.next
                lB -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None

sol = Solution()
l1 = ListNode(4)
l1.next = ListNode(1)
l1.next.next = ListNode(8)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
#---
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(1)
l2.next.next.next =l1.next.next

l3 = ListNode(0)
l3 = sol.getIntersectionNode(l1, l2)

while l3:
    print(l3.val, end= " ")
    l3 = l3.next

print()