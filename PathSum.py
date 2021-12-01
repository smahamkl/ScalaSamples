from typing import Optional


class TreeNode:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None
    
'''
Leetcode 112 - PathSum problem
'''

class Solution:
    def targetSum(self, root: Optional[TreeNode], target:int, cursum:int)->bool:
        if root:
            if (root.left == None and root.right == None) and (cursum + root.val == target):
                return True
            
            return self.check_target_sum(root.left, target, cursum + root.val) or self.check_target_sum(root.right, target, cursum + root.val)

        
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum:int)->bool:
        return self.targetSum(root, targetSum, 0)


if __name__ == "__main__":
    sol = Solution()
    # root = Node1(5)
    # root.left = Node1(4)
    # root.right = Node1(8)
    # root.left.left = Node1(11)
    # root.left.left.left = Node1(7)
    # root.left.left.right = Node1(2)
    # root.right.left = Node1(13)
    # root.right.right = Node1(4)
    # root.right.right.right = Node1(1)
    #-----------------------------------
    # root = Node1(1)
    # root.left = Node1(2)
    # root.right = Node1(3)
    root = None
    print(sol.hasPathSum(root, 0))