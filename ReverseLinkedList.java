import java.util.*;

public class ReverseLinkedList {
    static class ListNode {
             int val;
             ListNode next;
             ListNode() {}
             ListNode(int val) { this.val = val; }
             ListNode(int val, ListNode next) { this.val = val; this.next = next; }
         }
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curNode = head;

        while(curNode != null)
        {
            ListNode cache = curNode.next;
            curNode.next = prev;
            prev = curNode;
            curNode = cache;
        }
        return prev;
    }

    public static void main(String[] args)
    {
        ListNode n = new ListNode(1);
        n.next = new ListNode(2);
        n.next.next = new ListNode(3);
        n.next.next.next = new ListNode(4);

        ListNode res = reverseList(n);
        while(res != null){
            System.out.println(res.val);
            res = res.next;
        }
    }
}
