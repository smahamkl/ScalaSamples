from typing import List
from collections import deque
'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
'''
class Solution:
    def decodeString(self, s: str) -> str:
        if len(s) < 1:
            return s
        strstck = deque()
        res = ""
        i = 0
        chrs = list(s)
        while i < len(chrs):
            if chrs[i].isdigit():
                tmp = chrs[i]
                #--what if the total number of digits are more than 1
                while i+1 < len(chrs) and chrs[i+1].isdigit():
                    tmp += chrs[i+1]
                    i += 1
                strstck.append(tmp)
            elif chrs[i] == "[":
                #--initiate the element inside the stack
                strstck.append("")
            elif chrs[i] == "]":
                #--process the stack and add to string ---
                tmppat = strstck.pop() * int(strstck.pop())
                #---what if there are already elements on the stack
                if len(strstck) > 0:
                    strstck.append(strstck.pop() + tmppat)
                else:
                    res += tmppat
            elif len(strstck) > 0:
                #----stack already initiated----
                strstck.append(strstck.pop() + chrs[i])
            else:
                #---any characters preceeding or following the encoded string---
                res += chrs[i]
            
            i += 1

        return res


sol = Solution()
#print(sol.decodeString("13[a2[c2[c]]]"))
#print(sol.decodeString("2[abc]3[cd]ef"))
#print(sol.decodeString("3[a2[c]]"))
print(sol.decodeString("3[a]2[bc]"))