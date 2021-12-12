from typing import List
'''
LeetCode 41
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        num_map={}
        max_val = 0
        for i in range(len(nums)):
            if max_val < nums[i]:
                max_val = nums[i]

            if (nums[i] not in num_map) and (nums[i] > 0):
                num_map[nums[i]]=1
        
        print(num_map)
        for i in range(1, max(max_val+2, 2)):
            if i not in num_map:
                return i



sol = Solution()
#print(sol.firstMissingPositive([7,8,9,11,12]))
#print(sol.firstMissingPositive([3,4,-1,1]))
#print(sol.firstMissingPositive([1,2,0]))
print(sol.firstMissingPositive([2147483647]))