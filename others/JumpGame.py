from typing import List
import sys
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        if nums[0] == 0 or(nums[0] > 0 and len(nums) == 1):
            return 0
        elif nums[0] >= len(nums) - 1:
            return 1
        
        tot_steps = 0
        max_idx = 0
        i = 0
        while i < len(nums):
            if i + nums[i] + 1 >= len(nums):
               return tot_steps + 1
            j = i + 1
            #between i and i'th index value(jump len) find the idx
            #corresponding to the next jumping length
            max_idx_val = nums[j]+i
            max_idx = j
            #print(j, (i + nums[i]), max_idx_val)
            while j <= (i + nums[i]):
                if (j + nums[j]) >= max_idx_val:
                   max_idx = j
                   max_idx_val = nums[j]+j
                j += 1
            tot_steps += 1
            i = max_idx
            #print("max index : " + str(max_idx) + " total steps: " + str(tot_steps) + " jump length:" + str(nums[i]))
            
sol = Solution()
print(sol.jump([2,3,1,1,4]))
print(sol.jump([2,1,1,1,4]))
print(sol.jump([3,2,2,1,4]))
print(sol.jump([1,2,3,4,5]))
print(sol.jump([5,9,3,2,1,0,2,3,3,1,0,0]))