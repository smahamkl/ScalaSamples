/*
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
*/
package dec2020challenge;

public class CanPlaceFlowers {
    public void printArr(int[] arr)
    {
        for(int item:arr)
        {
            System.out.print(item + " ");
        }
        System.out.println();
    }
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        if(n == 0)
            return true;
        int i = 0;
        while(i < flowerbed.length)
        {
            if(flowerbed[i] == 1 || (i > 0 && flowerbed[i-1] == 1)){
                i += 1;
            }
            else if(((i+1) < flowerbed.length && flowerbed[i+1] == 0) || i == flowerbed.length-1)
            {
                flowerbed[i] = 2;
                n--;
                i+=2;
            }else{
                i+=1;
            }
            if(n == 0){
                printArr(flowerbed);
                return true;
            }
        }
     printArr(flowerbed);
     return false;   
    }

    public static void main(String[] args)
    {
        System.out.println(new CanPlaceFlowers().canPlaceFlowers(new int[]{}, 1));
    }
}
