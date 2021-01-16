from typing import List
'''
You are given an integer n. An array nums of length n + 1 is generated in the following way:

nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.
'''
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nmap = {}
        nmap[0] = 0
        nmap[1] = 1
        res = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nmap[i] = nmap[i/2]
            else:
                tmp = (i - 1)/2
                nmap[i] = nmap[tmp] + nmap[tmp+1]
            res = max(res, nmap[i])
        #print(nmap)
        return res

sol = Solution()
#print(sol.getMaximumGenerated(7))
#print(sol.getMaximumGenerated(2))
print(sol.getMaximumGenerated(3))