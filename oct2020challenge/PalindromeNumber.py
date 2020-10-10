from typing import List

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        x1 = str(x) + str(x)[::-1]
        print(x1)
        xlen = len(str(x))
        for i in range(xlen):
            if x1[i] != x1[i+xlen]:
                return False
        
        return True

        
sol = Solution()
print(sol.isPalindrome(-121))