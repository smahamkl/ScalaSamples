from typing import List
'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the 
integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not 
fit in 32-bit integer, return -1.

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1

Solution:
---------
scan the number from the right side, compare each digit with the previous digit to look for a digit pair 
where the left digit is less than right side digit. if there is such pair exists, start from the right side 
digit of the number pair and look for a number inside the rest of the array that is just greater than the 
left side digit. Interchange that number with the left side digit Starting from the index of the right 
side of the digit pair, sort the numbers of the right side of the array and concatenate it with the left 
part of the array to get the resultant number
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nstr = list(str(n))
        startch = -1
        for i in range(len(nstr)-2, -1, -1):
            if(nstr[i] < nstr[i+1]):
                startch = i
                break
        if startch == -1:
            return startch
        
        A = min([(x,i) for i,x in enumerate(nstr[startch:]) if x > nstr[startch]])

        nstr[startch], nstr[startch+A[1]] = nstr[startch+A[1]], nstr[startch]

        res = int(''.join(nstr[:startch+1] + sorted(nstr[startch+1:])))

        return res if res <= (2 ** 31 -1) else -1

sol = Solution()
print(sol.nextGreaterElement(199999999))
#print(sol.nextGreaterElement(230241))
#print(sol.nextGreaterElement(12443322)) #13222344