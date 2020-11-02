from typing import List
'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

'''
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
        #tmp.next = head.next.next.next.next
        return head.next

    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        
        res = ""
        while head != None:
            res += str(head.val)
            head = head.next
        return int(res, 2)


sol = Solution()
head = sol.buildListNode([0])
print(sol.getDecimalValue(head))
