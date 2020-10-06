'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic={}
        for w in wordDict:
            if len(w) in dic:
                dic[len(w)].append(w)
            else:
                dic[len(w)]=[w]
        dp=[1]+[0]*len(s)
        for i in range(len(s)):
            for k in dic:
                if i-k+1>=0 and dp[i-k+1] and s[i-k+1:i+1] in dic[k]:
                    dp[i+1]=1
        return dp[-1]