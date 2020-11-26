from typing import List
'''
Given a positive integer K, you need to find the length of the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N. If there is no such N, return -1.

Note: N may not fit in a 64-bit signed integer.

 

Example 1:

Input: K = 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: K = 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: K = 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Solution:
-----------
we can improve this algorithm with Pigeonhole Principle. Recall that the number of possible values of remainder (ranging from 0 to K-1) is limited, and in fact, 
the number is K. As a result, if the while-loop continues more than K times, and haven't stopped, then we can conclude that remainder repeats -- you can not have more than K different remainder.

Hence, if N exists, the while-loop must return length_N in the first K loops. Otherwise, it goes into an infinite loop.

Therefore, we can just run the while-loop K times, and return -1 if not stopped.
'''
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        str_k = str(K)
        last_digit = int(str_k[len(str_k)-1])
        if last_digit not in [1,3,7,9]:
            return -1
        else:
            num = 1
            l = 1
            while True:
                tmp = num % K
                if  tmp == 0:
                    return l
                elif num > 1 and l > K:
                    return -1
                else:
                    num  = num * 10 + 1
                    l += 1
    #----Solution from leetcode------------
    # def smallestRepunitDivByK(self, K: int) -> int:
    #     remainder = 0
    #     for length_N in range(1,K+1):
    #         remainder = (remainder*10+1) % K
    #         if remainder == 0:
    #             return length_N
    #     return -1



sol = Solution()
#print(sol.smallestRepunitDivByK(9))
print(sol.smallestRepunitDivByK(19927))
#print("mod", 111111111111111111111111111111111111111111%13777777777777777777)