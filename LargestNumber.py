from typing import List
from functools import cmp_to_key
'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''
from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if sum(nums) == 0:
            return "0"

        def compare(x, y):
            if int(str(x) + str(y)) > int(str(y) + str(x)):
                return -1
            else:
                return 1
        nums1 = sorted(nums, key=cmp_to_key(compare))
        #print(nums1)
        return "".join(str(x) for x in nums1)

sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))
print(sol.largestNumber([10,2]))
print(sol.largestNumber([121,12]))
print(sol.largestNumber([0, 0]))
print(sol.largestNumber([1]))