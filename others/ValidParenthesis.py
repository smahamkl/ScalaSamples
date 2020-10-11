from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        
        char_stck = []
        for chr in s:
            if chr in ['}', ']', ')'] and len(char_stck) == 0:
                return False
            elif chr == '}' and char_stck[-1] == '{':
                char_stck.pop()
            elif chr == '}' and char_stck[-1] != '{':
                return False
            elif chr == ')' and char_stck[-1] == '(':
                char_stck.pop()
            elif chr == ')' and char_stck[-1] != '(':
                return False
            elif chr == ']' and char_stck[-1] == '[':
                char_stck.pop()
            elif chr == ']' and char_stck[-1] != '[':
                return False
            else:
                char_stck.append(chr)
        if len(char_stck) > 0:
            return False
        
        return True
sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("("))
print(sol.isValid("(]"))
print(sol.isValid("{[]}"))
print(sol.isValid("([)]"))
print(sol.isValid("()[]{}"))
print(sol.isValid("){"))
print(sol.isValid("(){}}{"))