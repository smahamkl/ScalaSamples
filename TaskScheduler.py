from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        aggcnt = Counter(tasks)
        keys = aggcnt.keys
        res = [None for x in range(len(tasks) * max(n, 1))]

        for k in aggcnt:
            for i,ele in enumerate(res):
                if ele == None:
                    tmp = i
                    for l in range(aggcnt[k]):
                        res[tmp] = k
                        tmp += max(len(aggcnt), n+1)
                    break

        while not res[-1]:
            res.pop()

        for ele in res:
            print(ele, end=",")
        
        print()
        return len(res)

        


sol = Solution()
#print(sol.leastInterval(["A","A","A","B","B","B"], 2))
#print(sol.leastInterval(["A","A","A","B","B","B"], 0))
#print(sol.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))
print(sol.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2))