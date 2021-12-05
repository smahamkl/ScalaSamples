from typing import List
'''
Leetcode - 56
https://leetcode.com/problems/merge-intervals/submissions/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        elif len(intervals) <= 1:
            return intervals

        intervals.sort()
        res = []

        for start,end in intervals:
            if len(res) == 0:
                res.append([start,end])
            else:
                curst,curend = res.pop()
                if(start > curend):
                    res.append([curst, curend])
                    res.append([start, end])
                else:
                    res.append([curst, max(curend, end)])
        return res

sol = Solution()
#res = sol.merge([[1,3],[2,6],[8,10],[15,18]])
res = sol.merge([[1,4],[2,3]])
print(res)


