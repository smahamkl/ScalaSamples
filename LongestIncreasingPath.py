from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        dp = {}

        def dfs(row, col, prevval):
            if row < 0 or row >= rows or col < 0 or col >= cols or matrix[row][col] <= prevval:
                return 0
            
            if (row, col) in dp:
                return dp[(row, col)]
            
            maxval = 1
            maxval = max(maxval, 1 + dfs(row+1, col, matrix[row][col]))
            maxval = max(maxval, 1 + dfs(row-1, col, matrix[row][col]))
            maxval = max(maxval, 1+ dfs(row, col+1, matrix[row][col]))
            maxval = max(maxval, 1 + dfs(row, col-1, matrix[row][col]))

            dp[(row, col)] = maxval

            return maxval
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, -1)

        return max(dp.values())

sol = Solution()
print(sol.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))