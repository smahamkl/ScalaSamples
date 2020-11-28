from typing import List
from collections import Counter

class Solution:
    def checkifpartition(self, nums, i, sum, target) -> bool:
        if sum == target:
            return True
        elif i >= len(nums):
            return False
        else:
            return (self.checkifpartition(nums, i+1, nums[i]+sum, target) or self.checkifpartition(nums, i+1, sum, target))
    def canPartition(self, nums: List[int]) -> bool:
        arr_sum = sum(nums)
        if arr_sum % 2 == 1 or arr_sum == 0:
            return False
        arr_sum /= 2
        nums = sorted(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                arr_sum -= nums[i]
                nums.pop(i-1)
                nums.pop(i-1)
                continue
            i += 1
        print(nums, arr_sum)
                


        # nums = [x[0] for x in Counter(nums).items() if x[1] % 2 == 1]
        # if len(nums) == 0:
        #     return True
        
        # arr_sum = int(arr_sum / 2)
        # return self.checkifpartition(nums, 0, 0, arr_sum)

sol  = Solution()
#print(sol.canPartition([1,5,11,5]))
# print(sol.canPartition([1,2,3,5]))
print(sol.canPartition([4,3,1,6]))
#print(sol.canPartition([6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]))
# print(sol.canPartition([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
# 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
# 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
# 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
# 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,
# 100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]))