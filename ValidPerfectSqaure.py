from typing import List
import math
'''
LeetCode 367
Valid perfect square
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def bin_search(st:int, end:int, n:int)->bool:
            if end > st:
                if st ** 2 == n or end ** 2 == n:
                    return True
                mid = max(1, (end - st) // 2)
                if n >= ((st+mid) ** 2):
                    return bin_search(st+mid, end, n)
                else:
                    return bin_search(st, st+mid-1, n)
            elif end == st:
                return True if end ** 2 == n else False
            return False
        
        return True if num == 1 else bin_search(1, num//2, num)
    
sol = Solution()
print(sol.isPerfectSquare(808201))
print(math.sqrt(808201))
print(899 ** 2)