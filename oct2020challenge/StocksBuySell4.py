from typing import List
from itertools import combinations

class Solution:
    '''
    profit[t][i] will be maximum of –
    profit[t][i-1] which represents not doing any transaction on the ith day.
    Maximum profit gained by selling on ith day. In order to sell shares on ith day, 
    we need to purchase it on any one of [0, i – 1] days. If we buy shares on jth day and sell it on ith day, 
    max profit will be price[i] – price[j] + profit[t-1][j] where j varies from 0 to i-1. 
    Here profit[t-1][j] is best we could have done with one less transaction till jth day.
    '''
    #---not an optimized solution but a dynamic programming one---
    def maxProfit_dp_not_optimized(self, prices:[], k):
        if len(prices) <= 1:
            return 0
        n = len(prices)
        profits = [[0 for x in range(k+1)] for x in range(n)]
        for i in range(1,n):
            for j in range(1,k+1):
                max_profit_so_far = 0
                for l in range(i):
                    max_profit_so_far = max(max_profit_so_far, prices[i]-prices[l] + profits[l][j-1])
                profits[i][j] = max(profits[i-1][j],max_profit_so_far)
        return profits[n-1][k]
    def maxProfit(self, prices:[], k):
        n = len(prices)
        if k > n:
            k = n//2
        if n <= 1:
            return 0
        profit = [[0 for i in range(n + 1)]  
                    for j in range(k + 1)]  
    
        # Fill the table in bottom-up fashion  
        for i in range(1, k + 1):  
            prevDiff = float('-inf') 
            
            for j in range(1, n):  
                prevDiff = max(prevDiff, 
                            profit[i - 1][j - 1] - 
                            prices[j - 1])  
                profit[i][j] = max(profit[i][j - 1],  
                                prices[j] + prevDiff)  
    
        return profit[k][n - 1]
sol = Solution()
# print(sol.maxProfit(2, [3,2,6,5,0,3]))
# print(sol.maxProfit(2, [1,2,3,4,5]))
#print(sol.maxProfit([2,4,1],2))
#print(sol.maxProfit([1,4,3,0,5],1))
print(sol.maxProfit([6,1,3,2,4,7], 2))