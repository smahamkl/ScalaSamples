from typing import Deque, List

'''
Leetcode 560

https://www.youtube.com/watch?v=fFVZt-6sgyo

'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1}
        res = 0
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)

            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
                   
          
        return res

sol = Solution()
print(sol.subarraySum([1,1,1], 2))
print(sol.subarraySum([1,2,3], 3))
print(sol.subarraySum([6,0,0], 6))
print(sol.subarraySum([0,5,-1,2], 6))
print(sol.subarraySum([-1,-1,1], 0))