'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Solution:
---------
using binary search
'''
class Solution:
    def search(self, nums, target):
        if len(nums) <= 1: return nums[0] == target if nums else False
        m = len(nums) // 2
        l, r = nums[:m], nums[m:]
        if l[-1] > r[-1]: 
            return self.search(l, target) if l[0] <= target <= l[-1] else self.search(r, target)
        if l[-1] < r[-1]:
            return self.search(r, target) if r[0] <= target <= r[-1] else self.search(l, target)
        return l[0] == target or self.search(l, target) or self.search(r, target)

sol = Solution()
print(sol.search([2,5,6,0,0,1,2], 6))