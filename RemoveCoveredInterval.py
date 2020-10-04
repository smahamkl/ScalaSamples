from typing import List
'''
Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
Example 3:

Input: intervals = [[0,10],[5,12]]
Output: 2
Example 4:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2
Example 5:

Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= intervals[i][0] < intervals[i][1] <= 10^5
All the intervals are unique.
'''
class Solution:
    def is_covered(self, interval:List[int], newInterval:List[int])->bool:
        if (newInterval[0] >= interval[0]) and (newInterval[1] <= interval[1]):
            return True
        elif (newInterval[0] <= interval[0]) and (newInterval[1] >= interval[1]):
            return True
        
        return False
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return len(intervals)
        intervals = sorted(intervals)
        minI = intervals[0][0]
        maxI = intervals[0][1]
        tot_intervals = 1
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if self.is_covered([minI, maxI], interval):
                minI = min(minI, interval[0])
                maxI = max(maxI, interval[1])
                print("Covered:" + str([minI, maxI]))
            else:
                tot_intervals += 1
                minI = interval[0]
                maxI = interval[1]

        return tot_intervals
                


if __name__ == "__main__":
    sol = Solution()
    print(sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]))
    print(sol.removeCoveredIntervals([[1,4],[2,3]]))
    print(sol.removeCoveredIntervals([[0,10],[5,12]]))
    print(sol.removeCoveredIntervals([[3,10],[4,10],[5,11]]))
    print(sol.removeCoveredIntervals([[1,4],[1,2],[3,4]]))
    print(sol.removeCoveredIntervals([[1,4]]))
    print(sol.removeCoveredIntervals([[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]))