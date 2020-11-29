from typing import List
from collections import deque

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1 or k == 1:
            return nums
        res = []
        q = deque()
        tmp = nums[0]
        for i in range(len(nums)):
            q.append(nums[i])
            if (i+1) >= k:
                if len(res) == 0 or (len(res) > 0 and tmp == res[-1]):
                    res += [max(q)]
                else:
                    res += [max(res[-1], nums[i])]
                tmp = q.popleft()

        return res

sol = Solution()
print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(sol.maxSlidingWindow([1], 1))
print(sol.maxSlidingWindow([1,-1], 1))
print(sol.maxSlidingWindow([9,11], 2))
print(sol.maxSlidingWindow([4,-2], 2))
print(sol.maxSlidingWindow([7,2,4], 2))
print(sol.maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5))