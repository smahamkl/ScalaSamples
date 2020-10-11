from typing import List
import copy
'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        a = list(matrix)
        for i in range(len(a)):
            matrix[i] = [x[i] for x in a][::-1]
        
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol.rotate(matrix)
print(matrix)
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
sol.rotate(matrix)
print(matrix)
# print(sol.rotate([[5]]))
# print(sol.rotate([[1,2],[3,4]]))
