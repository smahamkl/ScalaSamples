from typing import List
from collections import deque

'''
the bit matrix represents all connected land(1) and water(0)
The idea is to return True is there is land sorrounding the water
A land is connected sideways and diagonally as well
***   Work in progress ******
'''
class Solution:
    def checkIfAllSidesCovered(self, grid: List[List[int]]) -> bool:
      rowl,coll = len(grid), len(grid[0])
      r,c = -1,-1
      for tmpr in range(rowl):
        for tmpc in range(coll):
          if grid[tmpr][tmpc] == 1:
            r,c = tmpr,tmpc
            break
        
        if r > -1 and c > -1:
          break
      print(r,c)
      
      def checkifvalidmove(row:int, col:int)->bool:
        if row >= 0 and row < rowl and col >= 0 and col < coll and grid[row][col] == 1:
          return True
        return False   
 
      
      def backtrack(row:int, col:int, totalmoves:int) -> bool:
        for tmpr,tmpc in [[row-1, col], [row+1,col], [row, col-1], [row, col+1],[row-1, col-1],[row+1,col+1], [row-1,col+1], [row+1, col-1]]:
          if grid[tmpr][tmpc] == 2 and r == tmpr and tmpc == c and totalmoves > 1:
            return True
          if checkifvalidmove(tmpr,tmpc):
            print("its a valid move:", tmpr, tmpc)
            grid[tmpr][tmpc] = 2
            if backtrack(tmpr,tmpc,totalmoves+1):
              return True
            
            grid[tmpr][tmpc] = 1
          
        return False
      
      grid[r][c] = 2
      return backtrack(r,c,0)



sol = Solution()
print(sol.checkIfAllSidesCovered([
  [1,1,1,0,0],
  [0,0,1,0,0],
  [0,1,0,1,0],
  [0,1,0,1,0],
  [0,1,0,1,0],
  [0,1,1,1,0],
  [0,0,0,0,0]
]))