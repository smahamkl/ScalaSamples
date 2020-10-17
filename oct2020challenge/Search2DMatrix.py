from typing import List
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
class Solution:
    def search_list_x(self, col_arr:[], left:int, right:int, target:int)->int:
        if right > left:
            m =left + int((right - left) / 2)
            if col_arr[m] == target:
                return m
            elif target < col_arr[m]:
                return self.search_list_x(col_arr, left, m - 1, target)
            elif target > col_arr[m]:
                return self.search_list_x(col_arr, m+1, right, target)
        elif right == left and (col_arr[left] == target):
            return left
        else:
            return -1
    def search_list_y(self, col_arr:[], left:int, right:int, target:int)->int:
        if right > left:
            m =left + int((right - left) / 2)
            if col_arr[m][0] <= target <= col_arr[m][1]:
                return m
            elif target < col_arr[m][0]:
                return self.search_list_y(col_arr, left, m - 1, target)
            elif target > col_arr[m][1]:
                return self.search_list_y(col_arr, m+1, right, target)
        elif right == left and (col_arr[left][0] <= target <= col_arr[left][1]):
            return left
        else:
            return -1
        

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or (len(matrix) == 1 and len(matrix[0]) == 0):
            return False
        col_arr = [(x[0], x[len(x)-1]) for x in matrix]
        #print(col_arr)
        row = self.search_list_y(col_arr, 0, len(col_arr)-1, target)
        #print(matrix[row], len(matrix[row])-1)
        if row == -1:
            return False
        col = self.search_list_x(matrix[row], 0, len(matrix[row])-1, target)
        if col == -1:
            return False
        else:
            return True

sol = Solution()
#print(sol.searchMatrix([[1,3,5,7,9],[10,11,16,20,21],[23,30,34,50,51]], 12))
#print(sol.searchMatrix([[1,3,5,7,9,11]], 0))
print(sol.searchMatrix([[]], 1))