class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binstr = ""
        for i in range(1,n+1):
            binstr += "{0:b}".format(i)
        return int(binstr, 2) % (10**9 + 7)
sol = Solution()
print(sol.concatenatedBinary(42))