from typing import List
from collections import deque

'''
LeetCode 838
Push Dominoes
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        domstck = deque()
        dom_arr = list(dominoes)

        for i, dom in enumerate(dom_arr):
            if dom != ".":
                if domstck:
                    lasti, lastdom = domstck.popleft()
                    if lastdom == "R" and dom == "L":
                        tmpl, tmpr = lasti+1, i-1
                        while tmpr > tmpl:
                            dom_arr[tmpr] = "L"
                            dom_arr[tmpl] = "R"
                            tmpl += 1
                            tmpr -= 1
                    elif lastdom == "L" and dom == "L":
                        tmpr = i-1
                        while tmpr > lasti and dom_arr[tmpr] == ".":
                            dom_arr[tmpr] = "L"
                            tmpr -= 1                            
                    elif lastdom == "R" and dom == "R":
                        tmpl, tmpr = lasti+1, i
                        while tmpl < tmpr and dom_arr[tmpl] == ".":
                            dom_arr[tmpl] = "R"
                            tmpl += 1
                
                else:
                    if dom == "L":
                        tmpl = i-1
                        while tmpl >= 0 and dom_arr[tmpl] == ".":
                            dom_arr[tmpl] = "L"
                            tmpl -= 1
                domstck.append([i, dom])
        if domstck:
            lasti, lastdom = domstck.popleft()
            lasti += 1
            if lastdom == "R":
                while lasti < len(dom_arr):
                    if dom_arr[lasti] == ".":
                        dom_arr[lasti] = "R"
                    lasti += 1
        
        return "".join(dom_arr)

sol = Solution()
print(sol.pushDominoes("RR.L"))
print(sol.pushDominoes("R.R.L"))

