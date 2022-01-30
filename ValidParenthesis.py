from collections import defaultdict, deque
from typing import List

'''
LeetCode 678 - Valid Parenthesis String
The below method uses bruteforce method using memoization technique
There is a greedy approach that would give a linear time complexity (check the below link)
https://www.youtube.com/watch?v=QhPdNS143Qg&t=551s
'''
class Solution:
    def checkValidString(self, s: str) -> bool:

        par_map = defaultdict()

        def evaluate_str(c:int, totalLeftParen:int)->bool:
            if c >= len(s):
                if totalLeftParen == 0:
                    par_map[(c, totalLeftParen)] = True
                    return True
                else:
                    par_map[(c, totalLeftParen)] = False
                    return False
            
            if (c, totalLeftParen) in par_map:
                return par_map[(c, totalLeftParen)]

            if s[c] == "(":
                dec1 = evaluate_str(c+1, totalLeftParen+1)
                par_map[(c+1, totalLeftParen+1)] = dec1
                return dec1
            elif s[c] == "*":
                dec1 = evaluate_str(c+1, totalLeftParen)
                dec2 = evaluate_str(c+1, totalLeftParen + 1)
                dec3 = False if totalLeftParen <= 0 else evaluate_str(c+1, totalLeftParen-1)

                par_map[(c+1, totalLeftParen)] = dec1
                par_map[(c+1, totalLeftParen + 1)] = dec2
                par_map[(c+1, totalLeftParen - 1)] = dec3

                return  dec1 or dec2 or dec3
            else:
                if totalLeftParen > 0:
                    dec1 = evaluate_str(c+1, totalLeftParen-1)
                    par_map[(c+1, totalLeftParen-1)] = dec1
                    return dec1
                else:
                    par_map[(c, totalLeftParen)] = False
                    return False
        
        return evaluate_str(0, 0)


sol = Solution()
print(sol.checkValidString("((((****"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("()"))
print(sol.checkValidString("())"))
print(sol.checkValidString("((())*"))
print(sol.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
print(sol.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
print(sol.checkValidString("("))