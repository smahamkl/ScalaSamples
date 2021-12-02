from collections import Counter, deque
from typing import List
import heapq

'''
Leetcode 621
https://www.youtube.com/watch?v=s8p8ukTyA2I&t=613s
'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        aggcnt = Counter(tasks)
        maxHeap = [-cnt for cnt in aggcnt.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        
        return time


sol = Solution()
#print(sol.leastInterval(["A","A","A","B","B","B"], 2))
#print(sol.leastInterval(["A","A","A","B","B","B"], 0))
#print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
print(sol.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))