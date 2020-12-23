from typing import List
import math
'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Solution:
---------
We DFS the tree and recursively check if each subtree is balanced. Because the definition of balancedness involves the depth of left and right subtrees, we also need to keep track of the depths for each subtree. 
So we maintain two values -- balancedness and depth. The base case is a null tree -- we see it as balanced and of depth 0 (True, 0). Otherwise, we go through its left and right subtree. 
It is only balanced if both of its left and right subtrees are balanced (lgood and rgood) and their depths are at most 1 apart (rdepth - 1 <= ldepth <= rdepth + 1). 
The depth of the current subtree is one deeper (itself) than the deeper one (max(ldepth, rdepth) + 1).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertLevelOrder(self, arr, root, i, n):
        # Base case for recursion  
        if i < n: 
            temp = TreeNode(arr[i])  
            root = temp    
            # insert left child  
            root.left = self.insertLevelOrder(arr, root.left, 
                                        (2 * i) + 1, n)
            # insert right child  
            root.right = self.insertLevelOrder(arr, root.right, 
                                        (2 * i) + 2, n)
        return root
    
    def dfs(self, t):
        if t is None:
            return 0
        ldepth = self.dfs(t.left)
        rdepth = self.dfs(t.right)
        return max(ldepth, rdepth) + 1 if ((rdepth - 1) <= ldepth <= (rdepth + 1)) else 200000

    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs(root) < 200000

sol = Solution()
arr = [1,2,None, 3,None, None, None, 4]
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
print(sol.isBalanced(root))
