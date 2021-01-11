from typing import List
'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m] = nums2[i]
            tmp = m - 1
            while tmp >= 0 and nums2[i] < nums1[tmp]:
                nums1[tmp], nums1[tmp+1] = nums1[tmp+1], nums1[tmp]
                tmp -= 1
            m += 1

sol = Solution()
nums1 = [2,0]
nums2 = [1]
sol.merge(nums1, 1, nums2, 1)
print(nums1)