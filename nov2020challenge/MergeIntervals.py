from typing import List
'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        if len(intervals) > 0 and intervals[0]:
            intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        tmp = intervals[0]

        for idx in range(1, len(intervals)):
            if intervals[idx][0] > tmp[1]:
                res += [tmp]
                tmp = intervals[idx]
            else:
                tmp = [min(tmp[0], intervals[idx][0]), max(tmp[1], intervals[idx][1])]
        
        res += [tmp]
        return res


sol = Solution()
#print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
#print(sol.merge([[1,3],[3,5]]))
#print(sol.merge([[1,4],[4,5]]))
#print(sol.merge([[1,4],[0,4]]))
#print(sol.merge([[1,4],[2,3]]))
print(sol.merge([[1,4],[0,2],[3,5]]))