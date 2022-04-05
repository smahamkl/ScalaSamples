from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #---take 4 corners of the matrix---
        tl, tr, bl, br = [0,0], [0, len(matrix[0])-1], [len(matrix)-1, 0], [len(matrix)-1, len(matrix[0])-1]

        res = []
        totalelements = len(matrix)*len(matrix[0])
        

        while len(res) < totalelements:
            #---nove top left to right---
            row = tl[0]
            for col  in range(tl[1], tr[1]+1):
                res.append(matrix[row][col])
            
            if len(res) == totalelements:
                break
            
            col = tr[1]
            for row in range(tr[0]+1, br[0]+1):
                res.append(matrix[row][col])
            if len(res) == totalelements:
                break

            row = br[0]
            for col in range(br[1]-1, bl[1]-1, -1):
                res.append(matrix[row][col])
            
            if len(res) == totalelements:
                break

            col = bl[1]
            for row in range(bl[0]-1, tl[0], -1):
                res.append(matrix[row][col])
            
            tl =  [tl[0]+1, tl[1]+1]
            tr = [tr[0]+1, tr[1]-1]
            br = [br[0]-1, br[1]-1]
            bl = [bl[0]-1, bl[1]+1]
        
        return res

sol = Solution()
#print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))