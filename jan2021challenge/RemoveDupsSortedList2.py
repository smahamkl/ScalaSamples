
'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list. Return the linked list sorted as well.
Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        l3 = ListNode(0)
        tmp = head
        tmp1 = head.next
        res = l3
        while tmp:
            if not tmp1:
                l3.next = ListNode(tmp.val)
                l3 = l3.next
                tmp = tmp.next
            elif tmp.val == tmp1.val:
                dup_found = True
                while tmp1 and tmp1.val == tmp.val:
                    tmp1 = tmp1.next
                if not tmp1:
                    break
                tmp = tmp1
                tmp1 = tmp1.next
            elif tmp.val != tmp1.val:
                l3.next = ListNode(tmp.val)
                tmp = tmp1
                tmp1 = tmp1.next
                l3 = l3.next

        return res.next


sol = Solution()
l1  = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l3 = sol.deleteDuplicates(ListNode(5))

while l3:
    print(l3.val)
    l3 = l3.next