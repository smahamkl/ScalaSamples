from typing import List

'''
LeetCode 881: You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. 
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person
'''
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        #---send people from the right side which is the heavier side and not from the left/lighter side---
        while l <= r:
            if people[r] == limit:
                r -= 1
                res += 1
                continue
            
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                res += 1
                continue
            
            r -= 1
            res += 1

        return res

sol = Solution()
print(sol.numRescueBoats([3,5,3,4], 5))
print(sol.numRescueBoats([1,2], 3))
print(sol.numRescueBoats([3,2,2,1], 3))
print(sol.numRescueBoats([5,1,4,2], 6))