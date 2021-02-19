/*
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n 
vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the 
most water.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
*/

class ContainerMostWater {

    public int getArea(int[] height, int l, int r)
    {
        return Math.min(height[l], height[r]) * (r - l);
    }

    public int maxArea(int[] height) {

        int l=0;
        int r = height.length-1;
        int maxArea = 0;

        while(l < r)
        {
            maxArea = Math.max(maxArea, getArea(height, l, r));
            if(height[l] < height[r])
                l++;
            else
                r--;
            
        }
        return maxArea;
    }

    public static void main(String[] args) {
        System.out.println(new ContainerMostWater().maxArea(new int[]{1,8,6,2,5,4,8,3,7}));
        System.out.println(new ContainerMostWater().maxArea(new int[]{4,3,2,1,4}));
        System.out.println(new ContainerMostWater().maxArea(new int[]{1,2,1}));
        System.out.println(new ContainerMostWater().maxArea(new int[]{1,1}));
        System.out.println(new ContainerMostWater().maxArea(new int[]{2,3,10,5,7,8,9}));
        System.out.println(new ContainerMostWater().maxArea(new int[]{2,3,4,5,18,17,6}));
    }
}