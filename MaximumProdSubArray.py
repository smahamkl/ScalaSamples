from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            tmp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(tmp * n, curMin*n, n)
            res = max(res, curMax)
        
        return res

sol = Solution()
print(sol.maxProduct([2,3,-2,4]))
print(sol.maxProduct([-2,0,-1]))
print(sol.maxProduct([-3,-1,-1]))