from collections import deque
from typing import List
import heapq

'''
LeetCode 220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such 
that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], idxdiff = 3, valdiff = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''
class Solution:

    # def minAbsValArr(self, arr: List[int]) -> int:
    #     minDiff = 9999999999
    #     for i in range(1, len(arr)):
    #         if minDiff > abs(arr[i] - arr[i-1]):
    #             minDiff = abs(arr[i] - arr[i-1])
    #     print("Least difference in array elements is: " + str(minDiff))
    #     return minDiff


    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False

        n = len(nums)
        num_arr = []
        # create a array of tuple where first index hold the element
        # and 2nd Index hold its index
        for i in range(n):
            temp = (nums[i],i)
            num_arr.append(temp)

        # sort the array
        num_arr = sorted(num_arr)

        # loop through array from 0th position
        for i in range(n):
            # loop array from i+1 postion
            for j in range(i+1,n):
                # check if difference of two elements is less than t or not
                # if not, no need to check further as array is already sorted
                # so further element's different will also not meet this criteria
                if abs(num_arr[i][0] - num_arr[j][0]) <= t :
                    # if above condition met, check if both index's position defference is less than k
                    if abs(num_arr[i][1] - num_arr[j][1]) <= k:
                        # if yes, return True
                        return True
                else:
                    break
        return False


        #---the if part below is a critical optimization just to check to see if list contains any duplicates(t=0)
        # if (t == 0) & (len(nums) == (k+1)):
        #     nums.sort()
        #     for i in range(1, len(nums)):
        #         if nums[i-1] == nums[i]:
        #             return True
        # else:
        #     for i, first in enumerate(nums):
        #         for j, second in enumerate(nums):
        #             if (i != j) & (abs(second - first) <= t) & (abs(j-i) <= k):
        #                 return True
        # return False

        # if k >= len(nums):
        #     tmp = nums
        #     tmp.sort()
        #     if(len(tmp) > 1):
        #         if self.minAbsValArr(tmp) <= t:
        #             return True
        # else:
        #     for i in range(0, len(nums), max(k, 1)):
        #         if((i+k) < len(nums)):
        #             tmp = nums[i:i+k+1]
        #             tmp.sort()
        #             print(tmp)
        #             if(len(tmp) > 1):
        #                 if self.minAbsValArr(tmp) <= t:
        #                     return True
        
        return False


if __name__ == "__main__":
    sol = Solution()
    # print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    # print(sol.containsNearbyAlmostDuplicate([1,0,1,1], 1,2))
    # print(sol.containsNearbyAlmostDuplicate([1,2,1,1], 1,0))
    # print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2,3))
    # print(sol.containsNearbyAlmostDuplicate([0], 0, 0))
    # print(sol.containsNearbyAlmostDuplicate([2,2], 3, 0))
    # print(sol.containsNearbyAlmostDuplicate([7,2,8], 2, 1))
    # print(sol.containsNearbyAlmostDuplicate([3,6,0,4], 2, 2))
    print(sol.containsNearbyAlmostDuplicate([1,14,23,45,56,2,3],1,10))