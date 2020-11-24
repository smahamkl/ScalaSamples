from typing import List

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

    def rob(self, root: TreeNode) -> int:
        def helper(node):
            # return [rob this node, not rob this node]
            if not node:
                return (0, 0)
            left = helper(node.left)
            right = helper(node.right)
            # if we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]
            # else we could choose to either rob its children or not
            not_rob = max(left) + max(right)
            return [rob, not_rob]

        return max(helper(root))

        

sol = Solution()
#root = sol.buildTree([3,2,3,None,3,None,1],0, None)
#root = sol.buildTree([3,4,5,1,3,None,1],0, None)
#root = sol.buildTree([4,1,None,2,None,None, None, 3],0, None)
#print(root.val, root.left.val, root.right.val, root.left.right.val, root.right.right.val)
#root = sol.buildTree([1,2,3],0, None)
root = sol.buildTree([2,1,3,None,4],0, None)
print(sol.rob(root))