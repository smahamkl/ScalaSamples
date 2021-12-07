from typing import List

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
        #---the if part below is a critical optimization just to check to see if list contains any duplicates(t=0)
        if (t == 0) & (len(nums) == (k+1)):
            nums.sort()
            for i in range(1, len(nums)):
                if nums[i-1] == nums[i]:
                    return True
        else:
            for i, first in enumerate(nums):
                for j, second in enumerate(nums):
                    if (i != j) & (abs(second - first) <= t) & (abs(j-i) <= k):
                        return True
        return False

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
    print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
    print(sol.containsNearbyAlmostDuplicate([1,0,1,1], 1,2))
    print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2,3))
    print(sol.containsNearbyAlmostDuplicate([0], 0, 0))
    print(sol.containsNearbyAlmostDuplicate([2,2], 3, 0))
    print(sol.containsNearbyAlmostDuplicate([7,2,8], 2, 1))
    print(sol.containsNearbyAlmostDuplicate([3,6,0,4], 2, 2))