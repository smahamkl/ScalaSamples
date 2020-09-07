'''
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''
class Solution:

    def wordPattern(self, pattern: str, str: str) -> bool:
        charMap = {}
        strList = str.split(" ")
        wordMap = {}
        

        if len(pattern) != len(strList):
            return False
        elif len(pattern) == 1:
            return True
        
        wordMap[strList[0]] = 1

        
        for i in range(0, len(pattern)):
            if i == 0:
                charMap[pattern[i]] = i
            else:
                if pattern[i] not in charMap:
                    charMap[pattern[i]] = i

                if (charMap[pattern[i]] == i) & (strList[i] in wordMap):
                    return False
                elif strList[i] != strList[charMap[pattern[i]]]:
                    return False
            if strList[i] not in wordMap:
                wordMap[strList[i]] = 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordPattern("abba", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog cat cat fish"))
    print(sol.wordPattern("aaaa", "dog cat cat dog"))
    print(sol.wordPattern("abba", "dog dog dog dog"))
    print(sol.wordPattern("abc", "dog cat dog"))
