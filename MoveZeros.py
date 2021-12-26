from typing import List

'''
Leetcode 283
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        f,s = 0, 0


        while f < len(nums):
            if nums[f] != 0:
                nums[s] = nums[f]
                s += 1
            f += 1
        
        while s < len(nums):
            nums[s] = 0
            s += 1




sol = Solution()
input = [0,0,0,0,1]

sol.moveZeroes(input)
print(input)