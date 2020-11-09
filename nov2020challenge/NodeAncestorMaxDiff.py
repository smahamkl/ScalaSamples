from typing import List
'''
Given the root of a binary tree, find the maximum value V for which there exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.maxdiff = 0

    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            if nodes[curVal] != None:
                root = TreeNode(nodes[curVal])
                root.left = self.buildTree(nodes, (2*curVal + 1), root.left)
                root.right = self.buildTree(nodes, (2*curVal + 2), root.right)
        return root
    
    def findMaxDiff(self, root:TreeNode) -> (int,int):
        if root:
            if root.left == None and root.right == None:
                return root.val,root.val
            
            if root.left and root.right:
                lmin, lmax = self.findMaxDiff(root.left)
                rmin, rmax = self.findMaxDiff(root.right)
                self.maxdiff = max(self.maxdiff, abs(root.val - lmin), abs(root.val - lmax), abs(root.val - rmin), abs(root.val - rmax))
                return min(root.val,lmin, rmin), max(root.val, lmax, rmax)
            elif root.right:
                rmin, rmax = self.findMaxDiff(root.right)
                self.maxdiff = max(self.maxdiff, abs(root.val - rmin), abs(root.val - rmax))
                return min(root.val,rmin), max(root.val, rmax)
            else:
                lmin, lmax = self.findMaxDiff(root.left)
                self.maxdiff = max(self.maxdiff, abs(root.val - lmin), abs(root.val - lmax))
                return min(root.val,lmin), max(root.val, lmax)
    
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
                return 0
        
        self.findMaxDiff(root)
        return self.maxdiff

        
sol = Solution()
root = sol.buildTree([8,3,10,1,6,None,14,None,None,4,7,None,None,13], 0, None)
#root = sol.buildTree([1,None,2,None,None,None,0,None,None,None,None,None,None,3], 0, None)
#root = sol.buildTree([8], 0, None)
print("root node:", root.val)
# print("left node:", root.left.val)
# print("right node:", root.right.val)
# print("right node:", root.right.right.val)
# print("right node:", root.right.right.left.val)
print(sol.maxAncestorDiff(root))