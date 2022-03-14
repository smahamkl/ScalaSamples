from typing import List
'''
LeetCode 441
Arranging Coins
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 1
        while r * (r+1) <= (n * 2):
            r += 1
        
        return r-1

sol = Solution()
print(sol.arrangeCoins(8))