
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if len(trips) == 1:
            if trips[0] > capacity: return False 
            else:return True

        trips = sorted(trips, key =lambda x:(x[1], x[2]))

        print(trips)
        curcap = trips[0][0]
        prevtrip = trips[0]
        for i in range(1, len(trips)):
            if trips[i][1] < prevtrip[2] and trips[i][0] + prevtrip[0] > capacity:
                return False
                
            if trips[i][2] > prevtrip[2]:
                curcap = trips[i][0]
            elif prevtrip[2] == trips[i][2]:
                curcap += trips[i][0]
            elif prevtrip[2] > trips[i][2]:
                trips[i][2] = prevtrip[2]
                curcap = prevtrip[0]
            print("currrent capacity", curcap, "trip from,to", trips[i])
            if curcap > capacity:
                return False
            prevtrip = trips[i]


        return True


sol = Solution()
#print(sol.carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))
#print(sol.carPooling([[2,1,5],[3,3,7]], 4))
#print(sol.carPooling( [[2,1,5],[3,3,7]], 5))
#print(sol.carPooling([[2,1,5],[3,5,7]], 3))
print(sol.carPooling([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23))