from typing import List
'''
LeetCode 1007
1007. Minimum Domino Rotations For Equal Row
Using dictionary
'''
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count = {c:[0,0] for c in range(1,7)} # only 6 numbers O(1) space
        
        for i in range (len(tops)):
            count[tops[i]][0] +=1
            count[bottoms[i]][1] +=1
        
        def minMoves(k, pos)->int:
            minMoves = 0
            for i in range(len(tops)):
                if pos == 0:
                    if tops[i] == k:
                        continue
                    elif bottoms[i] == k:
                        minMoves += 1
                    else:
                        return len(tops)
                else:
                    if bottoms[i] == k:
                        continue
                    elif tops[i] == k:
                        minMoves += 1
                    else:
                        return len(tops)
            return minMoves                  
        
        res = len(tops)
        #print(count)
        for k,v in count.items():
            if v[0] + v[1] >= len(tops):
                if v[0] > v[1]:
                    res = min(res, minMoves(k, 0))
                else:
                    res = min(res, minMoves(k, 1))
        
        return res if res != len(tops) else -1

sol = Solution()
print(sol.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(sol.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))