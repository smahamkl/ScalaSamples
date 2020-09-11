from typing import List
from collections import defaultdict


class Solution:
    def maxprod(self, nums:List[int], idx, prod) -> int:
        if idx < len(nums):
            if nums[idx] == 0:
                return max(prod, self.maxprod(nums, idx + 1, 0))
            else:
                if prod == 0:
                    return max(nums[idx], prod, self.maxprod(nums, idx + 1, nums[idx]))
                else: 
                    return max(nums[idx], prod, self.maxprod(nums, idx + 1, nums[idx]),
                    self.maxprod(nums, idx + 1, (prod * nums[idx])))
        else:
            return prod
        

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1], nums[0]*nums[1])
        
        return self.maxprod(nums, 1, nums[0])
          
      
if __name__ == "__main__":
    sol = Solution()
    #print(sol.maxProduct([2,3,-2,4]))
    print(sol.maxProduct([-2,0,-1]))
    #print(sol.maxProduct([0,2]))
    #print(sol.maxProduct([3,-1,4]))
    #print(sol.maxProduct([-2, 3, -4]))
    #print(sol.maxProduct([-2, 0]))
    #print(sol.maxProduct([2, -5, -2, -4, 3]))
    