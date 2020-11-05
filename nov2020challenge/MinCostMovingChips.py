from typing import List
from queue import PriorityQueue
import collections

class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        if len(position) <= 1:
            return 0

        max_val = max(position)
        num_map = {x:cnt for x,cnt in collections.Counter(position).items()}

        print(num_map)
        
        q = PriorityQueue()
        for k,v in num_map.items():
            q.put((v, k))
        
        res = 0
        if len(num_map.keys()) > 1:
            while not q.empty():
                tot,pos = q.get()
                newtot, newpos = q.get()
                pos, newpos = pos%2, newpos%2
                print(tot, pos, newtot, newpos)
                if abs(newpos - pos) == 1:
                    res += tot

                if q.empty():
                    break
                else:
                    q.put((tot+newtot, newpos))
        
        return res



sol = Solution()
#print(sol.minCostToMoveChips([2,2,2,3,3]))
#print(sol.minCostToMoveChips([1,1000000000]))
print(sol.minCostToMoveChips([1,2,3]))