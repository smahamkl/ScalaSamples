from typing import List
'''
Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
'''
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        max_len = 1
        res = 1
        prev_char = s[0]
        for idx in range(1, len(s)):
            if s[idx] == prev_char:
                max_len += 1
            else:
                max_len = 1
            res = max(res, max_len)
            prev_char = s[idx]
        
        return res

sol = Solution()
print(sol.maxPower("abbcccddddeeeeedcba"))
print(sol.maxPower("hooraaaaaaaaaaay"))
print(sol.maxPower("tourist"))
print(sol.maxPower("triplepillooooow"))
print(sol.maxPower("leetcode"))
print(sol.maxPower("cc"))