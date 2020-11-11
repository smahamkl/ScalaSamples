from typing import List
'''
Valid Square
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''
class Solution:
    def coordDistance(self, p1, p2)->float:
        return ((p2[1]-p1[1]) ** 2) + ((p2[0]-p1[0]) ** 2)
    
   
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        dist_arr = []
        dist_arr.append(self.coordDistance(p1,p2))
        dist_arr.append(self.coordDistance(p1,p3))
        dist_arr.append(self.coordDistance(p1,p4))
        dist_arr.append(self.coordDistance(p2,p3))
        dist_arr.append(self.coordDistance(p2,p4))
        dist_arr.append(self.coordDistance(p3,p4))
        if not min(dist_arr):
            return False
        
        if 2 * min(dist_arr) == max(dist_arr) and len(set(dist_arr)) == 2:
            return True

        return False

sol = Solution()
#print(sol.validSquare(p1=[1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]))
#print(sol.validSquare(p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]))
#print(sol.validSquare(p1 = [1,1], p2 = [0,1], p3 = [1,2], p4 = [0,0]))
print(sol.validSquare([0,0],[1,1],[1,0],[1,1]))