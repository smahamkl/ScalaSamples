from typing import List
import heapq
'''
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j). 

Note: It is assumed that negative cost cycles do not exist in the input matrix.
 

Example 1:

Input: grid = {{9,4,9,9},{6,7,6,4},
{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
'''
class Solution:
    def minimumCostPath(self, grid):
        rows,cols = len(grid), len(grid[0])
        visited = set()
        nextMoves = []
        heapq.heappush(nextMoves, [grid[0][0],0,0])
        visited.add((0,0))

        while nextMoves:
            cost,r,c = heapq.heappop(nextMoves)
            if r == rows-1 and c == cols-1:
                return cost

            for tmpr, tmpc in [[r,c-1],[r,c+1],[r-1, c],[r+1,c]]:
                if tmpr >= 0 and tmpc >= 0 and tmpr < rows and tmpc < cols and (tmpr,tmpc) not in visited:
                    heapq.heappush(nextMoves, [cost+grid[tmpr][tmpc], tmpr, tmpc])
                    visited.add((tmpr,tmpc))
        return 0

sol  = Solution()
sol.minimumCostPath([[9,4,9,9],[6,7,6,4],[8,3,3,7],[7,4,9,10]])
sol.minimumCostPath([[4,4],[3,7]])