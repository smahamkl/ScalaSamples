class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(0)
        res = l3

        while l1 and l2:
            if l1.val < l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        return res.next

sol = Solution()
l1  = ListNode(1)
l1.next = ListNode(3)
l1.next.next = ListNode(5)
l2  = ListNode(7)
l2.next = ListNode(8)
l2.next.next = ListNode(9)
l3 = sol.mergeTwoLists(None,None)

while l3:
    print(l3.val)
    l3 = l3.next