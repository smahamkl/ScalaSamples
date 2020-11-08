from typing import List
'''
Given the root of a binary tree, return the sum of every tree node's tilt.

The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. 
If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if there the node does not have a right child.

Example:
--------
Input: root = [1,2,3]
Output: 1
Explanation: 
Tilt of node 2 : |0-0| = 0 (no children)
Tilt of node 3 : |0-0| = 0 (no children)
Tile of node 1 : |2-3| = 1 (left subtree is just left child, so sum is 2; right subtree is just right child, so sum is 3)
Sum of every tilt : 0 + 0 + 1 = 1

Example-2
----------
Input: root = [4,2,9,3,5,null,7]
Output: 15
Explanation: 
Tilt of node 3 : |0-0| = 0 (no children)
Tilt of node 5 : |0-0| = 0 (no children)
Tilt of node 7 : |0-0| = 0 (no children)
Tilt of node 2 : |3-5| = 2 (left subtree is just left child, so sum is 3; right subtree is just right child, so sum is 5)
Tilt of node 9 : |0-7| = 7 (no left child, so sum is 0; right subtree is just right child, so sum is 7)
Tilt of node 4 : |(3+5+2)-(9+7)| = |10-16| = 6 (left subtree values are 3, 5, and 2, which sums to 10; right subtree values are 9 and 7, which sums to 16)
Sum of every tilt : 0 + 0 + 0 + 2 + 7 + 6 = 15
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.tilt = []
    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            root = TreeNode(nodes[curVal])
            root.left = self.buildTree(nodes, (2*curVal + 1), root.left)
            root.right = self.buildTree(nodes, (2*curVal + 2), root.right)
        return root

    def computeSum(self, root: TreeNode) -> int:
        if root == None or root.val == None:
            return 0

        if root.left == None and root.right == None:
            return root.val
        
        leftsum = self.computeSum(root.left)
        rightsum = self.computeSum(root.right)

        #print("leftsum, rightsum:", leftsum, rightsum)

        self.tilt += [abs(leftsum - rightsum)]
        return leftsum + rightsum + root.val
    
    def findTilt(self, root: TreeNode) -> int:
        if root == None or root.val == None:
            return 0
        
        self.computeSum(root)

        return sum(self.tilt)

        
sol = Solution()
root = sol.buildTree([-8,3,0,-8,None,None,None,None,-1,None,None, None, None, None, None, None, None, None, 8], 0, None)
print("root node:", root.val)
print("left node:", root.left.val)
print("right node:", root.right.val)
print("left left node:", root.left.left.val)
print("left left right node:", root.left.left.right.val)
print("left left right left node:", root.left.left.right.right.val)
print(sol.findTilt(root))
print("tilt", sol.tilt)

