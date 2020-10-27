from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def buildListNode(self, nodes:List[int])->ListNode:
        tmp = head = ListNode(0)
        for item in nodes:
            tmp.next = ListNode(item)
            tmp = tmp.next
        tmp.next = head.next
        return head.next

    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        if head.next != None:
            fast = head.next
        while True:
            if fast.next == None:
                return None
            
            fast = fast.next
            slow = slow.next
            print(slow.val, fast.val)

            #--now check if fast can reach the slow pointer---
            #--only true if there is a cycle
            tmp = fast
            while True:
                if tmp.next == None:
                    return False
                elif tmp.next == slow:
                    return tmp
                tmp = tmp.next

            



sol = Solution()
listNode = sol.buildListNode([3,2,0,-4])
print(sol.detectCycle(listNode).val)
# print(listNode.val)
# print(listNode.next.next.next.next.val)