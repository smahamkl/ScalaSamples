from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        maxp = -1
        minv = prices[0]
        for i in range(1, len(prices)):
            minv = min(minv, prices[i])
            maxp = max(maxp, (prices[i] - minv), (prices[i] - prices[i-1]))
        return maxp

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit( [7,6,4,3,1]))
print(sol.maxProfit( [2,1]))