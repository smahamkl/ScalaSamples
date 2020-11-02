'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 
Constraints:
--------------
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1

        for idx in range(len(haystack)):
            if haystack[idx] == needle[0] and len(haystack[idx:]) >= len(needle):
                found = True
                l = 1
                while l < len(needle):
                    if haystack[idx+l] != needle[l]:
                        found = False
                        break
                    l += 1
                if found:
                    return idx
        return -1


sol = Solution()
print(sol.strStr("hello", "llo"))
#print(sol.strStr("", ""))
#print(sol.strStr("aaaaa", "bba"))