from typing import List
'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have equal probability of returning.
solution.getRandom();
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def buildListNode(self, nodes:List[int]):
        tmp = head = ListNode(0)
        for item in nodes:
            tmp.next = ListNode(item)
            tmp = tmp.next
        return head.next

import random
class Solution:
    def __init__(self, head: ListNode):
        self.res = []
        while head:
            self.res.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        return random.choice(self.res)

ln = ListNode()
root = ln.buildListNode([1,2,3])
#print(root.next.next.next)
sol = Solution(root)
print(sol.getRandom())
