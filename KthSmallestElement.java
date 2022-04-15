import java.util.*;

/*
LeetCode 215
*/

public class KthSmallestElement {
    public static int kthSmallest(int[] arr, int l, int r, int k) 
    { 
        //Your code here
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(arr[l]);

        for(int i=l+1;i<=r;i++)
        {
            pq.offer(arr[i]);
        }

        while(k > 1 && pq.size() > 1)
        {
            pq.poll();
            k--;
        }

        return pq.peek();

    } 

    public static void main(String[] args)
    {
        KthSmallestElement obj = new KthSmallestElement();
        //System.out.println(obj.kthSmallest(new int[]{7,10,4,3,20,15}, 0, 5, 3));
        System.out.println(obj.kthSmallest(new int[]{7,10,4,20,15}, 0, 4, 4));
    }
}
