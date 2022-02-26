from typing import List
import functools

'''
LeetCode 1288

Remove Covered Intervals
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        if k >= len(num):
            return "0"

        res = []
        i = 0
        while i <= len(num) - k:
            res.append(int(num[:i] + num[i+k:]))
            i += 1
        
        print(res)
        
        return str(min(res))

sol = Solution()
print(sol.removeKdigits("1432219", 3))
print(sol.removeKdigits("10200", 1))
print(sol.removeKdigits("10", 2))
print(sol.removeKdigits("112", 1))