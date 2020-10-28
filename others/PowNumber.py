from typing import List

class Solution:
    #----recursion causes depth exceeded error----
    # def compute_pow1(self, x:float, n:int) -> float:
    #     if n > 0:
    #         return x * self.compute_pow(x, n-1)
    #     else:
    #         return 1
    # #----this is also not going to work------
    # def compute_pow2(self, x:float, n:int) -> float:
    #     pow_arr = [0 for x in range(n)]
    #     pow_arr[0] = x
    #     for idx in range(1, len(pow_arr)):
    #         pow_arr[idx] = pow_arr[idx-1] * x
        
    #     return pow_arr[n-1]
    
    # def compute_pow(self, x:float, n:int) -> float:
    #     if n % 2 == 0 and n > 2:
    #         tmp = float(n / 2)
    #         return self.compute_pow(x, tmp) * self.compute_pow(x, tmp)
    #     else:
    #         return float(x ** n)
        

    # def myPow(self, x: float, n: int) -> float:
    #     if n == 0 or x == 1:
    #         return 1
    #     elif x == 0:
    #         return 0
    #     elif n > 0:
    #         return self.compute_pow(x, n)
    #     else:
    #         return 1/self.compute_pow(x, -1 * n)

    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        elif n < 0: x, n = 1/x, abs(n)
        res, t = x, 1
        while n > 1:
            if n % 2: t *= res
            n //= 2
            res *= res
            
        return res * t

sol = Solution()
print(sol.myPow(2, 25))
# print(sol.myPow(2.1, 3))
# print(sol.myPow(2.00, -2))
# print(sol.myPow(0, -2))