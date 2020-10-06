from typing import List

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping 
you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''
class Solution:

    def maxSum(self, nums:List[int], idx, curSum:int) -> int:
        if idx < (len(nums)-1):
            return max(self.maxSum(nums, idx+2, (curSum + nums[idx])), self.maxSum(nums, idx+3, (curSum + nums[idx+1])))
        elif idx == (len(nums)-1): 
            return curSum + nums[idx]
        else:
            return curSum
        # cumSum = 0
        # for i in range(1, len(nums)):
            
        
        # return cumSum
    
    #---working function to first form combinations of numbers and then filter based on the sum
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        

        res = []
        res.append(nums[0])
        res.append(nums[1])
        res.append(nums[0] + nums[2])

        for i in range(3, len(nums)):
            res.append(max(res[i-3]+nums[i], res[i-2]+nums[i], res[i-1]))

        return max(res)
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2,1,1,2]))
    print(sol.rob([2,7,9,3,1]))
    print(sol.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,
      55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,
      120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))
   