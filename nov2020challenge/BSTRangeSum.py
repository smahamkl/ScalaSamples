from typing import List
'''
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].

Example:
--------
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next: 'Node' = None):
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

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        cursum = 0
        if root.val != None:
            cursum = root.val if low <= root.val <= high else 0
        if root.left and root.val >= low:
            cursum += self.rangeSumBST(root.left, low, high)
        if root.right and root.val <= high:
            cursum += self.rangeSumBST(root.right, low, high)

        return cursum


sol = Solution()
root = sol.buildTree([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 0, None)
#root = sol.buildTree([10,5,15,3,7,None,18], 0, None)
print(sol.rangeSumBST(root, 6, 10))
#print(sol.rangeSumBST(root, 7, 15))
