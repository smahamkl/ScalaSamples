package dec2020challenge;
import java.util.LinkedList;
import java.util.Queue;
/*
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

*/
public class BSTIterator{

    Queue<TreeNode> nodeList = null;

    public BSTIterator(TreeNode root) {
        nodeList = new LinkedList<TreeNode>();
        inorder(root);
    }

    private void inorder(TreeNode root){
        if(root != null)
        {
            inorder(root.left);
            nodeList.add(root);
            inorder(root.right);
        }
    }
    
    public int next() {
        return nodeList.poll().val;
    }
    
    public boolean hasNext() {
        return !nodeList.isEmpty();
    }


    public static void main(String[] args)
    {
        TreeNode root = new TreeNode(7);
        root.left = new TreeNode(3);
        root.right = new TreeNode(15);
        root.right.left = new TreeNode(9);
        root.right.right = new TreeNode(20);

        BSTIterator bst = new BSTIterator(root);
        System.out.println(bst.next());    // return 3
        System.out.println(bst.next());    // return 7
        System.out.println(bst.hasNext()); // return True
        System.out.println(bst.next());    // return 9
        System.out.println(bst.hasNext()); // return True
        System.out.println(bst.next());    // return 15
        System.out.println(bst.hasNext()); // return True
        System.out.println(bst.next());    // return 20
        System.out.println(bst.hasNext()); // return False
    
    }
}