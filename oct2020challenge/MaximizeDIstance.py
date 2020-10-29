from typing import List
'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1

Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.

Solution:
----------
1) First build an array with indexes of all items that are seated(1s)
2) next iterate through the above array taking differences between the current item and the previous item divided by 2
    including the item s[0], for a scenario where the first seat is empty, and the diffeence between length of elements and index of last non-empty seat,
    to include the case where the last seat is empty. 
3) The maximum of all these items would be the maximum distance to the closest person
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        if len(seats) <= 2:
            return len(seats) - 1

        s = [x for x in range(len(seats)) if seats[x] == 1]
        t = max([s[0]] + [int((s[x] - s[x-1])/2) for x in range(1, len(s))] + [len(seats) - 1 - s[-1]])
        return t
        
sol = Solution()
print(sol.maxDistToClosest([0,1]))