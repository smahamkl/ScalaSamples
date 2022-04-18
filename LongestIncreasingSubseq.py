from typing import List
'''
300. Longest Increasing Subsequence
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = {}
        res = 0

        for i in range(len(nums)-1, -1, -1):
            tmp = 1

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    tmp = max(1, 1+lis[j], tmp)
            
            lis[i] = tmp
            res = max(res, tmp)
        
        return res

sol = Solution()
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))
print(sol.lengthOfLIS( [0,1,0,3,2,3]))
print(sol.lengthOfLIS([7,7,7,7,7,7,7]))