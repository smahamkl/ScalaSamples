from typing import List

class Solution:
    def reverse(self, x: int) -> int:
        mul = -1 if x < 0 else 1
        print(mul)
        x1 = str(abs(x))[::-1]
        if (-1)*(2**31) <= int(x1) <= ((2**31)-1) :
            return int(x1) * mul
        else:
            return 0

sol = Solution()
print(2 ** 31 - 1)
print(sol.reverse(2**30))