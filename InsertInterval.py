from typing import List
import copy

class Solution:
    def isOverlapping(self, interval:List[int], newInterval:List[List])->bool:
        if (interval[0] < newInterval[0]) & (interval[1] < newInterval[0]):
            return False
        elif (interval[0] > newInterval[1]) & (interval[1] > newInterval[1]):
            return False
        
        return True
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if len(intervals) == 0:
            res.append(newInterval)
            return res

        minI = newInterval[0]
        maxI = newInterval[1]
        for i in range(len(intervals)):
            interval = intervals[i]
            if not self.isOverlapping(interval, newInterval):
                res.append(interval)
            else:
                minI = min(minI, interval[0], newInterval[0])
                maxI = max(maxI, interval[1], newInterval[1])

        res.append([minI, maxI])
        res = sorted(res)
        return res
                


if __name__ == "__main__":
    sol = Solution()
    print(sol.insert([[1,3],[6,9]], [2,5]))
    print(sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
    print(sol.insert([], [4,8]))
    print(sol.insert([[1,5]], [2,3]))
    print(sol.insert([[1,5]], [6,8]))
    print(sol.insert([[1,5]], [0,3]))
    print(sol.insert([[1,5]], [0,0]))
    print(sol.insert([[0,5],[8,9]], [3,4]))