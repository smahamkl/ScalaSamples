from typing import List

'''
You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is:

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.
'''
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, nodes: List[int], curIdx: int, root: TreeNode) -> TreeNode:
        if curIdx < len(nodes):
            root = TreeNode(nodes[curIdx])
            root.left = self.buildTree(nodes, ((2 * curIdx) + 1), root.left)
            root.right = self.buildTree(nodes, ((2 * curIdx) + 2), root.right)

        return root

    def traverseTree(self, root: TreeNode, newVal:int):
        #print(root.val)
        if root != None:
            if (root.left == None) and (newVal < root.val):
                root.left = TreeNode(newVal)
                return
            elif newVal < root.val:
                self.traverseTree(root.left, newVal)

            if (root.right == None) and (newVal > root.val):
                root.right = TreeNode(newVal)
                return
            elif newVal > root.val:
                self.traverseTree(root.right, newVal)

    def inorderTraversal(self, root: TreeNode, elements) -> List[int]:
        if root != None:
            if root.left != None:
                self.inorderTraversal(root.left, elements)
            
            elements.append(root.val)

            if root.right != None:
                self.inorderTraversal(root.right, elements)

        return elements
    
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            root = TreeNode(val)
        else:
            self.traverseTree(root, val)
        return root
        

sol = Solution()
# root = sol.buildTree([40,20,60,10,30,50,70], 0, None)
# print(sol.insertIntoBST(root, 25))

# root = sol.buildTree([4,2,7,1,3], 0, None)
# print(sol.insertIntoBST(root, 5))

root = sol.buildTree([], 0, None)
print(sol.inorderTraversal(sol.insertIntoBST(root, 5), []))