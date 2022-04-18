import java.util.*;

public class MaximumProductSum {
    
    public static int maxProduct(int[] nums) {

        int min = 1;
        int max = 1;
        int res = Integer.MIN_VALUE;

        for(int num:nums)
            res=Math.max(res, num);

        for(int num: nums)
        {
            if(num == 0)
            {
                min = 1;
                max = 1;
                continue;
            }
            int tmp = min;
            min = Math.min(min * num, Math.min(num, max * num));
            max = Math.max(max * num, Math.max(num, tmp * num));

            res = Math.max(res, max);
        }

        return res;
        
    }

    public static void main(String[] args)
    {
        System.out.println(maxProduct(new int[]{-2,0,-1}));
    }

}
