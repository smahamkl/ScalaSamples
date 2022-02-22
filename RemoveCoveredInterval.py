from typing import List

'''
LeetCode 1288

Remove Covered Intervals
'''
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[0])

        tmpx, tmpy = intervals[0]
        res = set()
        # 1,4 : 2:3  or 1,2: 1:4 

        for i in range(1, len(intervals)):
            tmpx_cur,tmpy_cur = intervals[i]
            if (tmpx_cur >= tmpx and tmpy_cur <= tmpy):
                tmpx,tmpy = tmpx,tmpy
            elif (tmpx == tmpx_cur and tmpy_cur >= tmpy):
                tmpx,tmpy = tmpx_cur, tmpy_cur
            else:
                res.add((tmpx, tmpy))
                tmpx,tmpy = tmpx_cur,tmpy_cur
        
        res.add((tmpx, tmpy))

        return len(res)

sol = Solution()
#print(sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
#print(sol.removeCoveredIntervals([[1,4],[2,3]]))
print(sol.removeCoveredIntervals([[1,4],[1,2],[1,3],[2,5]]))