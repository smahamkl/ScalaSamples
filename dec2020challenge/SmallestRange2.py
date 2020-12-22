from typing import List
import queue
'''
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 

Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]


Solution:
-----------
First sort a in ascending order. Then the best strategy is to flip the direction from +k to -k at certain point going from the smallest to the largest element.

We can go through the sorted array and enumerate all the possible changing point. At each adjacent numbers x and y, the numbers that will affect the range are cands = [a[0]+k, x+k, y-k, a[-1]-k]. We can simply compute max(cands) - min(cands), or, to be a little bit smarter, notice that a[0]+k < x+k and y-k < a[-1]-k and thus only a[0]+k or y-k could be the min and only x+k and a[-1]-k could be the max.

Don't forget the possibility of +k (or -k) for all the elements in a, which will give max(a) - min(a), or when a is sorted, just a[-1] - a[0].

Below we show pictorial explanations for two sample cases where 1) a=[1,4,8,10], k=3, flipping between 4 and 8; and 2) a=[2,2,4,7,8], k=5, flipping between 4 and 7.
'''
class Solution:
    def smallestRangeII(self, a: List[int], k: int) -> int:
        a.sort()
        ans = a[-1] - a[0]
        for x, y in zip(a, a[1:]):
            #print(x,y)
            ans = min(ans, max(a[-1]-k, x+k) - min(a[0]+k, y-k))
        return ans

sol = Solution()
print(sol.smallestRangeII([0,1,2,3,4,10], 2))
