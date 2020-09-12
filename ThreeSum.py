from typing import List
import copy
from itertools import combinations

class Solution:
    def validArr(self, arr:List[int]) -> bool:
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
            elif arr[i] > 9:
                return False

        return True
    def combSum(self, k:int, n:int, arr, finalArr:List[List[int]]):
        if self.validArr(arr):
            if sum(arr) == n:
                if (arr not in finalArr):
                    finalArr.append(copy.deepcopy(arr))
                #now increment the nearest pointer
                arr[k-2] += 1
            elif sum(arr) > n:
                #decrement the farther pointer 
                arr[k-1] -= 1
            else:
                #increment the nearest/second pointer
                arr[k-2] += 1
            self.combSum(k, n, arr, finalArr)
        
    def combinationSum3_1(self, k: int, n: int) -> List[List[int]]:
        finalArr:List[List[int]] = []
        for i in range(1, 10):
            arr = []
            #assign (k-1) elements with consequetive numbers
            for j in range(k-1):
                arr.append(i+j)
            #last element/pointer needs to point to the last but one element(n-1)
            if n > 9:
                arr.append(9)
            else:
                arr.append(n-1)
            print(arr)
            self.combSum(k, n, copy.deepcopy(arr), finalArr)
            
        return finalArr
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return filter(lambda x: sum(x) == n, combinations(range(1, 10), r=k))


if __name__ == "__main__":
    sol = Solution()
    #print(sol.combinationSum3(3,7)) 
    #print(sol.combinationSum3(3,9))
    #print(sol.combinationSum3(2,18)) 
    #print(sol.combinationSum3(3,15)) 
    #[[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
    print(sol.combinationSum3(4,24)) 