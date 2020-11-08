from typing import List
'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

SOLUTION:
---------
Since the list starts with the most significant degit at the head position, we need to solve it using
recursion. One workaround is to make the two lists of same size by appending 0s at the beginning to the
smaller list and then perform the addition them using recursion
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.carry = 0

    def buildListNode(self, nodes:List[int])->ListNode:
        tmp = head = ListNode(0)
        for item in nodes:
            tmp.next = ListNode(item)
            tmp = tmp.next
        return head.next
    
    def addSameSizeLists(self, l1:ListNode, l2:ListNode, le:int) -> ListNode:
        if l1 != None:
            l = self.addSameSizeLists(l1.next, l2.next, le+1)
            sum = (l1.val + l2.val + self.carry) % 10
            self.carry = int((l1.val + l2.val + self.carry) / 10)
            n = ListNode(sum)
            n.next = l
            return n
        else:
            return None
            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #---get lengths of l1 and l2----
        tmp1 = l1
        tmp2 = l2
        len1 = 0
        len2 = 0
        while tmp1 != None or tmp2 != None:
            if tmp1:
                len1+=1
                tmp1 = tmp1.next
            if tmp2:
                len2+=1
                tmp2 = tmp2.next
        diff = abs(len1 - len2)
        res = tmpNode = ListNode(0)

        while diff > 0:
            tmpNode.next = ListNode(0)
            tmpNode = tmpNode.next
            diff -= 1            

        if len1 > len2:
            tmpNode.next = l2
            res =  self.addSameSizeLists(l1, res.next, 0)
        elif len1 < len2:
            tmpNode.next = l1
            res =  self.addSameSizeLists(res.next, l2, 0)
        elif len1 == len2:
            res = self.addSameSizeLists(l1, l2, 0)
        if self.carry > 0:
                n1 = ListNode(self.carry)
                n1.next = res
                return n1
        else:
            return res

sol = Solution()
num1 = sol.buildListNode([5])
num2 = sol.buildListNode([5])
res = sol.addTwoNumbers(num1, num2)
print(res.val)
print(res.next.val)
#print(res.next.next.val)
#print(res.next.next.next.val)
#print(res.next.next.next.next.val)