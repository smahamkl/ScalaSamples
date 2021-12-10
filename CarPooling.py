
from typing import List
'''
Leetcode 1094
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 1:
            if trips[0] > capacity: return False 
            else:return True

        res = []
        for cap, st, end in trips:
            res.append((st, cap))
            res.append((end, -cap))
        
        res.sort()
        c = 0
        
        for p, cap in res:
            c += cap
            if c > capacity:
                return False


        return True


sol = Solution()
print(sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))
print(sol.carPooling([[2,1,5],[3,3,7]], 4))
print(sol.carPooling( [[2,1,5],[3,3,7]], 5))
print(sol.carPooling([[2,1,5],[3,5,7]], 3))
print(sol.carPooling([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23))