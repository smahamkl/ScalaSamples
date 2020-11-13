from typing import List
'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), 
your function should populate each next pointer to point to its next right node, just like in Figure B. 
The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # def __init__(self):
    #     self.nummap = {}

    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            root = TreeNode(nodes[curVal])
            root.left = self.buildTree(nodes, (2*curVal + 1), root.left)
            root.right = self.buildTree(nodes, (2*curVal + 2), root.right)
        return root
    

    # def levelTraversal(self, root:'Node', level:int):
    #     if root != None:
    #         if root.left == root.right == None:
    #             return root,level
    #         else:
    #             left,level1 = self.levelTraversal(root.left, level+1)

    #             if level1 in self.nummap:
    #                 #print("level:", level1, "latest value in nummap:", self.nummap[level1][-1].val, "total list size:", len(self.nummap[level1]))
    #                 self.nummap[level1][-1].next = left
    #                 self.nummap[level1].pop()

    #             right,level1 = self.levelTraversal(root.right, level+1)

    #             if right and left:
    #                 left.next = right
    #                 if level1 not in self.nummap:
    #                     self.nummap[level1] = [right]
    #                 else:
    #                     self.nummap[level1] += [right]
                    
                
    #             return root, level


    # def connect1(self, root: 'Node') -> 'Node':
    #     if root == None:
    #         return root
    #     root,level = self.levelTraversal(root, 0)
    #     return root
    
    def connect(self, root: 'Node') -> 'Node':
        if not root or not root.left:
            return root
        root.left.next = root.right
        root.right.next = root.next.left if root.next else None
        self.connect(root.left)
        self.connect(root.right)
        return root

sol = Solution()
#root = sol.buildTree([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14], 0, None)
root = sol.buildTree([-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13],0,None)
#print(root.val,root.left.val, root.right.val,root.left.left.val, root.left.right.val,  root.right.left.val, root.right.right.val)
root = sol.connect(root)
print(root.right.left.right.next.val) # 12
print(root.left.left.right.next.val) #8
print(root.left.right.right.next.val) #10
print(root.right.right.left.next.val) #13
print(root.left.next.val)#1
print(root.left.right.next.val) #4
print(root.left.left.next.val) #3