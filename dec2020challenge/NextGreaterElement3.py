from typing import List
from itertools import permutations

class Solution:
    def getMinVal(self, arr):
        A = [int(''.join(x)) for x in permutations(arr, len(arr))]
        return str(min(A))

    def nextGreaterElement(self, n: int) -> int:
        nstr = list(str(n))
        startch = -1
        for i in range(len(nstr)-2, -1, -1):
            if(nstr[i] < nstr[i+1]):
                startch = i+1
                break
        if startch == -1:
            return startch
        nstr[startch],nstr[startch-1] = nstr[startch-1],nstr[startch]
        minS = self.getMinVal(nstr[startch:])
        return int(''.join(nstr[:startch] + list(minS)))


sol = Solution()
#print(sol.nextGreaterElement(213))
#print(sol.nextGreaterElement(230241))
print(sol.nextGreaterElement(12443322)) #13222344