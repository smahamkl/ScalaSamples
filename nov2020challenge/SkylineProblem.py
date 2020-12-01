from typing import List

class Solution:
    #---return the left intersecting point of two buildings
    def checkbuildingoverlap_left(self, building1, building2)-> []:
        if building1 == building2:
            return []
        elif building1[1] > building2[0]:
            #---if second building is taller than the first building it will have an intersecting point, else there wont be any intersecting
            if building2[2] > building1[2]:
                return [building1[0], building1[2]]
            else:
                return []
        else:
            return []
    
    #---return the right intersecting point of two buildings
    def checkbuildingoverlap_right(self, building1, building2)-> []:
        if building1 == building2:
            return []
        elif building1[1] > building2[0]:
            #---if second building is taller than the first building it will have an intersecting point, else there wont be any intersecting
            if (building2[2] > building1[2] and building2[1] < building1[1]) or (building2[2] < building1[2] and building2[1] > building1[1]):
                return [min(building1[1], building2[1]), min(building2[2], building1[2])]
            else:
                return []
        else:
            return []
        
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        buildings = sorted(buildings, key=lambda x:x[0])
        #print(buildings)
        prev = buildings[0]
        res = []
        for i in range(1, len(buildings)):
            #--check if the current building is behind previous building
            loverlaps = self.checkbuildingoverlap_left(prev, buildings[i])
            roverlaps = self.checkbuildingoverlap_right(prev, buildings[i])
            if len(loverlaps) > 0:
                res += [[loverlaps]]
            if len(roverlaps) > 0:
                res += [[roverlaps]]
            prev = buildings[i]
        
        print(res)

sol = Solution()
#print(sol.getSkyline([ [2,9,10], [3,7,15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]))
print(sol.getSkyline([ [2,9,10], [3,7,15], [5, 12, 12]]))