from typing import List

'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Notice that you should not modify the linked list.

Follow up:

Can you solve it using O(1) (i.e. constant) memory?

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

SOLUTION:
--------------
https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle

Distance travelled by slowPointer before meeting =x+y

Distance travelled by fastPointer before meeting =(x+y+z)+y=x+2y+z
x = distance of the list before the circular loop starts
y = first half of the loop before fast & slow pointers meets
z = distance of the other half of the loop through which fast pointer moves before meeting the slow pointer

Since fastPointer travels with double the speed of slowPointer, and time is constant for both when the reach the meeting point. 
So by using simple speed, time and distance relation (slowPointer traveled half the distance):

2∗dist(slowPointer)2(x+y)2x+2yx =  dist(fastPointer)=x+2y+z=x+2y+z=z

Hence by moving slowPointer to start of linked list and fast pointer start moving from the point where they initially meet, 
and making both slowPointer and fastPointer to move one node at a time, they both have same distance to cover.

They will reach at the point where the loop starts in the linked list.
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
        tmp.next = head.next
        print(tmp.val)
        return head.next
    

    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            if fast != None and fast.next != None:
                slow,fast = slow.next, fast.next.next
            else:
                return None
            
            if not fast:
                return None
            
            if fast == slow:
                #----now move the slow pointer to the head and move fast & slow pointers one step at a time and where both
                #----meet is the where the cycle has begun
                slow = head
                while True:
                    if slow == fast:
                        return slow
                    slow,fast = slow.next, fast.next
                    
            
sol = Solution()
listNode = sol.buildListNode([3,2,0,-4, 5, 6, 7, 8, 9])
print(sol.detectCycle(listNode).val)

listNode = sol.buildListNode([1])
ln = sol.detectCycle(listNode)
if ln:
    print(ln.val)
else:
    print("None")