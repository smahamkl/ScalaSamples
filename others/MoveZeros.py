from typing import List
'''
#Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of 
#the non-zero elements.
'''
class Solution:
    def solution(self, nums:List[int]):
        for i in nums:
            if 0 in nums:
                nums.remove(0)
                nums.append(0)
        return nums
        
sol = Solution()
print(sol.solution([0,1,0,3,12]))