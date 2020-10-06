from typing import List
from collections import OrderedDict


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x : x[1])
        print(trips)
        l=len(trips)
        start=trips[0][1]
        end=max(i[2] for i in trips)
        drop={i:0 for i in range(start,end+1)}
        print(drop)
        num=0
        i=start
        pick=0
        while i<end+1:
            
            num-=drop[i]
            while i==trips[pick][1]:
                num+=trips[pick][0]
                if num>capacity:
                    return False
                drop[trips[pick][2]]+=trips[pick][0]
                pick+=1
                if pick==l:
                    return True
            
            print(drop)
            print("Total capacity:" + str(num))
            i+=1


sol = Solution()
print(sol.carPooling([[3, 2, 7], [3, 7, 9], [8, 3, 9]], 11))
#print(sol.carPooling([[2, 1, 5], [3, 5, 7]], 3))
