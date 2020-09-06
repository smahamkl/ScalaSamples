from typing import List

class Solution:
    def __init__(self):
        self.evalStateList = []
        self.N = 0

    def swapElements(self, A: List[int], src:int, dest:int):
        if A[src] != A[dest]:
            A[src], A[dest] = A[dest], A[src]

    def checkLargestOverlap(self, A: List[int], B: List[int]) -> int:
        count = 0
        for i in range(len(A)):
            if 1 & A[i] & B[i]:
                count+=1
        return count

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A1 = []
        B1 = []
        self.N = len(A)
        for eachList in A:
            for item in eachList:
                A1.append(item)

        for eachList in B:
            for item in eachList:
                B1.append(item)
        print("Size of the matrix: " + str(self.N))
        print(A1)
        print(B1)
        print(self.checkLargestOverlap(A1, B1))

        return 0

if __name__ == "__main__":
    sol = Solution()
    sol.largestOverlap(A = [[1,1,0],[0,1,0],[0,1,0]], B = [[0,0,0],[0,1,1],[0,0,1]])