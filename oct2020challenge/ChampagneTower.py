from typing import List
'''
We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, and so on until the 100th row.  Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top.  When the topmost glass is full, any excess liquid poured will fall equally to the glass 
immediately to the left and right of it.  When those glasses become full, any excess champagne will fall equally to the left and right of those glasses, and so on.  
(A glass at the bottom row has its excess champagne fall on the floor.)

For example, after one cup of champagne is poured, the top most glass is full.  After two cups of champagne are poured, the two glasses on the second row are half full. 
After three cups of champagne are poured, those two cups become full - there are 3 full glasses total now.  
After four cups of champagne are poured, the third row has the middle glass half full, and the two outside glasses are a quarter full, as pictured below.

******* SOLUTION ***************
There will be i*(i+1)/2 glasses till ith row (including ith row) and Initialize all glasses as empty
1) Put all water in first glass
2) Now let the water flow to the downward glasses till the row number is less than or/ equal to i (given row) correction : X can be zero for side glasses as 
they have lower rate to fill
3) Fill glasses in a given row. Number of columns in a row is equal to row number
4) Keep the amount less than or equal to capacity in current glass
5) Distribute the remaining amount to the down two glasses
'''
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured <= 1:
            if poured == 1 and (query_row == 0 and query_glass == 0):
                return 1
            else:
                return 0

        glass = [[0.0 for x in range(query_row+2)] for x in range(query_row+2)]

        glass[0][0] = poured
        for row in range(query_row+1):
            for col in range(row+1):
                poured = glass[row][col]
                #--check if champagne poured is greater than its capacity to spill down to the bottom glasses
                if poured > 1:
                    poured -= 1
                    #--now take remaining champagne and spill to bottom glasses---
                    glass[row+1][col] += poured/2
                    glass[row+1][col+1] += poured/2

        #print(glass)
        return min(glass[query_row][query_glass], 1.0)
        
    #---working but copied from the leetcode forums -----------------------
    # def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    #     cur=[poured]
    #     for l in range(1,query_row+1):
    #         cur_=[0]*(l+1)
    #         for i in range(l):
    #             p=(cur[i]-1)/2
    #             if p<0: continue
    #             cur_[i]+=p
    #             cur_[i+1]+=p
    #         cur=cur_
    #     return cur[query_glass] if cur[query_glass]<1 else 1

sol = Solution()
#print(sol.champagneTower(100000009, 33, 17))
#print(sol.champagneTower(2, 1, 1))
#print(sol.champagneTower(25, 6, 1))
print(sol.champagneTower(25, 6, 1)) #0.18750
#print(sol.champagneTower(0,0,0))