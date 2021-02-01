from queue import heappop
from queue import heappush
from typing import List
'''
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, 
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), 
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, 
left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

Idea:

Use Dijkstra's algorithm to find the "shortest" path from a given source (here (0,0)).
Note in this case, the cost combinator is max (third last line) instead of + in the classic setting.
Use heap or priority queue to find the best node to process at each step in log time.
Check for and pass on visited nodes to save time.

Complexity:
Say the map has m rows and n columns.
Time complexity is O(mn log(mn)), as we will need to go through mn vertices/cells and each time do heap push and pop for a heap of O(mn) size for O(mn) edges.
Space complexity is O(mn). Heap of size O(mn) edges and visited of O(mn) cells.

Submission status:
Runtime: 648 ms (beats 97.41 %)
Memory Usage: 15.5 MB (beats 81.66 %)
 
'''
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        di = (0, 1, 0, -1)
        dj = (1, 0, -1, 0)
        m, n = len(heights), len(heights[0])
        visited = [[False] * n for _ in range(m)]
        h = [(0, 0, 0)]
        while h:
            effort, i, j = heappop(h)
            if visited[i][j]:
                continue
            visited[i][j] = True
            if i + 1 == m and j + 1 == n:
                return effort  ## have reached the (m-1, n-1) cell
            for k in range(4):
                ii, jj = i + di[k], j + dj[k]
                if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj]:
                    neffort = max(effort, abs(heights[i][j] - heights[ii][jj]))
                    heappush(h, (neffort, ii, jj))
        return ## cell (m-1, n-1) not reachable, should never happen
sol = Solution()
print(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
print(sol.minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]))