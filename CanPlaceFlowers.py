from typing import List

'''
LeetCode 605
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

        if len(flowerbed) == 1:
            if n == 1 and flowerbed[0] == 0:
                return True
            elif n == 0:
                return True
            else:
                return False

'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n-= 1
                elif i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n-=1
        
        return True if n == 0 else False

sol = Solution()
print(sol.canPlaceFlowers([1,0,0,0,1], 1))
print(sol.canPlaceFlowers([1,0,0,0,1], 2))
print(sol.canPlaceFlowers([0,1,0,0,0,0], 2))
print(sol.canPlaceFlowers([0,0,0], 2))
print(sol.canPlaceFlowers([1], 1))