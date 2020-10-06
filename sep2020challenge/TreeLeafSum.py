from typing import List

'''
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  
For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
'''
class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, nodes: List[int], curVal: int, root: TreeNode) -> TreeNode:
        if curVal < len(nodes):
            root = TreeNode(nodes[curVal])
            root.left = self.buildTree(nodes, ((2 * curVal) + 1), root.left)
            root.right = self.buildTree(nodes, ((2 * curVal) + 2), root.right)

        return root

    def pathValue(self, path: str) -> int:
        if path is None:
            return 0
        res = 0
        path = path[::-1]
        #print("path: " + path)
        for i in range(len(path)):
	        digit = path[i]
	        if digit == '1':
		        res += pow(2, i)
            
        return res
    
    def treeTraversal(self, root: TreeNode, res:str, pathVal:List[int]) -> int:
        #print(root.val)

        if root != None:
            
            if root.left != None:
                self.treeTraversal(root.left, res + str(root.val), pathVal)

            if root.right != None:
                self.treeTraversal(root.right, res + str(root.val), pathVal)
                   
            if (root.left is None) & (root.right is None):
                res += str(root.val)
                #print("value of string on left res: " + str(self.pathValue(res)))
                pathVal.append(self.pathValue(res))
              
        return sum(pathVal)
    

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return self.treeTraversal(root, "", [0])


if __name__ == "__main__":
    sol = Solution()
    root1 = sol.buildTree([1,1], 0, None)
    #root2 = sol.buildTree([1, 0, 3], 0, None)

    print(sol.sumRootToLeaf(root1))

    #print(sol.pathValue("1111"))
