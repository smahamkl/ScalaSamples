from typing import List
from collections import defaultdict

'''
Approach:
Case 1: If the array has only positive elements ( 0 not included ) , product of all the elements will be returned as result.
Case 2: If the array has 0 in the array , the continuity will break , the subarray with max product will be returned.
In this question we are dealing with negative numbers as well.
At each element we need to maintain two values -> 
    1) maximum positive product till the ith position : max ( ( the current element ) nums[i] ,( product of current element and the largest product calculated till now ) max[i-1] * nums[i] , 
       (product of current element and the smallest product calculated till now ) min[i-1] * nums[i] )
    2) maximum negative product till ith position : min ( ( the current element ) nums[i] ,
        ( product of current element and the largest product calculated till now ) max[i-1] * nums[i] , (product of current element and the smallest product calculated till now ) min[i-1] * nums[i] )
'''
class Solution:
    # def maxprod(self, nums: List[int], idx, prod) -> int:
    #     if idx < len(nums):
    #         if nums[idx] == 0:
    #             return max(prod, self.maxprod(nums, idx + 1, 0))
    #         else:
    #             if prod == 0:
    #                 return max(nums[idx], prod, self.maxprod(nums, idx + 1, nums[idx]))
    #             else:
    #                 return max(nums[idx], prod, self.maxprod(nums, idx + 1, nums[idx]),
    #                            self.maxprod(nums, idx + 1, (prod * nums[idx])))
    #     else:
    #         return prod


    def maxProduct(self, nums: List[int]) -> int:
        m=[0]*len(nums)
        n=[0]*len(nums)
        m[0]=nums[0]
        n[0]=nums[0]
        for i in range(1,len(nums)):
            m[i]=max(nums[i],m[i-1]*nums[i],nums[i]*n[i-1])
            n[i]=min(nums[i],m[i-1]*nums[i],nums[i]*n[i-1])
        print(m)
        print(n)
        return max(m)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.maxProduct([2,3,-2,4]))
    # print(sol.maxProduct([-2,0,-1]))
    # print(sol.maxProduct([0,2]))
    # print(sol.maxProduct([3,-1,4]))
    # print(sol.maxProduct([-2, 3, -4]))
    # print(sol.maxProduct([-2, 0]))
    # print(sol.maxProduct([2, -5, -2, -4, 3]))
    # print(sol.maxProduct([-2]))
    print(sol.maxProduct([1, 0, -1, 2, 3, -5, -2]))
