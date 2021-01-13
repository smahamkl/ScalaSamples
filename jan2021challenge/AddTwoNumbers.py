from typing import List
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l2:
            return l1
        elif not l1:
            return l2
        l3 = ListNode(0)
        head = l3
        sum = 0
        carry = 0
        while l1 and l2:
            sum = (l1.val + l2.val + carry)%10
            carry = int((l1.val + l2.val + carry)/10)
            l3.next = ListNode(sum)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            sum = (l1.val + carry)%10
            carry = int((l1.val + carry)/10)
            l3.next = ListNode(sum)
            l1 = l1.next
            l3 = l3.next
            
        while l2:
            sum = (l2.val + carry)%10
            carry = int((l2.val + carry)/10)
            l3.next = ListNode(sum)
            l2 = l2.next
            l3 = l3.next 

        if carry > 0:
            l3.next = ListNode(carry)
        
        return head.next


sol = Solution()
# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)

# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)

l1 = ListNode(0)
l2 = ListNode(0)

l3 = sol.addTwoNumbers(l1,l2)
while l3:
    print(l3.val)
    l3 = l3.next
