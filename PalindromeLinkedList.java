import java.util.*;

public class PalindromeLinkedList {
    /* Structure of class Node is */
    static class Node
    {
        int data;
        Node next;
        
        Node(int d)
        {
            data = d;
            next = null;
        }
    }

    static boolean isPalindrome(Node head) 
    {
        //Your code here

        Stack<Node> st = new Stack<Node>();
        Node cur = head;
        while(cur != null)
        {
            st.push(cur);
            cur = cur.next;
        }

        while(head != null)
        {
            Node tmp = st.pop();
            //System.out.println(tmp.data + "," + head.data);
            if(head.data != tmp.data)
                return false;
            head = head.next;
        }

        return true;

    } 

    public static void main(String[] args)
    {
        Node n = new Node(1);
        n.next = new Node(2);
        n.next.next = new Node(2);
        n.next.next.next = new Node(1);

        System.out.println(isPalindrome(n));
    }
}
