from typing import List

'''
LeetCode: 802
https://leetcode.com/problems/find-eventual-safe-states/
'''
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        totnodes = len(graph)
        nodeMap = {}
        res = []

        def dfs(idx:int) -> bool:
            if idx in nodeMap:
                return nodeMap[idx]
            
            nodeMap[idx] = False

            for item in graph[idx]:
                if not dfs(item):
                    return False
                
            nodeMap[idx] = True
            
            return True



        for i in range(totnodes):
            if dfs(i):
                res.append(i)
        
        print(nodeMap)
                     

        return res

sol = Solution()
print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))