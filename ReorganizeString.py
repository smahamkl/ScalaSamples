from collections import Counter
import heapq

'''
LeetCode - 767  
https://www.youtube.com/watch?v=2g_b1aYTHeg

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

'''
class Solution:
    def reorganizeString(self, s: str) -> str:
        charCnt = Counter(s)

        il = [(-cnt, char) for char, cnt in charCnt.items()]

        heapq.heapify(il)

        prev = None
        res = ""

        while il:
            cnt, char = heapq.heappop(il)
            res += char

            if prev and prev[0] != 0:
                heapq.heappush(il, prev)
            
            prev = (cnt+1, char)
       
        if len(res) != len(s):
            return ""
        else:
            return res



sol = Solution()
print(sol.reorganizeString("aaab"))