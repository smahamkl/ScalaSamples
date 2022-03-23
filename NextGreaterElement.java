import java.util.*;

public class NextGreaterElement{

    public int[] nextGreaterElement(int[] nums1, int[] nums2)
    {
        int[] res = new int[nums1.length];
        Stack<Integer> stck = new Stack<Integer>();
        HashMap<Integer, Integer> lmap = new HashMap<Integer, Integer>();

        for(int i=0;i<nums1.length;i++)
         {
             res[i] = -1;
             lmap.put(nums1[i], i);
         }
        
        for(int i=0;i<nums2.length;i++)
         {
             int cur = nums2[i];
             while(!stck.empty() && cur > stck.peek())
             {
                 int topEle = stck.pop();
                 int idx = lmap.get(topEle);
                 res[idx] = cur;
             }
             if(lmap.containsKey(cur))
                stck.push(cur);
         }

         return res;
        
    }

    public static void main(String[] args)
    {
        NextGreaterElement obj = new NextGreaterElement();
        //int[] res = obj.nextGreaterElement(new int[]{4,1,2} ,new int[]{1,3,4,2});
        int[] res = obj.nextGreaterElement(new int[]{2,4} ,new int[]{1,2, 3,4});
        System.out.println(res.length);
        for(int ele : res){
            System.out.print(ele + ", ");
        }
    }
}