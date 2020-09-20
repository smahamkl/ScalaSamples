from typing import List
import sys

'''
On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid
'''
class Solution:
    def isValidMove(self, grid: List[List[int]], curPath: [], row:int, col:int) -> bool:
        if ((0 <= row < self.totRows) and (0 <= col < self.totCols)):
            if (row,col) in curPath:
                return False
            elif grid[row][col] == 0:
                return True
        return False
    def checkAdjFinalCell(self, grid:List[List[int]], curPath:[], curCell:(int,int))->bool:
        
        if(len(curPath) < ((self.totCols * self.totRows)-1-self.tothurdles)):
            return False

        if ((curCell[0]-1) >= 0) and grid[curCell[0]-1][curCell[1]] == 2:
            return True
        elif ((curCell[0]+1) < self.totRows) and grid[curCell[0]+1][curCell[1]] == 2:
            return True
        elif ((curCell[1]+1) < self.totCols) and grid[curCell[0]][curCell[1]+1] == 2:
            return True
        elif ((curCell[1]-1) >= 0) and grid[curCell[0]][curCell[1]-1] == 2:
            return True
        return False

    def findPaths(self, grid: List[List[int]], curPath: []):
        #print(curPath)
        l = len(curPath)
        curCell = curPath[l-1]
        #--now evaluate path for previous cell same row---
        if self.isValidMove(grid, curPath, curCell[0]-1, curCell[1]):
            self.findPaths(grid, curPath + [(curCell[0]-1, curCell[1])])
        #--now evaluate path for next cell same row---
        if self.isValidMove(grid, curPath, curCell[0]+1, curCell[1]):
            self.findPaths(grid, curPath  + [(curCell[0]+1, curCell[1])])
        #--now evaluate path cell above same column---
        if self.isValidMove(grid, curPath, curCell[0], curCell[1]-1):
            self.findPaths(grid, curPath + [(curCell[0], curCell[1]-1)])
        #--now evaluate path cell below same column---
        if self.isValidMove(grid, curPath, curCell[0], curCell[1]+1):
            self.findPaths(grid, curPath + [(curCell[0], curCell[1]+1)])
        if self.checkAdjFinalCell(grid, curPath, curCell):
            #print(curPath)
            self.totalPaths += 1

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        #--get the rwo,col index of 1--
        r = -1
        c = -1
        self.totalPaths = 0
        self.totRows = 0
        self.totCols = 0
        self.tothurdles = 0
        for row, ele in enumerate(grid):
            self.totRows += 1
            self.totCols = len(ele)
            for col, ele1 in enumerate(ele):
                if grid[row][col] == 1:
                    r = row
                    c = col
                elif grid[row][col] == -1:
                    self.tothurdles += 1
        lis = [(r,c)]
        #print(self.totRows, self.totCols)
        self.findPaths(grid, lis)
        return self.totalPaths

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
    print(sol.uniquePathsIII([[0,1],[2,0]]))