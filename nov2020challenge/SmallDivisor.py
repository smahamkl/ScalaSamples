from typing import List
import math

'''
Problem:
-----------
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

 

Example 1:

Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 


********** Below is a java solution seems to be easier to understand **************
class Solution 
{
    /* The description of this problem pretty much describes what's to be done.  Perform the summation
     * on a series of divisors until the correct one is found.  As hint #2 suggest a binary search is
     * used to reduce the time in selecting divisors to try.
     *
     * A couple things to note.  The greatest value of the summation occurs when the divisor is 1.  In
     * this case each value in the nums array returns itself and it's a true summation.  The lowest 
     * value of the summation occurs when the divisor is equal to the largest value in the nums array. 
     * When using this value every number in the nums array divides down to 1 and the sumation will 
     * equal nums.length. This is also true for values greater than the largest value, but checking 
     * these values would be redundant.  So you can set the initial range of divisors to be tested as 
     * 1..max value in nums.
     */
    
    public int smallestDivisor(int[] nums, int threshold) 
    {
        int     m = 0;
        int     l = 1;
        int     r = max( nums );

        while( l <= r )
        {
            if( sum( nums, threshold, m = (l + r) / 2 ) )
            {
                l = m + 1;
            }
            else
            {
                r = m - 1;
            }
        }
        
        return l;
    }
    
    // --- Utility method to find max value in an array ---
    
    private static int max( int[] nums )
    {
        int     max = 0;
        
        for( int n : nums )
        {
            max = Math.max( max, n );
        }
        
        return max;
    }

    // --- Utility method to perform sum and compare against threshold (i.e. t) ---
    
    private static boolean sum( int[] nums, int t, int d )
    {
        int     sum = 0;
        
        for( int n : nums )
        {
            sum += (n - 1) / d + 1;
        }
        
        return sum > t;
    }
}
'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo = (sum(nums) + threshold - 1) // threshold
        hi = lo * 2
        tot = sum((x + hi - 1) // hi for x in nums)
        while tot > threshold:
            lo = hi
            hi *= 2
            tot = sum((x + hi - 1) // hi for x in nums)
            
        while lo < hi:
            mid = (lo + hi) // 2
            tot = sum((x + mid - 1) // mid for x in nums)
            if tot <= threshold:
                hi = mid
            else:
                lo = mid + 1
            
        return lo

sol = Solution()
print(sol.smallestDivisor([1,2,5,9], 6))
