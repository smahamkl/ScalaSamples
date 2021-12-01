from typing import List
from collections import deque
'''
Leetcode 977 Squares of an sorted array
using two pointers
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        ans = deque()

        while left <= right:
            lsq, rsq = nums[left] ** 2, nums[right] ** 2

            if lsq > rsq:
                ans.insert(0, lsq)
                left += 1
            else:
                ans.insert(0, rsq)
                right -= 1
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    res = sol.sortedSquares([-4,-1,0,3,10])
    for i in res:
        print(i, end=",")