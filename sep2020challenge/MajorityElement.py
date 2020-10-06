
from typing import List

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) ==1:
            return nums
        numtimes = float(len(nums))/3.0
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] +=1
        res = list(filter(lambda k: num_map[k] > numtimes, num_map.keys()))
        print(num_map)
        return res

sol = Solution()
print(sol.majorityElement([1,1,1,3,3,2,2,2]))
print(sol.majorityElement([]))
print(sol.majorityElement([1,1, 2,3, 4]))
print(sol.majorityElement([0,0,0]))
print(sol.majorityElement([0,-1,2,-1]))
print(sol.majorityElement([-1,-1,2147483647]))