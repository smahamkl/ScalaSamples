from typing import List

'''
LeetCode 74
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        def binSearch(arr:List[int], l, r)->int:
            while l <= r:
                m = (l + r) // 2

                if arr[m] == target:
                    return True
                
                if target < arr[m]:
                    r = m -1
                else:
                    l = m + 1
            
            return False

        l, r = 0, rows-1

        while l <= r:
            m = (l + r) // 2

            if target >= matrix[m][0] and target <= matrix[m][cols-1]:
                return binSearch(matrix[m], 0, cols-1)
            
            if target < matrix[m][0]:
                r = m - 1
            
            else:
                l = m + 1
        
        return False

sol  =Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 33))