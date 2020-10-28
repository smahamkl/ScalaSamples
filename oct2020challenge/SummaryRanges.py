from typing import List
'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
'''
class Solution:
    def get_range(self, start, end)->str:
        if end > start:
            return str(start) + "->" + str(end)
        else:
            return str(start)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return  nums
        elif len(nums) == 1:
            return [str(nums[0])]

        minv = nums[0]
        res = []
        for idx in range(1, len(nums)):
            #---check if this is the last element
            if idx == len(nums)-1:
                if (nums[idx] - 1) == nums[idx-1]:
                    res.append(self.get_range(minv, nums[idx])) #if sequential
                else:
                    res.append(self.get_range(minv, nums[idx-1]))
                    res.append(str(nums[idx]))
            #--check if not sequential
            elif (nums[idx] - 1) != nums[idx-1]:
                #--insert the previous summary range
                res.append(self.get_range(minv, nums[idx-1]))
                minv = nums[idx]
                
        return res

sol = Solution()
print(sol.summaryRanges([0,1,3,4,5,7,9,10,11,13]))
print(sol.summaryRanges([1,3]))