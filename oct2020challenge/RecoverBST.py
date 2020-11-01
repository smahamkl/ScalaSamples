from typing import List
'''

SOLUTION:
---------
The inorder traversal of a BST produces a sorted array. So a simple method is to store inorder traversal of the input tree in an auxiliary array. Sort the auxiliary array. 
Finally, insert the auxiliary array elements back to the BST, keeping the structure of the BST same. The time complexity of this method is O(nLogn) and the auxiliary space needed is O(n).
We can solve this in O(n) time and with a single traversal of the given BST. Since inorder traversal of BST is always a sorted array, the problem can be reduced to a problem where two 
elements of a sorted array are swapped. There are two cases that we need to handle:

1. The swapped nodes are not adjacent in the inorder traversal of the BST. 

 For example, Nodes 5 and 25 are swapped in {3 5 7 8 10 15 20 25}. 
 The inorder traversal of the given tree is 3 25 7 8 10 15 20 5 
If we observe carefully, during inorder traversal, we find node 7 is smaller than the previous visited node 25. Here save the context of node 25 (previous node). Again, we find that node 5 is 
smaller than the previous node 20. This time, we save the context of node 5 (the current node ). Finally, swap the two node’s values

2. The swapped nodes are adjacent in the inorder traversal of BST.

  For example, Nodes 7 and 8 are swapped in {3 5 7 8 10 15 20 25}. 
  The inorder traversal of the given tree is 3 5 8 7 10 15 20 25 
Unlike case #1, here only one point exists where a node value is smaller than the previous node value. e.g. node 7 is smaller than node 8. 
How to Solve? We will maintain three-pointers, first, middle, and last. When we find the first point where the current node value is smaller than the previous node value, we update the first 
with the previous node & the middle with the current node. When we find the second point where the current node value is smaller than the previous node value, we update the last with the current node. 
In the case of #2, we will never find the second point. So, the last pointer will not be updated. After processing, if the last node value is null, then two swapped nodes of BST are adjacent. 
Following is the implementation of the given code.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, nums:List[int], head:TreeNode, idx:int)->TreeNode:
        if idx < len(nums):
            head = TreeNode(nums[idx])
            head.left = self.buildTree(nums, head.left, 2*idx+1)
            head.right = self.buildTree(nums, head.left, 2*idx+2)
            return head

    
    # Utility function to track the nodes
    # that we have to swap
    def correctBstUtil(self, root, first, middle,
                    last, prev):
                            
        if(root and (root.val != None)):
            
            # Recur for the left sub tree
            self.correctBstUtil(root.left, first,
                        middle, last, prev)
                            
            # If this is the first violation, mark these 
            # two nodes as 'first and 'middle'
            if(prev[0] and root.val < prev[0].val):
                if(not first[0]):
                    first[0] = prev[0]
                    middle[0] = root
                else:
                    
                    # If this is the second violation,
                    # mark this node as last
                    last[0] = root
                    
            prev[0] = root
            
            # Recur for the right subtree
            self.correctBstUtil(root.right, first, 
                        middle, last, prev)
        
    # A function to fix a given BST where 
    # two nodes are swapped. This function
    # uses correctBSTUtil() to find out two
    # nodes and swaps the nodes to fix the BST 
    def correctBst(self, root):
        
        # Followed four lines just for forming
        # an array with only index 0 filled 
        # with None and we will update it accordingly.
        # we made it null so that we can fill 
        # node data in them.
        first = [None]
        middle = [None]
        last = [None]
        prev = [None]
        
        # Setting arrays (having zero index only) 
        # for capturing the requird node
        self.correctBstUtil(root, first, middle,
                    last, prev)
    
        # Fixing the two nodes
        if(first[0] and last[0]):
            
            # Swapping for first and last key values
            first[0].val, last[0].val = (last[0].val, 
                                        first[0].val)
    
        elif(first[0] and middle[0]):
        
            # Swapping for first and middle key values
            first[0].val, middle[0].val = (middle[0].val,
                                            first[0].val)
        elif root and root.left:
            if root.left.val > root.val:
                root.val, root.left.val = root.left.val, root.val
        elif root and root.right:
            if root.right.val < root.val:
                root.val, root.right.val = root.right.val, root.val


    def recoverTree(self, root: TreeNode) -> None:
        #----inorder traversal in a binary tree would give elements in ascending order
        if root:
            self.correctBst(root)
    def PrintInorder(self, root):
        if(root):
            self.PrintInorder(root.left)
            print(root.val, end = " ")
            self.PrintInorder(root.right)
            
        else:
            return
        

sol = Solution()
#root = sol.buildTree([3,1,4,None,None,2], None, 0)
#root = sol.buildTree([27,14,35,10,19,31,42], None, 0)
#print(root.right.left.val)
root = sol.buildTree([10,5,15,0,8,13,20,2,-5,6,9,12,14,18,25], None, 0)
sol.PrintInorder(root)
print("")
#sol.PrintInorder(root)
sol.recoverTree(root)
sol.PrintInorder(root)
print("")