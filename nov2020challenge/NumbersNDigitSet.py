from typing import List
from itertools import permutations
import math
'''
Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.


Approach 1: Dynamic Programming + Counting
--------------------------------------------
Intuition

First, call a positive integer X valid if X <= N and X only consists of digits from D. Our goal is to find the number of valid integers.

Say N has K digits. If we write a valid number with k digits (k < K), then there are (D.length) power k possible numbers we could write, since all of them will definitely be less than N.

Now, say we are to write a valid K digit number from left to right. For example, N = 2345, K = 4, and D = '1', '2', ..., '9'. Let's consider what happens when we write the first digit.

* If the first digit we write is less than the first digit of N, then we could write any numbers after, for a total of (D.length) power K−1 valid numbers from this one-digit prefix. 
In our example, if we start with 1, we could write any of the numbers 1111 to 1999 from this prefix.

* If the first digit we write is the same, then we require that the next digit we write is equal to or lower than the next digit in N. In our example (with N = 2345), 
if we start with 2, the next digit we write must be 3 or less.

* We can't write a larger digit, because if we started with eg. 3, then even a number of 3000 is definitely larger than N.

Algorithm
---------------
Let dp[i] be the number of ways to write a valid number if N became N[i], N[i+1], .... For example, if N = 2345, then dp[0] would be the number of valid numbers at most 2345, 
dp[1] would be the ones at most 345, 
dp[2] would be the ones at most 45, and dp[3] would be the ones at most 5.

Then, by our reasoning above, dp[i] = (number of d in D with d < S[i]) * ((D.length) ** (K-i-1)), plus dp[i+1] if S[i] is in D.
'''
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        S = str(N)
        K = len(S)
        dp = [0] * K + [1]
        # dp[i] = total number of valid integers if N was "N[i:]"

        for i in range(K-1, -1, -1):
            # Compute dp[i]

            for d in D:
                if d < S[i]:
                    dp[i] += len(D) ** (K-i-1)
                elif d == S[i]:
                    dp[i] += dp[i+1]
                print("i", i, "digit from n:", S[i], "array number", d, "dp array value:", dp)
        tmp = [len(D) ** i for i in range(1, K)]
        print(tmp)
        return dp[0] + sum(tmp)
       

sol = Solution()
print(sol.atMostNGivenDigitSet(["1","3","5","7"], 570))
# print(sol.atMostNGivenDigitSet(["1","4","9"], 1000000000))
# print(sol.atMostNGivenDigitSet(["7","1"], 89))
# print(sol.atMostNGivenDigitSet(["7","1"], 1))
# print(sol.atMostNGivenDigitSet(["7","1"], 7))
# print(sol.atMostNGivenDigitSet(["7","1"], 777))
# print(sol.atMostNGivenDigitSet(["3", "4", "5", "6"], 644))
# print(sol.atMostNGivenDigitSet(["5", "6"], 19))
#print(sol.atMostNGivenDigitSet(["2","3","4","6","8"], 61))