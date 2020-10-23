from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDepth(self, root:TreeNode, depth:int) -> int:
        if root.left == None and root.right == None:
            return depth
        elif root.right == None:
            return self.findDepth(root.left, depth+1)
        elif root.left == None:
            return self.findDepth(root.right, depth+1)
        else:
            return min(self.findDepth(root.left, depth+1), self.findDepth(root.right, depth+1))

    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return self.findDepth(root, 1)

    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            if nodes[curVal] != 0:
                root = TreeNode(nodes[curVal])
                root.left = self.buildTree(nodes, (curVal + 1), root.left)
                root.right = self.buildTree(nodes, (curVal + 2), root.right)
        return root

sol = Solution()
# root = sol.buildTree([3,9,20,None,None,15,7], 0, None)
# print(sol.minDepth(root))

# root = sol.buildTree([3,9,20], 0, None)
# print(sol.minDepth(root))

root = sol.buildTree([2,0,3,0,4,0,5,0,6], 0, None)
print(sol.minDepth(root))