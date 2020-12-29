from typing import List
import math

'''
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Solution:
---------
The crux of the problem is to put + and - signs on the numbers 1, 2, 3, ..., k so that the sum is target.

When target < 0 and we made a sum of target, we could switch the signs of all the numbers so that it equals Math.abs(target). Thus, the answer for target is the same as Math.abs(target), and so without loss of generality, we can consider only target > 0.

Now let's say k is the smallest number with S = 1 + 2 + ... + k >= target. If S == target, the answer is clearly k.

If S > target, we need to change some number signs. If delta = S - target is even, then we can always find a subset of {1, 2, ..., k} equal to delta / 2 and switch the signs, so the answer is k. (This depends on T = delta / 2 being at most S.) 
[The proof is simple: either T <= k and we choose it, or we choose k in our subset and try to solve the same instance of the problem for T -= k and the set {1, 2, ..., k-1}.]

Otherwise, if delta is odd, we can't do it, as every sign change from positive to negative changes the sum by an even number. So let's consider a candidate answer of k+1, which changes delta by k+1. 
If this is odd, then delta will be even and we can have an answer of k+1. Otherwise, delta will be odd, and we will have an answer of k+2.

For concrete examples of the above four cases, consider the following:

If target = 3, then k = 2, delta = 0 and the answer is k = 2.
If target = 4, then k = 3, delta = 2, delta is even and the answer is k = 3.
If target = 7, then k = 4, delta = 3, delta is odd and adding k+1 makes delta even. The answer is k+1 = 5.
If target = 5, then k = 3, delta = 1, delta is odd and adding k+1 keeps delta odd. The answer is k+2 = 5.
Algorithm

Subtract ++k from target until it goes non-positive. Then k will be as described, and target will be delta as described. We can output the four cases above: if delta is even then the answer is k, if delta is odd then the answer is k+1 or k+2 depending on the parity of k.
'''
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = math.ceil(math.sqrt(2*target)-1) # n = 1 gives O(sqrt(target)) solution
        while True:
            upper = n * (n+1) // 2
            #print("upper", upper)
            if upper >= target and (upper - target) % 2 == 0:
                break
            n += 1
        return n      

sol = Solution()
print(sol.reachNumber(23))