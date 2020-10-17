from typing import List
'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        elif head.next == None:
            return head
        return self.divideList(head)
    
    def divideList(self, head:ListNode) -> ListNode:
        slow_ptr = fast_ptr = head
        #print(head.val)
        if head.next == None:
            return head
        while fast_ptr != None and fast_ptr.next != None:
            tmp  = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        tmp.next = None
        i = self.divideList(head)
        j = self.divideList(slow_ptr)
        return self.merge(i, j)
    def merge(self, i, j):
        """
                 This method mainly achieves the combined operation
                 The process of combining is to start from i and j. It is to start from the beginning and the middle.
                 Finally return to the head
        :param i:ListNode
        :param j:ListNode
        :return:
        """
        TempNode = ListNode(0)
        temp = TempNode
        while i is not None and j is not None:
            if i.val <= j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            temp = temp.next
        if i is not None:
            temp.next = i
        if j is not None:
            temp.next = j
        return TempNode.next


node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)
print(Solution().sortList(node).val)
