from typing import List
from itertools import combinations
'''
The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)


Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
'''
class Solution:
    def findBoats(self, people, left, right, limit, res):
        if left < right:
            if people[right] + people[left] <= limit:
                return self.findBoats(people, left+1, right-1, limit, res+1)
            else:
               return self.findBoats(people, left, right-1, limit, res+1)
        elif left == right:
            return res + 1
        else:
            return res

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        if len(people) == 1:
            return 1
        elif people[0] + people[1] > limit:
            return len(people)

        return self.findBoats(people, 0, len(people)-1, limit, 0)

sol = Solution()
print(sol.numRescueBoats([3,2,2,1], 3))
print(sol.numRescueBoats([3,5,3,4], 5))
print(sol.numRescueBoats([1,2], 3))
print(sol.numRescueBoats([1], 3))