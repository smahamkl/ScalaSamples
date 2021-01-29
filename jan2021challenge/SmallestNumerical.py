class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if k == 26*n: return 'z' * n
        nz, nshift = divmod(k - n, 25)
        return 'a' * (n - nz - 1) + chr(ord('a') + nshift) + 'z' * nz

sol = Solution()
print(sol.getSmallestString(85, 2159))