from typing import List, Set

'''
Leetcode 90 (Subsets II) - Same as Power set

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        totalcomb = 2 ** len(nums)

        nums.sort()

        res = set()

        for i in range(totalcomb):
            tmp = []
            for j in range(len(nums)):
                if (i & (1 << j)) > 0:
                    tmp.append(nums[j])
            
            res.add(tuple(tmp))
        
        return list(res)

sol = Solution()
print(sol.subsetsWithDup([4,4,4,1,4]))