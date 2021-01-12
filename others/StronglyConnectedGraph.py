from typing import List
from collections import defaultdict
'''
check if a graph is strongly connected
'''

class Solution:
    def __init__(self, v):
        self.graph = defaultdict(list)
        self.vertices = v

    def addEdge(self, start, end):
        self.graph[start].append(end)
    
    def dfs_traverse(self, v, visited):
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_traverse(i, visited)
    
    def getReverseGraph(self):
        sol = Solution(self.vertices)

        for i in self.graph:
            for j in self.graph[i]:
                sol.addEdge(j, i)
        
        return sol

    def checkIfStronglyConnected(self, start)->bool:
        visited = [False for x in range(self.vertices)]
        self.dfs_traverse(start, visited)

        for vertex in visited:
            if vertex == False:
                return False
        
        g = self.getReverseGraph()
        visited = [False for x in range(self.vertices)]
        g.dfs_traverse(0, visited)
        for vertex in visited:
            if vertex == False:
                return False

        return True

sol = Solution(4)
# sol.addEdge(0,1)
# sol.addEdge(0,3)
# sol.addEdge(1,2)
# sol.addEdge(2,4)
# sol.addEdge(3,4)
# sol.addEdge(4,5)
# sol.addEdge(5,3)
# sol.addEdge(5,0)
sol.addEdge(0,1)
sol.addEdge(1,2)
sol.addEdge(2,3)

print(sol.checkIfStronglyConnected(0))    