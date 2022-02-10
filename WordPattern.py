from typing import List
'''
LeetCode 290
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split(" ")
        if len(pattern) != len(s_words):
            return False

        word_map = {}
        s_map = {}

        for i in range(len(pattern)):
            letter = pattern[i]
            if letter in word_map:
                #get the latest and previous position of the word
                prev,cur = word_map[letter], i
                if s_words[prev] == s_words[cur]:
                    word_map[letter] = i
                else:
                    return False
            else:
                word_map[letter] = i
                if s_words[i] in s_map:
                    return False
                s_map[s_words[i]] = 1
            
        return True

sol = Solution()
print(sol.wordPattern("abab", "dog cat dog cat"))