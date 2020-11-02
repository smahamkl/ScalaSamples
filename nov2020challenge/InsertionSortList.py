'''
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
'''

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def buildListNode(self, nodes:List[int])->ListNode:
        tmp = head = ListNode(0)
        for item in nodes:
            tmp.next = ListNode(item)
            tmp = tmp.next
        return head.next

    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        res = ListNode(head.val)
        head = head.next
        while head != None:
            found = False
            #--start from the beginning
            tmp = prev = res
            while tmp != None:
                if tmp.val >= head.val:
                    #--now insert the new node between prev & tmp
                    if prev != tmp:
                        prev.next = ListNode(head.val)
                        prev.next.next = tmp
                    else:
                        newnode = ListNode(head.val)
                        newnode.next = res
                        res = newnode
                    found = True
                    break
                prev = tmp
                tmp = tmp.next
            #---if the order is already sorted, then insert the new node at the end
            if not found:
                prev.next = ListNode(head.val)
            head = head.next
            
        return res
                    
sol = Solution()
head = sol.buildListNode([0,-1,-2,4])
#print(head.next.next.val)
print(sol.insertionSortList(head).val)
print(sol.insertionSortList(head).next.next.val)
# print(sol.insertionSortList(head).next.next.next.val)
# print(sol.insertionSortList(head).next.next.next.next.val)