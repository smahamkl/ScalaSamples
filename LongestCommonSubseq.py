from typing import List

'''
LeetCode 1143
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

                if text1[i-1] == text2[j-1]:
                    dp[i][j] = max(1+dp[i-1][j-1], dp[i][j])

        return dp[l1][l2]


sol = Solution()
print(sol.longestCommonSubsequence("abc", "def"))
