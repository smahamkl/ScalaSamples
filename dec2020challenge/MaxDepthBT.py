from typing import List

'''
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            root = TreeNode(nodes[curVal])
            root.left = self.buildTree(nodes, (2*curVal + 1), root.left)
            root.right = self.buildTree(nodes, (2*curVal + 2), root.right)
        return root

    def getdepth(self, root, depth)-> int:
        if not root:
            return depth
        
        return max(self.getdepth(root.left, depth+1), self.getdepth(root.right, depth+1))

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            return self.getdepth(root, 0)

sol = Solution()
#root = sol.buildTree([-8,3,0,-8,None,None,None,None,-1,None,None, None, None, None, None, None, None, None, 8], 0, None)
#root = sol.buildTree([3,9,20,None,None,15,7], 0, None)
root = sol.buildTree([3,9,20], 0, None)
print("root node:", root.val)
print("left node:", root.left.val)
print("right node:", root.right.val)
print(sol.maxDepth(root))