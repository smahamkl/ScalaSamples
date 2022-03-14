from typing import List
import heapq

'''
LeetCode 973
K Closest Points to Origin
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def eqDistance(x1, y1)->float:
            return ((x1 ** 2) + (y1 ** 2))
        
        heapt = []
        res = []
        
        for x, y in points:
            heapq.heappush(heapt, [eqDistance(x, y), x, y])
        while(k > 0):
            d,x,y = heapq.heappop(heapt)
            res.append([x,y])
            k -= 1
        
        return res


sol  = Solution()
print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
print(sol.kClosest([[1,3],[-2,2]], 1))

