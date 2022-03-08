from typing import List, Optional
'''
Invert Binary Tree
LeetCode 226
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def mirrorTree(root:TreeNode)->TreeNode:
            if root:
                mirrorTree(root.left)
                mirrorTree(root.right)

                root.left, root.right = root.right, root.left
                return root
            return None
        
        return mirrorTree(root)

sol = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)
root = sol.invertTree(root)
print(root.left.val, root.right.val, root.left.left.val, root.left.right.val)
