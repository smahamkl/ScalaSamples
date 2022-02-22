from typing import List
import functools

'''
LeetCode 179
Largest Number
https://www.youtube.com/c/NeetCode/videos
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if len(nums) == 1:
            return str(nums[0])

        def compare(x, y):
            return int(str(y)+str(x))-int(str(x)+str(y))

        sorted_nums = sorted(nums, key=functools.cmp_to_key(compare))
        
        res = ""

        if sorted_nums[0] == 0:
            res = "0"
        else:
            for x in sorted_nums:
                res += str(x)
        
        return res


sol = Solution()
print(sol.largestNumber([3,30,34,5,9]))
print(sol.largestNumber([10,2]))