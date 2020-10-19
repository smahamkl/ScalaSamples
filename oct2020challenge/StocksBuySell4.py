from typing import List
from itertools import combinations
'''
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
'''
class Solution:
    '''
    profit[t][i] will be maximum of –
    profit[t][i-1] which represents not doing any transaction on the ith day.
    Maximum profit gained by selling on ith day. In order to sell shares on ith day, 
    we need to purchase it on any one of [0, i – 1] days. If we buy shares on jth day and sell it on ith day, 
    max profit will be price[i] – price[j] + profit[t-1][j] where j varies from 0 to i-1. 
    Here profit[t-1][j] is best we could have done with one less transaction till jth day.
    '''
    #---not an optimized solution but uses dynamic programming method---
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
    #----optimizded DP method---------------
    '''
    There are two cases to consider here, one where the number of transactions allowed excedes the
    length of the prices array divided in half, and the case where the number allowed is less than
    half the length of the prices array.  When the number of transactions excedes half the the 
    length of prices this is the simple case.  There are enough transations to allow the capture of
    every price increase and profit can be found by iterating over the array and adding any 
    increase in price into the return value.  For the case where the number of transactions is less
    than half of the length of prices a basic dynamic-programming algorythm can be applied.

    Implementation of optimized DP method:
    ---------------------------------------
    Optimized Solution:
    The previous method - maxProfit_dp_not_optimized has time complexity of O(k.n2). It can be reduced if we are able to calculate the maximum profit gained by selling shares on the ith day in constant time.

    profit[t][i] = max(profit [t][i-1], max(price[i] – price[j] + profit[t-1][j]))
                                for all j in range [0, i-1]

    If we carefully notice,
    max(price[i] – price[j] + profit[t-1][j])
    for all j in range [0, i-1]

    can be rewritten as,
    = price[i] + max(profit[t-1][j] – price[j])
    for all j in range [0, i-1]
    = price[i] + max(prevDiff, profit[t-1][i-1] – price[i-1])
    where prevDiff is max(profit[t-1][j] – price[j])
    for all j in range [0, i-2]

    So, if we have already calculated max(profit[t-1][j] – price[j]) for all j in range [0, i-2], we can calculate it for j = i – 1 in constant time. 
    In other words, we don’t have to look back in the range [0, i-1] anymore to find out best day to buy. We can determine that in constant time using below revised relation.

    profit[t][i] = max(profit[t][i-1], price[i] + max(prevDiff, profit [t-1][i-1] – price[i-1])
    where prevDiff is max(profit[t-1][j] – price[j]) for all j in range [0, i-2]
    '''
    
    def maxProfit(self, k, prices:[]):
        n = len(prices)
        if n <= 1:
            return 0

        if k > n:
            return self.processSimple( prices )

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
    def processSimple(self, prices:[])->int:
        n   = len(prices)
        ret = 0
            
        for i in range(1,n):
            ret += max( 0, prices[ i ] - prices[ i - 1 ] )
    
        return ret
sol = Solution()
# print(sol.maxProfit(2, [3,2,6,5,0,3]))
# print(sol.maxProfit(2, [1,2,3,4,5]))
print(sol.maxProfit(2, [2,4,1]))
#print(sol.maxProfit([1,4,3,0,5],1))
#print(sol.maxProfit([6,1,3,2,4,7], 15))