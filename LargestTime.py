from itertools import permutations
from typing import List
'''
LeetCode - 949  Largest Time for Given Digits(Medium)

Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format.  If no valid time can be made, return an empty string.
 

Example 1:

Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". Of these times, "23:41" is the latest.
'''
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        if all(ele == 0 for ele in arr):
            return "00:00"

        times = permutations(arr, 4)

        largetime = 0
        for each in times:
            tmp = each[3]
            tmp += (each[2] * 10) + (each[1] * 100) + (each[0] * 1000)
            if each[2] * 10 > 59:
                continue
            if (each[1] * 100) + (each[0] * 1000) > 2300:
                continue
            largetime = max(largetime, tmp)
        
        if largetime ==0:
            return ""

        res = str(largetime).rjust(4, "0")
        return str(res[:2]) + ":" + str(res[2:4])

sol = Solution()
# print(sol.largestTimeFromDigits([1,2,3,4]))
# print(sol.largestTimeFromDigits([5,5,5,5]))
# print(sol.largestTimeFromDigits([0,0,1,0]))
# print(sol.largestTimeFromDigits([0,9,1,9]))
print(sol.largestTimeFromDigits([0,0,3,0]))