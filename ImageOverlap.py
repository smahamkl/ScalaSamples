from typing import List
import copy
import collections

'''
Sep Challenge - Leetcode
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  
After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
'''
#***Working Solution, copied from the discussion board on Leetcode ****
class Solution1:
    '''
    The logic here is to first get the coordinates of both the lists  A & B having the bit value '1'
    Then check the distance between x & y coordinates(ax-bx, bx-by) for each combination of coordinate values and form a list of tuples
    Using the collections counter class, aggregating/count the tuples having the same distance between the coordinstes
    Of all the tuples, the tuple having the maximum count will be solution to the most overlapped binary bit cells from both the lists 
    '''
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A= [(i,j) for i, row in enumerate(A) for j , item in enumerate(row) if item ]
        B =[(i,j) for i , row in enumerate(B) for j , item in enumerate(row) if item ]
        count=collections.Counter((ax-bx,ay-by) for ax, ay in A for bx,by in B)
        return max(count.values() or [0])

#----------------Solution I have tried----------------------------------
class Solution:
    def __init__(self):
        self.N = 0

    def checkLargestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        count = 0
        for idx1, elA in enumerate(A):
            elB = B[idx1]
            for idx2, item1 in enumerate(elA):
                item2 = elB[idx2]
                if 1 & item1 & item2:
                    count += 1
        return count

    def shiftUp(self,  A: List[List[int]]) -> List[List[int]]:
        B = copy.deepcopy(A)
        for i in range(len(B)):
            if (i+1) < len(B):
                B[i] = A[i+1]

        B[len(B) - 1] = [0 for i in range(len(B))]
        return B

    def shiftDown(self,  A: List[List[int]]) -> List[List[int]]:
        B = copy.deepcopy(A)
        for i in range(1, len(A)):
            B[i] = list(A[i-1])

        B[0] = [0 for i in range(len(B))]
        return B

    def shiftLeft(self, A: List[List[int]]) -> List[List[int]]:
        B = copy.deepcopy(A)
        for i in range(len(B)):
            inlst = B[i]
            for j in range(len(inlst)):
                if (j+1) < len(B):
                    inlst[j] = inlst[j+1]
                else:
                    inlst[j] = 0
        return B

    def shiftRight(self, A: List[List[int]]) -> List[List[int]]:
        B = copy.deepcopy(A)
        for i in range(len(B)):
            for j in range(1, len(B)):
                B[i][j] = A[i][j-1]

        for i in range(len(B)):
            B[i][0] = 0
        return B

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        res = 0

        minL = min(A, B)
        maxL = max(A, B)
        if minL == 0:
            return 0

        res = self.checkLargestOverlap(minL, maxL)
        tmp = -1
        for i in range(len(A)):
            maxL = self.shiftDown(maxL)
            tmp = self.checkLargestOverlap(minL, maxL)
            if tmp > res:
                res = tmp
        
        maxL = max(A, B)

        for i in range(len(A)):
            maxL = self.shiftUp(maxL)
            #print(maxL)
            tmp = self.checkLargestOverlap(minL, maxL)
            if tmp > res:
                res = tmp

        maxL = max(A, B)

        for i in range(len(A)):
            maxL = self.shiftLeft(maxL)
            #print(maxL)
            tmp = self.checkLargestOverlap(minL, maxL)
            if tmp > res:
                res = tmp

        maxL = max(A, B)

        for i in range(len(A)):
            maxL = self.shiftRight(maxL)
            print(maxL)
            tmp = self.checkLargestOverlap(minL, maxL)
            if tmp > res:
                res = tmp
        return res


if __name__ == "__main__":
    sol = Solution1()
    # print(sol.shiftUp([[1, 1, 0], [0, 1, 0], [0, 1, 0]]))
    # print(sol.shiftDown([[1, 1, 0], [0, 1, 0], [0, 1, 0]]))
    # print(sol.shiftLeft([[1, 1, 0], [0, 1, 0], [0, 1, 0]]))
    #print(sol.shiftRight([[1, 1, 0], [0, 1, 0], [0, 1, 0]]))
    print(sol.largestOverlap(A=[[1, 1, 0], [0, 1, 0], [
          0, 1, 0]], B=[[0, 0, 0], [0, 1, 1], [0, 0, 1]]))
    # print(sol.largestOverlap(A=[[1, 1, 0], [0, 1, 0], [
    #       0, 1, 0]], B=[[1, 1, 0], [0, 1, 0], [1, 1, 0]]))
    # print(sol.largestOverlap(A=[[1, 0], [1, 0]], B=[[0, 1], [1, 0]]))
    #print(sol.largestOverlap(A = [[0,1],[1,1]], B = [[1,1],[1,0]]))

    #print(sol.checkLargestOverlap(A = [[1,1,0],[0,1,0],[0,1,0]], B = [[0,0,0],[0,1,1],[0,0,1]]))
    #print(sol.checkLargestOverlap(A = [[0,1],[1,1]], B = [[1,1],[1,0]]))
