from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        totalLen = sum(matchsticks)
        print(totalLen)
        if totalLen % 4 != 0:
            return False

        totalLen = totalLen // 4

        print(totalLen)
        tmpSum = 0

        for item in matchsticks:
            tmpSum += item

            if tmpSum == totalLen:
                tmpSum = 0
            elif tmpSum > totalLen:
                return False
        
        if tmpSum >0 and tmpSum < totalLen:
            return False
        
        return True

sol = Solution()
# print(sol.makesquare([1,1,2,2,2]))
# print(sol.makesquare([3,3,3,3,4]))
print(sol.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))