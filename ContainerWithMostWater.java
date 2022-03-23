import java.util.*;

public class ContainerWithMostWater {

    public int getArea(int h1, int h2, int w)
    {
        int h = Math.min(h1, h2);
        return Math.abs(h * w);
    }
    public int maxArea(int[] height) {

        int l = 0, r = height.length-1;
        int res = 0;

        while(l < r)
        {
            int area = getArea(height[l], height[r], r - l);
            res = Math.max(res, area);
            if(height[l] > height[r])
                r--;
            else
                l++;
        }

        return res;        
    }

    public static void main(String[] args)
    {
        ContainerWithMostWater obj = new ContainerWithMostWater();
        System.out.println(obj.maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
        System.out.println(obj.maxArea(new int[]{1,1}));
    }
    
}
