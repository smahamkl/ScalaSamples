'''
LeetCode  - 3
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #---A typical sliding window problem---
        #---use a set structure to keep track of the characters --
        #---a left pointer for facilitating the sliding window ---
        l = 0
        chrset = set()
        res = 0

        for i in range(len(s)):
            while s[i] in chrset:
                chrset.remove(s[l])
                l+=1
            
            chrset.add(s[i])

            res = max(len(chrset), res)
        
        return res

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))