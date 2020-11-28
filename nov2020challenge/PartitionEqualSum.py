from typing import List
from collections import Counter
'''
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

Solution:
----------
Using DP and memozation technique to store the intermedia states by index and the sum
'''
class Solution:
    def checkifpartition(self, nums, i, sum, target, partmap) -> bool:
        if sum == target:
            return True
        elif i >= len(nums):
            return False
        elif partmap.get((i, sum), None) != None:
            return partmap[(i, sum)]
        else:
            val = (self.checkifpartition(nums, i+1, nums[i]+sum, target, partmap) or self.checkifpartition(nums, i+1, sum, target, partmap))
            partmap[(i, sum)] =val
            return val

    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum % 2 == 1 or arr_sum == 0:
            return False
        arr_sum /= 2
        return self.checkifpartition(nums, 0, 0, arr_sum, {})

sol  = Solution()
print(sol.canPartition([1,5,11,5]))
print(sol.canPartition([1,2,3,5]))
print(sol.canPartition([4,3,1,6]))
print(sol.canPartition([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]))
print(sol.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))