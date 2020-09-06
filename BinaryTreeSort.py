from typing import List

'''
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]
Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]
Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]

Constraints:

Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
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

    def inorderTraversal(self, root: TreeNode, elements: List[int]) -> List[int]:
        #print(root.val)
        if root != None:
            if root.left != None:
                self.inorderTraversal(root.left, elements)
            
            if (root != None) & (root.val != None):
                elements.append(root.val)

            if root.right != None:
                self.inorderTraversal(root.right, elements)

        return elements
    


    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = sol.inorderTraversal(root1, [])
        list2 = sol.inorderTraversal(root2, [])
        res = []
        i = 0
        j = 0
        while (i < len(list1)) | (j < len(list2)):
            if i >= len(list1):
                res.append(list2[j])
                j+=1
            elif j >= len(list2):
                res.append(list1[i])
                i+=1
            elif list1[i] > list2[j]:
                res.append(list2[j])
                j+=1
            elif list2[j] > list1[i]:
                res.append(list1[i])
                i+=1
            else:
                res.append(list1[i])
                res.append(list2[j])
                i+=1
                j+=1

        return res




if __name__ == "__main__":
    sol = Solution()
    root1 = sol.buildTree([2, 1, 4], 0, None)
    root2 = sol.buildTree([1, 0, 3], 0, None)

    print(sol.getAllElements(root1, root2))

    root3 = sol.buildTree([0, -10, 10], 0, None)
    root4 = sol.buildTree([5,1,7,0,2], 0, None)

    print(sol.getAllElements(root3, root4))

    root3 = sol.buildTree([], 0, None)
    root4 = sol.buildTree([5,1,7,0,2], 0, None)

    print(sol.getAllElements(root3, root4))

    root3 = sol.buildTree([0,-10, 10], 0, None)
    root4 = sol.buildTree([], 0, None)

    print(sol.getAllElements(root3, root4))

    root3 = sol.buildTree([1, None, 8], 0, None)
    root4 = sol.buildTree([8, 1], 0, None)

    print(sol.getAllElements(root3, root4))


    #print(treeNode1.val)
    #print(treeNode1.right.val)
    #print(treeNode1.left.left.val)
    
    # print(sol.inorderTraversal(root1, []))
    # print(sol.inorderTraversal(root2, []))
    # print(sol.inorderTraversal(root3, []))
