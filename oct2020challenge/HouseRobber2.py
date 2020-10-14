from typing import List

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0
'''
class Solution:

    #---working function to first form combinations of numbers and then filter based on the sum
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], nums[1], nums[2])

        res = []
        res.append(nums[0])
        res.append(nums[1])
        res.append(nums[0]+nums[2])
        for i in range(3, len(nums)-1):
            res.append(max(nums[i]+res[i-2], nums[i]+res[i-3]))
        
        a = max(res)
        res = []
        res.append(nums[1])
        res.append(nums[2])
        res.append(nums[1]+nums[3])

        for i in range(4, len(nums)):
            res.append(max(nums[i]+res[i-4], nums[i]+res[i-3]))

        return max(a, max(res))
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2,3,2,2]))
    #print(sol.rob([200,3,140,20,10]))
    #print(sol.rob([1,3,1,3,100]))
    #print(sol.rob([0]))
    #print(sol.rob([2,7,9,3,1]))
    # print(sol.rob([226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,
    #   55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,
    #   120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]))
   