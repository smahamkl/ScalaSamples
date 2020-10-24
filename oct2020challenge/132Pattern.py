from typing import List

class Solution:

     def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) >= 3:
            n1 = nums[0]
            for i in range(1, len(nums)-1):
                n1 = min(n1, nums[i-1])
                if nums[i] > n1:
                    n2 = [num for num in nums[i+1:] if n1 < num < nums[i]]
                    #n2 = self.findMin(0, len(nums_sorted)-1, nums_sorted, n1, nums[i])
                    #print(n1, nums[i], n2)
                    if n2:
                        return True
        return False

        
sol = Solution()
print(sol.find132pattern([1,2,3,4]))
print(sol.find132pattern([3,1,4,2]))
print(sol.find132pattern([-1,3,2,0]))
print(sol.find132pattern([1,0,1,-4,-3]))
print(sol.find132pattern([3,5,0,3,4]))
print(sol.find132pattern([2,1,3,4]))