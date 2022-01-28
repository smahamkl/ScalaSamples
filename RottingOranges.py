from collections import deque
from typing import List
from collections import deque

'''
994. Rotting Oranges
https://www.youtube.com/c/NeetCode/videos
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        totRows = len(grid)
        totCols = len(grid[0])

        def checkIfFreshOrange(r, c) -> bool:
            if r < 0 or c < 0 or r >= totRows or c >= totCols:
                return False
            if grid[r][c] == 1:
                return True
            
            return False
        

        nextSet = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    nextSet.append([row, col, 0])
        
        
        minMins = 0
        while nextSet:
            r,c, minMins = nextSet.popleft()
            posMoves = [[r-1, c], [r+1, c], [r, c-1], [r,c+1]]
            for item in posMoves:
                if checkIfFreshOrange(item[0], item[1]):
                    nextSet.append([item[0], item[1], minMins + 1])
                    grid[item[0]][item[1]] = 2
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        return minMins

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(sol.orangesRotting([[0,2]]))