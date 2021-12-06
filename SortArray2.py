from typing import List
'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/1605178/Py3Py-Simple-solution-using-for-loop-and-del-on-list-w-comments
'''
from math import inf

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Init
        prev = inf
        count = 0
        
        # from last to first element
        for i in range(len(nums)-1,-1,-1):
           
            # Reset Count
            if prev != nums[i]:
                count = 0
            
            # Increment count for current number
            count += 1
            prev = nums[i] # previous is current
            
            # If count if more than 2 delete
            if count > 2:
                del nums[i]
      
        return len(nums)

sol = Solution()
#print(sol.removeDuplicates([1,1,1,2,2,3]))
print(sol.removeDuplicates([1,1,1,1,1,1,2]))
# print(sol.removeDuplicates([1,2]))
# print(sol.removeDuplicates([1,2,2,3]))
# print(sol.removeDuplicates([1,1,1,1,1,1,1,1]))
# print(sol.removeDuplicates([1,2,3,4,5]))
# print(sol.removeDuplicates([1]))
# print(sol.removeDuplicates([]))