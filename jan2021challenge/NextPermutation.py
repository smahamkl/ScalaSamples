from typing import List
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        def reverse(left):
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if not nums:
            return
        
        n = len(nums)
        first = n - 2
        
        while first >= 0 and nums[first] >= nums[first+1]:
            first -= 1
            
        if first < 0:
            reverse(0)
            return
            
        second = n - 1
        while second >= 0 and nums[second] <= nums[first]:
            second -= 1
        
        if first == second: #same index so no need to continue
            return
        
        nums[first], nums[second] = nums[second], nums[first]
        
        reverse(first + 1)

sol = Solution()
l = [1,1,5]
sol.nextPermutation(l)
print(l)