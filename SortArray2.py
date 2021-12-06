from typing import List
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/1605178/Py3Py-Simple-solution-using-for-loop-and-del-on-list-w-comments
'''
from math import inf

class Solution:
    
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)
        count = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            
            if count > 2:
                del nums[i]
            else:
                i += 1
        
        return len(nums)

sol = Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))
#print(sol.removeDuplicates([1,1,1,1,1,1,2]))
#print(sol.removeDuplicates([1,2]))
#print(sol.removeDuplicates([1,2,2,3]))
#print(sol.removeDuplicates([1,1,1,1,1,1,1,1]))
#print(sol.removeDuplicates([1,2,3,4,5]))
# print(sol.removeDuplicates([1]))
# print(sol.removeDuplicates([]))