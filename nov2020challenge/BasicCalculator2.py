from typing import List
from collections import deque
import re
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
'''
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        tmp= ""
        terms = []
        for i in range(len(list(s))):
            chr = s[i].strip()
            if not chr:
                continue
            if chr in ['+', '-', '*', '/']:
                terms += [tmp] if tmp else [0]
                if chr == '-':
                    tmp = "-"
                    terms += ['+']
                else:
                    tmp = ""
                    terms += [chr]
            else:
                tmp += chr
        terms += [tmp]
        i = 0
        while i < len(terms):
            if terms[i] == '*':
                tmp = int(int(terms[i-1])*int(terms[i+1]))
                terms.pop(i)
                terms.pop(i)
                terms[i-1] = tmp
                i = 0
                continue
            elif terms[i] == '/':
                tmp = int(int(terms[i-1])/int(terms[i+1]))
                terms.pop(i)
                terms.pop(i)
                terms[i-1] = tmp
                i = 0 
                continue
            i += 1
        print(terms)
        i = 0
        while i < len(terms) and len(terms) > 1:
            if terms[i] == '+':
                tmp = int(terms[i-1]) + int(terms[i+1])
                terms.pop(i)
                terms.pop(i)
                terms[i-1] = tmp
                i = 0
                continue
            i += 1
        print(terms)
        i = 0
        while i < len(terms) and len(terms) > 1:
            if terms[i] == '-':
                tmp = int(terms[i-1]) - int(terms[i+1])
                terms.pop(i)
                terms.pop(i)
                terms[i-1] = tmp
                i = 0
                continue
            i += 1
        
        return terms[0]

sol = Solution()
# print(sol.calculate(" 3+5 / 2 "))
# print(sol.calculate(" 3/2 "))
# print(sol.calculate("3+2*2"))
#print(sol.calculate("1-1+1"))
print(sol.calculate("14/3*2"))