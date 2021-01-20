from typing import List
'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        substring = ''
        for i in range(len(s)):
            word_even = self.radial(i, i+1, s)
            word_odd = self.radial(i, i, s)

            print(word_even, word_odd)
            
            max_word = word_even if len(word_even) > len(word_odd) else word_odd
            
            if len(substring) < len(max_word):
                substring = max_word
        return substring
    
    def radial(self, l, r, words):
        while l >= 0 and r < len(words) and words[l] == words[r]:
            l-= 1
            r+= 1
        
        return words[l+1:r]

sol = Solution()
print(sol.longestPalindrome("madammadam"))