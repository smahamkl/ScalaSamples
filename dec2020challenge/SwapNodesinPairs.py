'''
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes. Only nodes itself may be changed.

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        p = head
        new_head = q = head.next
        prev = None
        while p and q:
            if prev:
                prev.next = q
            p.next = q.next
            q.next = p
            
            prev = p
            p = p.next
            if not p:
                break
            q = p.next
            
        return new_head