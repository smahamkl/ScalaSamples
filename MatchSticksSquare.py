from typing import List
'''
LeetCode 473. Matchsticks to Square
https://www.youtube.com/watch?v=hUe0cUKV-YY
'''
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        
        sideLength = sum(matchsticks) // 4
        eachSide = [0] * 4

        if sum(matchsticks)/4 !=  sideLength:
            return False

        matchsticks.sort(reverse=True)
        def back_track(i:int) -> bool:
            if i >= len(matchsticks):
                return True
            
            for k in range(4):

                if eachSide[k] + matchsticks[i] <= sideLength:

                    eachSide[k] += matchsticks[i]

                    if back_track(i+1):
                        return True
                        
                    eachSide[k] -= matchsticks[i]
                
            return False
        return back_track(0)
        

sol = Solution()
# print(sol.makesquare([1,1,2,2,2]))
# print(sol.makesquare([3,3,3,3,4]))
print(sol.makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))