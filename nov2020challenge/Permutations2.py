from typing import List

'''
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        p = [i for i in range(n+1)]
        permutations = set()
        permutations.add(tuple(nums))
        i = 1
        while i < n:
            p[i] -= 1
            j = (i % 2) * p[i]
            
            nums[i], nums[j] = nums[j], nums[i]
            permutations.add(tuple(nums))
            i = 1
            while p[i] == 0:
                p[i] = i
                i += 1
        return permutations

sol = Solution()
print(sol.permuteUnique([1,2,3]))