from typing import List

'''
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:
Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:
Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
'''
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        lsize = 1
        rsize = 0
        mtnsize = 0

        for idx in range(1, len(A)):
            if A[idx] > A[idx-1]:
                if rsize > 0:
                    mtnsize = max(mtnsize, lsize+rsize)
                    lsize = 1
                    rsize = 0
                lsize += 1
            elif lsize > 1 and A[idx] < A[idx-1]:
                rsize += 1
            else:
                if lsize > 1 and rsize >= 1:
                    mtnsize = max(mtnsize, lsize+rsize)
                lsize = 1
                rsize = 0
            
            #print(lsize, rsize, mtnsize)
        
        return max(mtnsize, lsize + rsize) if rsize > 0 else mtnsize


sol = Solution()
print(sol.longestMountain([2,1,4,7,3,2,5]))
print(sol.longestMountain([2,3,2,3,4,5,4,3,2,1]))
print(sol.longestMountain([2,3,2,2,2,2,2,2,3,2,1]))
print(sol.longestMountain([2,3,2,2,2,2,2,2]))
print(sol.longestMountain([2,2,2]))
print(sol.longestMountain([2,3,4]))
print(sol.longestMountain([4,3,2]))