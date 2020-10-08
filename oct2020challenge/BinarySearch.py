from typing import List
'''
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. 
If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
'''
class Solution:
    def findnum(self, nums:List[int], target:int, start:int, end:int)-> int:
        if (start == end) and (target == nums[start]):
            return start
        elif end > start:
            mid_idx = start + int((end - start)/2)
            #print("middle index:" + str(mid_idx))
            if nums[mid_idx] == target:
                #print(mid_idx)
                return mid_idx
            else:
                return max(self.findnum(nums, target, start, mid_idx-1),
                self.findnum(nums, target, mid_idx+1, end))
        else:
            return -1


    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and target == nums[0]:
            return 0
        elif len(nums) == 1 and target != nums[0]:
            return -1
        
        return self.findnum(nums, target, 0, len(nums)-1)

sol = Solution()
#print(sol.search([-1,0,3,5,9,12], 5))
print(sol.search([], -1))