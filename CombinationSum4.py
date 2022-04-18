from typing import List
'''
LeetCode 377
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.
'''
class Solution:

    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        def dfs(target:int) -> int:

            if target == 0:
                return 1
            if target < 0:
                return 0
            
            if target in cache:
                return cache[target]
            
            res = 0

            for n in nums:
                tmp = dfs(target-n)
                cache[target-n] = tmp
                res += int(tmp)
            
            return res
        
        return dfs(target)
    
sol = Solution()
#print(sol.combinationSum4([3,4,5,6,7], 1))
print(sol.combinationSum4([4,2,1], 32))