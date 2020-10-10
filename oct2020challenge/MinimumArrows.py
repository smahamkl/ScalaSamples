from typing import List
'''
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start 
and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates 
of start and end of the diameter suffice. The start is always smaller than the end.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend 
bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. 
An arrow once shot keeps traveling up infinitely

Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.


Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and 
another arrow at x = 11 (bursting the other two balloons).
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Example 4:

Input: points = [[1,2]]
Output: 1
Example 5:

Input: points = [[2,3],[2,3]]
Output: 1
 

Constraints:

0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1
'''
class Solution:
    def is_overlapping(self, point1:List[int], point2:List[int])->bool:
        if point1[0] <= point2[0] <= point1[1]:
            return True
        return False
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        elif len(points) == 1:
            return 1
        #points = sorted(points)
        points = sorted(points, key=lambda x: x[1])
        print(points)
        from_point = points[0]
        tot_arrows = 1
        for i in range(1, len(points)):
            if self.is_overlapping(from_point, points[i]):
                print(str(points[i]) + " is overlapping with: " + str(from_point))
                minx = max(from_point[0], points[i][0])
                maxy = min(from_point[1], points[i][1])
                from_point = [minx, maxy]
                print("new from point is:" + str(from_point))
            else:
                tot_arrows += 1
                from_point = points[i]
        return tot_arrows

sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12],[7,14]]))
# print(sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
# print(sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))
# print(sol.findMinArrowShots([[1,2]]))
# print(sol.findMinArrowShots([[2,3],[2,3]]))
# print(sol.findMinArrowShots([]))