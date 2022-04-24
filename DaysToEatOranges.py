from typing import List, Set
from collections import deque

'''
LeetCode 1553. Minimum Number of Days to Eat N Oranges
This can be done using DP but BFS method also working just fine
'''
class Solution:
    def minDays(self, n: int) -> int:
        allPos = deque()
        allPos.append([n, 0])
        visited = set()
        visited.add(n)

        while allPos:
            oranges,totDays = allPos.popleft()

            #print(oranges, totDays)

            if oranges == 0:
                return totDays
            
            visited.add(oranges)

            tmpActions = []
            if oranges % 2 == 0 and (oranges - (oranges / 2)) > 0 and (oranges - (oranges / 2)) not in visited:
                tmpActions.append((oranges - (oranges / 2)))
            
            if oranges % 3 == 0 and (oranges - (2 * (oranges / 3)) > 0) and (oranges - (2 * (oranges / 3))) not in visited:
                tmpActions.append((oranges - (2 * (oranges / 3))))
            
            if oranges - 1 not in visited:
                tmpActions.append(oranges-1)
            
            for oranges in tmpActions:
                allPos.append([oranges, totDays+1])
        
        return -1

sol = Solution()
print(sol.minDays(6))