from typing import List
'''
https://practice.geeksforgeeks.org/problems/convert-array-into-zig-zag-fashion1638/1/?page=1&company[]=Amazon&curated[]=1&sortBy=submissions
'''
class Solution:
    def zigZag(self,arr, n):
        for i in range(1, n):
            if i % 2 == 1:
                if arr[i] - arr[i-1] < 0:
                      arr[i], arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i] - arr[i-1] > 0:
                      arr[i], arr[i-1] = arr[i-1], arr[i]
        return arr

sol = Solution()
print(sol.zigZag([4, 3, 7, 8, 6, 2, 1], 7))
print(sol.zigZag([1,4,3,2], 4))
