import java.util.*;

public class RotatedSortedArray {
    public int findMin(int[] nums) {
        if(nums.length == 1)
            return nums[0];
        int l = 0, r = nums.length-1;
        int res = Integer.MAX_VALUE;
        
        while(l < r)
        {
            int m = (l + r) / 2;
            res = Math.min(res, Math.min(Math.min(nums[l], nums[r]), nums[m]));

            if(nums[l] > nums[r] && nums[m] > nums[r])
                l = m+1;
            else
                r = m-1;
        }

        return res;
    } 
    public static void main(String[] args)
    {
        RotatedSortedArray obj = new RotatedSortedArray();
        System.out.println(obj.findMin(new int[]{3,4,5,1,2}));
        System.out.println(obj.findMin(new int[]{4,5,6,7,0,1,2}));
        System.out.println(obj.findMin(new int[]{11,13,15,17}));
        System.out.println(obj.findMin(new int[]{1}));
        System.out.println(obj.findMin(new int[]{2,1}));
        System.out.println(obj.findMin(new int[]{5,1,2,3,4}));
    }
}
