from typing import List
from collections import Counter
'''
In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the ith domino.  
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1
Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, 
as indicated by the second figure
'''
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        cmn_element = [x for x, count in Counter(A+B).items() if count>=len(A)]
        if len(cmn_element) == 0 or len(A) == 0 or len(B) == 0:
            return -1
        rot_a = rot_b = 0
        for item in zip(A,B):
            if cmn_element[0] != item[0] and cmn_element[0] != item[1]:
                return -1
            elif cmn_element[0] != item[0] and cmn_element[0] == item[1]:
                rot_a += 1
            elif cmn_element[0] == item[0] and cmn_element[0] != item[1]:
                rot_b += 1
        return min(rot_a, rot_b)
    
sol = Solution()
#print(sol.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(sol.minDominoRotations([2,3,2], [3,2,3]))
#print(sol.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))