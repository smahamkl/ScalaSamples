from typing import List
from queue import PriorityQueue
'''
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def buildListNode(self, lists:List[List[int]])->List[ListNode]:
        tmp = []
        for list in lists:
            tmpN = headN = ListNode()
            for item in list:
                tmpN.val = item
                tmpN.next = ListNode()
                tmpN = tmpN.next
            tmpN = None
            tmp.append(headN)
        return tmp
    #-----this is by using a priority queue -----
    def mergeKLists(self, lists):
            """
            :type lists: List[ListNode]
            :rtype: ListNode
            """
            head = point = ListNode(0)
            q = PriorityQueue()
            for l in lists:
                if l:
                    q.put((l.val, l))
            while not q.empty():
                val, node = q.get()
                point.next = ListNode(val)
                point = point.next
                node = node.next
                if node:
                    q.put((node.val, node))
            return head.next
    #----working - brut force way -------
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     res = []
    #     for list in lists:
    #         while list != None and list.val != 0:
    #             res.append(list.val)
    #             list = list.next
    #     if len(res) == 0:
    #         return None
    #     res = sorted(res)
    #     tmpNode = resNode = ListNode()
    #     print(res)
    #     for i in range(len(res)):
    #         resNode.val = res[i]
    #         if i < (len(res)-1):
    #             resNode.next = ListNode()
    #             resNode = resNode.next
    #     return tmpNode
        
sol = Solution()
matrix = sol.buildListNode([[1,4,5],[1,3,4],[2,6]])
#matrix = sol.buildListNode([])
#print(matrix[0].next.next.val)
resNode:ListNode = sol.mergeKLists(matrix)
print(resNode.val)
