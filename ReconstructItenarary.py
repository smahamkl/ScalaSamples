from typing import List
'''
LeetCode - 332 
https://www.youtube.com/watch?v=ZyB_gQ8vqGA
'''

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = {x[0]:[] for x in tickets}

        for ticket in tickets:
            src, dest = ticket[0], ticket[1]
            adj[src].append(dest)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False
            
            tmp = list(adj[src])

            for i, v in enumerate(tmp):
                res.append(v)
                adj[src].pop(i)

                if dfs(v): return True

                res.pop()
                adj[src].insert(i, v)
            
            return False
        dfs("JFK")
        return res


sol = Solution()
#res = sol.reconstructIter([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
res = sol.findItinerary([["JFK","ATL"],["JFK","SFO"],["SFO","JFK"]])
print(res)
