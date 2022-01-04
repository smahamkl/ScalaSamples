from typing import List
from collections import Counter
'''
Leetcode - 136
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum([x if y == 1 else 0 for x, y in Counter(nums).items()])

sol = Solution()
print(sol.singleNumber([2,2,1,1,3]))