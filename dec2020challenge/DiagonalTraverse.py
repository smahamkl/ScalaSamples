from typing import List
'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
'''
class Solution:
    def isValidMove(self, row, col, totrows, totcols)->bool:
        if row >= 0 and row < totrows and col >= 0 and col < totcols:
            return True
        return False

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        elif len(matrix) == 1:
            return matrix[0]
        elif len(matrix[0]) == 1:
            return [x[0] for x in matrix]

        res = []
        res += [matrix[0][0]]
        totrows = len(matrix)
        totcols = len(matrix[0])
        dir = 'D'
        row = 0
        col = 1
        while True:
            print(res, row, col, dir)
            res += [matrix[row][col]]
            print(res, row, col, dir)
            if len(res) == (totcols * totrows):
                break

            if dir == 'D':
                if self.isValidMove(row+1, col-1, totrows, totcols): 
                    row+=1
                    col-=1
                elif self.isValidMove(row+1, col, totrows, totcols):
                    row+=1
                    dir = 'U'
                elif self.isValidMove(row, col+1, totrows, totcols):
                    col+=1
                    dir = 'U'
            else:
                if self.isValidMove(row-1, col+1, totrows, totcols):
                    row -= 1
                    col += 1
                elif self.isValidMove(row, col+1, totrows, totcols):
                    col += 1
                    dir = 'D'
                elif self.isValidMove(row+1, col, totrows, totcols):
                    row += 1
                    dir = 'D'
        return res

sol= Solution()
#print(sol.findDiagonalOrder([[ 1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]))
#print(sol.findDiagonalOrder([[ 1,2,3,4,5]]))
print(sol.findDiagonalOrder([[1], [2], [3]]))