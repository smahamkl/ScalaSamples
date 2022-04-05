from typing import List
from collections import deque

'''
LeetCode 934  - Shortest bridge
'''
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        totrows = len(grid)
        totcols = len(grid[0])
        allmoves = deque()
        visited = set()
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
       
        def dfs(row:int, col:int):
            visited.add((row, col))
            allmoves.append([row, col, 0])
            for r,c in moves:
                r += row
                c += col
                if r >= 0 and c >= 0 and r < totrows and c < totcols and grid[r][c] == 1 and (r,c) not in visited:
                    dfs(r, c)
        
        def bfs()->int:
            while allmoves:
                curR, curC, totmoves = allmoves.popleft()
                for r,c in moves:
                    r += curR
                    c += curC
                    if r >= 0 and c >= 0 and r < totrows and c < totcols and (r,c) not in visited:
                        if grid[r][c] and totmoves > 0:
                            return totmoves
                        else:
                            visited.add((r,c))
                            allmoves.append([r,c, totmoves+1])
        
        for i in range(totrows):
            for j in range(totcols):
                if grid[i][j]:
                    dfs(i, j)
                    print(visited)
                    totmoves = bfs()
                    return totmoves

sol = Solution()
print(sol.shortestBridge([[0,1],[1,0]]))
print(sol.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(sol.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))
