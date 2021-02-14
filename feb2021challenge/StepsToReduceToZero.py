from typing import List
'''
Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

 

Example 1:

Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
'''
class Solution:
    def numberOfSteps (self, num: int) -> int:
        def findSteps(num, steps)->int:
            if num == 2:
                return steps+2
            elif num == 1:
                return steps +1
            else:
                if num % 2 == 0:
                    return findSteps(num/2, steps+1)
                else:
                    return findSteps(num-1, steps+1)
        return findSteps(num, 0) if num > 0 else 0

sol = Solution()
print(sol.numberOfSteps(123))
print(sol.numberOfSteps(14))
print(sol.numberOfSteps(8))
print(sol.numberOfSteps(0))
print(sol.numberOfSteps(1))