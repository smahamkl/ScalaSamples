
'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        slow_ptr = head
        tot_nodes = 0
        orig_head = head

        if head == None or k == 0:
            return head

        while head != None:
            head = head.next
            tot_nodes += 1
        
        if (tot_nodes == 1) or (k % tot_nodes == 0):
            return orig_head

        if k > tot_nodes:
            k = k % tot_nodes
        head = orig_head
        print("value of k:" + str(k))
        
        tot_nodes = 0
        while head != None:
            if tot_nodes >= k:
                slow_ptr = slow_ptr.next
            head = head.next
            tot_nodes += 1

        tmphead = slow_ptr
        while slow_ptr.next != None:
            #print("slow pointer:" + str(slow_ptr.val))
            slow_ptr = slow_ptr.next
        i = 1
        while i <= (tot_nodes - k):
            #print("running from head pointer:" + str(i))
            slow_ptr.next = orig_head
            slow_ptr = slow_ptr.next
            orig_head = orig_head.next
            i += 1
        slow_ptr.next = None
        return tmphead
        

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
newhead = sol.rotateRight(head, 702)
while newhead != None:
    print(newhead.val)
    newhead = newhead.next
# head = ListNode(1, ListNode(2, None))
# newhead = sol.rotateRight(head, 1)
# while newhead != None:
#     print(newhead.val)
#     newhead = newhead.next

# head = ListNode(1, None)
# newhead = sol.rotateRight(head, 2)
# while newhead != None:
#     print(newhead.val)
#     newhead = newhead.next

# head = ListNode(0, ListNode(1, ListNode(2, None)))
# newhead = sol.rotateRight(head, 4)
# while newhead != None:
#     print(newhead.val)
#     newhead = newhead.next

# newhead = sol.rotateRight(None, 0)
# while newhead != None:
#     print(newhead.val)
#     newhead = newhead.next
# head = ListNode(1, ListNode(2, None))
# newhead = sol.rotateRight(head, 0)
# while newhead != None:
#     print(newhead.val)
#     newhead = newhead.next