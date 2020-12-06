package dec2020challenge;

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {
    }

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
}

class BSTNextPointer2 {

    public Node connect(Node root) {
            
        Node rootPointer = root;

        //maintain 2 pointers
        Node childHead = null; //NEXT level's head pointer
        Node child = null; //NEXT level's traversal pointer

        while (root !=null ) 
        {
            //*******************************************
            //Step1: build child level's next pointers
            //*******************************************
            
            //if current item has left child
            if (root.left !=null ) 
            {    
                //mark child level's head if it is not done
                if(childHead ==null)
                {
                    //both child and childHead point to left node
                    childHead = root.left;
                    child = root.left;
                }
                else
                {
                    //attach child next to root's left node
                    child.next = root.left;   
                    
                    //move to child's next                     
                    child = child.next;
                }
            }

            if (root.right !=null) 
            {
                //mark child level's head if it is not done
                if(childHead ==null)
                {
                    //both child and childHead point to right node
                    childHead = root.right;
                    child = root.right;
                }
                else
                {
                    //attach child next to root's right node
                    child.next = root.right;   
                    
                    //move to child's next                     
                    child = child.next;
                }
            }
            
            //*******************************************
            //Step2: move to next item on SAME level
            //*******************************************
            root = root.next;

            //*******************************************
            //Step3: Once we reach END of current level
            //*******************************************
            if(root ==null)
            {
                //go to next LEVEL
                root = childHead;                    

                //reset child and childHead pointers 
                childHead = null;
                child = null;
            }
        }
        
        return rootPointer;
    }

    public static void main(String[] args) {
        BSTNextPointer2 bst = new BSTNextPointer2();
        // Node root = new Node(1);
        // root.left = new Node(2);
        // root.right = new Node(3);
        // root.left.left = new Node(4);
        // root.left.right = new Node(5);
        // root.left.left.left = new Node(7);
        // root.right.right = new Node(6);
        // root.right.right.right = new Node(8);
        Node root = new Node(2);
        root.left = new Node(1);
        root.right = new Node(3);
        root.right.left = new Node(9);
        root.right.right = new Node(1);
        root.right.right.left = new Node(8);
        root.right.right.right = new Node(8);
        root.left.left = new Node(0);
        root.left.right = new Node(7);
        root.left.left.left = new Node(2);
        root.left.right.left = new Node(1);
        root.left.right.right = new Node(0);
        root.left.right.right.left = new Node(7);
        Node newroot = bst.connect(root);
        // System.out.println(newroot.left.next.val);
        // System.out.println(newroot.left.left.next.val);
        // System.out.println(newroot.left.right.next.val);
        // System.out.println(newroot.left.left.left.next.val);
        System.out.println(newroot.left.right.right.next.val);
        //System.out.println(newroot.right.next.val);

    }

}