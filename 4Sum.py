from typing import List

'''
LeetCode 18
4 sum array problem
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if len(nums) < 4:
            return []

        res = set()
        nums.sort()
        nummap = {}
        arrlen = len(nums)
        for i, num in enumerate(nums):
            num1 = num
            j = i + 1
            while j < arrlen:
                num2 = nums[j]
                rem = target - (num1 + num2)
                k = j + 1
                nummap.clear()
                #print(num1, num2, rem)
                while k < arrlen:
                    if rem - nums[k] in nummap:
                        res.add((num1, num2, nums[k], rem - nums[k]))
                    
                    if nums[k] not in nummap:
                        nummap[nums[k]] = 1
                    
                    k+=1
                j+=1
        
        return list(res)

sol = Solution()
#print(sol.fourSum([1,0,-1,0,-2,2], 0))
print(sol.fourSum([2,2,2,2,2], 8))
