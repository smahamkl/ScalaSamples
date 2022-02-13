from typing import List
from collections import Counter

'''
LeetCode 287
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return [i for i,v in Counter(nums).items() if v>=2][0]

sol = Solution()
# print(sol.findDuplicate([1,3,4,2,2]))
# print(sol.findDuplicate([3,1,3,4,2]))
# print(sol.findDuplicate([1,1]))
# print(sol.findDuplicate([1,1]))
print(sol.findDuplicate([2,2,2,2,2]))
print(sol.findDuplicate([3,3,3,3,3]))
print(sol.findDuplicate([4,4,4,4,4]))