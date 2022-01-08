from typing import List

'''
Leetcode 438
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        parr = [0 for x in range(26)]
        sarr = [0 for x in range(26)]

        res = []

        for c in list(p):
            parr[ord(c) - ord('a')] += 1
        
        ctr = 0
        for i in range(len(s)):
            sarr[ord(s[i]) - ord('a')] += 1

            if parr == sarr:
                res.append(i - len(p)+1)
            #print(sarr)
            
            ctr += 1

            if ctr >= len(p):
                sarr[ord(s[i-len(p) + 1]) - ord('a')] -= 1
        
        return res

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "abc"))
print(sol.findAnagrams("abab", "ab"))