import heapq
from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minheap = []
        res = []

        for item in arr:
            minheap.append((abs(item-x), item))
        
        heapq.heapify(minheap)

        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        
        res.sort()
        return res


sol = Solution()
print(sol.findClosestElements([1,2,3,4,5], 4, 3))
print(sol.findClosestElements([0, 2], 1, 1))