from typing import List
from collections import defaultdict
import math

'''
LeetCode 209
https://www.youtube.com/watch?v=HAA8mgxlov8
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minlen = math.inf
        tmpSum = 0

        if sum(nums) == target:
            return len(nums)

        for r in range(len(nums)):
           tmpSum += nums[r]
           while tmpSum >= target:
                minlen = min(minlen, (r - l + 1))
                tmpSum -= nums[l]
                l += 1
        if minlen == math.inf:
            return 0
        return minlen

sol = Solution()
print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
print(sol.minSubArrayLen(4, [1,4,4]))
print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(sol.minSubArrayLen(11, [1,2,3,4,5]))
print(sol.minSubArrayLen(15, [1,2,3,4,5]))
print(sol.minSubArrayLen(5, [2,3,1,1,1,1]))