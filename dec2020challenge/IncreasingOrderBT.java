/*
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
*/
package dec2020challenge;

class IncreasingOrderBT {

    // Definition for a binary tree node.
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    private TreeNode pointer;

    public void inorder(TreeNode root) {

        if (root == null)
            return;

        inorder(root.left);
        root.left = null;
        pointer.right = root;
        pointer = pointer.right;
        inorder(root.right);

    }

    public TreeNode increasingBST(TreeNode root) {
        if (root == null) {
            return root;
        }
        TreeNode dummy = new TreeNode(0);
        pointer = dummy;
        inorder(root);
        return dummy.right;
    }

    // [5,3,6,2,4,null,8,1,null,null,null,7,9]
    public static void main(String[] args) {
        IncreasingOrderBT bst = new IncreasingOrderBT();
        TreeNode root = bst.new TreeNode(5);
        root.left = bst.new TreeNode(3);
        root.right = bst.new TreeNode(6);
        // root.left.left = bst.new TreeNode(2);
        // root.left.right = bst.new TreeNode(4);
        // root.right.right = bst.new TreeNode(8);
        // root.left.left.left = bst.new TreeNode(1);
        // root.right.right.left = bst.new TreeNode(7);
        // root.right.right.right = bst.new TreeNode(9);
        TreeNode newroot = bst.increasingBST(root);
        System.out.println(newroot.val);
    }

}