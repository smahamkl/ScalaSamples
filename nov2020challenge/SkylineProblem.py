from typing import List
'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. 
Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output 
the skyline formed by these buildings collectively (Figure B).

Buildings Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates 
of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 
0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. 
A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark 
the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; 
the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
'''
class Solution:
    # #---return the left intersecting point of two buildings
    # def checkbuildingoverlap_left(self, building1, building2)-> [[]]:
    #     if building1 == building2:
    #         return [[]]
    #     elif building1[1] > building2[0]:
    #         #---if second building is taller than the first building it will have an intersecting point, else there wont be any intersecting
    #         if building2[2] > building1[2]:
    #             return [[building1[0], building1[2]], [building2[0], building2[2]]]
    #         else:
    #             return [[]]
    #     else:
    #         return [[]]
    
    # #---return the right intersecting point of two buildings
    # def checkbuildingoverlap_right(self, building1, building2)-> [[]]:
    #     if building1 == building2:
    #         return [[]]
    #     elif building1[1] > building2[0]:
    #         #---if second building is taller than the first building it will have an intersecting point, else there wont be any intersecting
    #         if (building2[2] > building1[2] and building2[1] < building1[1]) or (building2[2] < building1[2] and building2[1] > building1[1]):
    #             return [[min(building1[1], building2[1]), min(building2[2], building1[2])]]
    #         else:
    #             return [[]]
    #     else:
    #         return [[]]
        
    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    #     if len(buildings) == 0:
    #         return buildings
    #     elif len(buildings) == 1:
    #         return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

    #     buildings = sorted(buildings, key=lambda x:x[0])
    #     #print(buildings)
    #     prev = buildings[0]
    #     res = []
    #     res += [[prev[0], prev[2]]]
    #     for i in range(1, len(buildings)):
    #         #--check if the current building is behind previous building
    #         loverlaps = self.checkbuildingoverlap_left(prev, buildings[i])
    #         roverlaps = self.checkbuildingoverlap_right(prev, buildings[i])
    #         #print(loverlaps, roverlaps)
    #         if len(loverlaps[0])>0:
    #             res += loverlaps
    #         if len(roverlaps[0])>0:
    #             res += roverlaps
    #         if len(loverlaps[0]) == 0 and len(roverlaps[0]) == 0 and buildings[i][0] > buildings[i-1][1]:
    #             res += [[buildings[i-1][1], 0]]
    #             res += [[buildings[i][0], buildings[i][2]]]
    #         elif len(loverlaps[0]) == 0 and len(roverlaps[0]) == 0 and buildings[i][0] == buildings[i-1][1]:
    #             res += [[buildings[i-1][0], buildings[i-1][2]]]
    #             res += [[buildings[i][0], buildings[i][2]]]

    #         prev = buildings[i]
    #     res += [[buildings[len(buildings)-1][1], 0]]
    #     i = 1
    #     while i < len(res):
    #         if res[i-1][0] == res[i][0]:
    #             if res[i-1][1] > res[i][1]:
    #                 res.pop(i)
    #             else:
    #                 res.pop(i-1)
    #             continue
    #         elif res[i-1][1] == res[i][1]:
    #             if res[i-1][0] < res[i][0]:
    #                 res.pop(i)
    #             else:
    #                 res.pop(i-1)
    #             continue
    #         i += 1

    #     return res
    '''
    Process the data left to right. For any new building, unless the building currently atop the heap dominates it, push tuple (-Hi,-Ri) onto the heap. 
    These are negated because heapq implements a min-heap, while we want a max heap nested by height and right edge. Once finished processing any position x, 
    the top building on the heap will always be the max height of all buildings that continue beyond x, and it will also be the longest building among any 
    such buildings that are tied for that max height.

As we iterate moving left to right, we consider any positions x either from new buildings or from the top of the heap. Whenever the height of the building 
appearing atop the heap changes, append the new value to the skyline.

When all new buildings are exhausted, any further steps in the skyline must be drawn from the heap, descending in height and ascending in position. 
Stop once the height remaining atop the heap is zero, which indicates that all buildings have been processed and the only remaining item is (0,-maxsize) 
that was preset at the top of the function.
    '''
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if (not(buildings)):
            return([])
        import heapq
        from sys import maxsize
        H = [(0,-maxsize)]
        j=0
        skyline=[]
        while (j<len(buildings)):
            prev_h = -H[0][0]
            x = min(-H[0][1],buildings[j][0])
            while ((-H[0][1]) <= x):
                heapq.heappop(H)
            while ((j<len(buildings)) and (buildings[j][0]==x)):
                B = buildings[j]
                if ((B[2]>-H[0][0]) or (B[1]>-H[0][1])):
                    heapq.heappush(H,(-B[2],-B[1]))
                j+=1
            if (-H[0][0] != prev_h):
                skyline.append([x,-H[0][0]])
        x = (-H[0][1])
        heapq.heappop(H)
        while (-H[0][0]>0):
            if (-H[0][1]>x):
                skyline.append([x,-H[0][0]])
                x = (-H[0][1])
            heapq.heappop(H)
        skyline.append([x,0])        
        return(skyline)

sol = Solution()
print(sol.getSkyline([ [2,9,10], [3,7,15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
print(sol.getSkyline([]))
print(sol.getSkyline([[0,1,3]]))
print(sol.getSkyline([[0,2,3],[2,5,3]]))
print(sol.getSkyline([[0,3,3],[1,5,3],[2,4,3],[3,7,3]]))
print(sol.getSkyline([[1,5,3],[1,5,3],[1,5,3]]))
print(sol.getSkyline([[2,4,7],[2,4,5],[2,4,6]]))
print(sol.getSkyline([[3,10,20],[3,9,19],[3,8,18],[3,7,17],[3,6,16],[3,5,15],[3,4,14]]))