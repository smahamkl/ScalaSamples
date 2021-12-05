from typing import List

'''
Constraint: 0<=len(s)<=1000
Given a string:
1.) Take all prefixes of the string and choose the longest palindrome between them.
2.) If chosen prefix has atleast two characters, cut this from s and go back to step 1 with the updated string. 
Otherwise, end the algo with the current string s.
'''
class Solution:
    def getstring(self, s)->str:
        def checkpalindrome(s)->bool:
            st,end = 0, len(s)-1
            while st < end:
                if s[st] != s[end]:
                    return False
                
                st += 1
                end -= 1
            return True
        
        nextstr = s

        while nextstr:
            palprefix = ""
            tmp = nextstr[0]
            for i in range(1, len(nextstr)):
                tmp += nextstr[i]
                if checkpalindrome(tmp):
                    palprefix = tmp
            if palprefix == "":
                break
            else:
                nextstr = nextstr[len(palprefix):]
        
        if len(nextstr) == 1:
            return ""
        else:
            return nextstr
    
sol = Solution()
print(sol.getstring("codesignal"))