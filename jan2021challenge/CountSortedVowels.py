from typing import List
'''
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically 
sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
'''
class Solution:
    def __init__(self):
        self.res = 0
    def fillWords(self, n, i, v, vi, word):
        if i == n:
            #print(word)
            self.res+=1
        elif i <= n-1:
            for idx in range(vi, len(v)):
                self.fillWords(n, i+1, v[idx:], vi, word+v[idx] )

    def countVowelStrings(self, n: int) -> int:
        v = ['a', 'e', 'i', 'o','u']
        self.fillWords(n,0, v, 0, "")
        return self.res

sol = Solution()
print(sol.countVowelStrings(1))