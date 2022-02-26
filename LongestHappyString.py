import heapq
from typing import List

'''
LeetCode 1405
Priority Queue problem
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #---first define a list to hold the total occurences -> a/b/c and push them into priority queue
        input = []
        res = ""
        cntr = 0

        for item in [(-a, "a"),(-b, "b"),(-c, "c")]:
            if item[0] < 0:
                heapq.heappush(input, item)
        
        heapq.heapify(input)
        while input:
            cnt_1st, char_1st = heapq.heappop(input)

            if cntr > 1 and (res[-1] == res[-2] == char_1st):
                if input:
                    cnt_2nd, char_2nd = heapq.heappop(input)
                    res += char_2nd
                    cnt_2nd += 1
                    cntr += 1
                    if cnt_2nd < 0:
                        heapq.heappush(input, (cnt_2nd, char_2nd))
                else:
                    break
            else:
                res += char_1st
                cnt_1st += 1
                cntr += 1

            if cnt_1st < 0:
                heapq.heappush(input, (cnt_1st, char_1st))
        
        return res



sol = Solution()
#print(sol.longestDiverseString(1,1,7))
print(sol.longestDiverseString(7,1,0))
